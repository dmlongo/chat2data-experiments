#!/usr/bin/env python3
import argparse
import asyncio
import json
import logging
import os
import random
import re
from datetime import datetime

import pandas as pd
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_openai import ChatOpenAI

from prompts import GPT4o_SAME_RESEARCH_TOPIC_PROMPT_v2

# Set up structured logging: logs will be written to both file and console.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("experiment.log"), logging.StreamHandler()],
)

# Default configuration parameters.
DEFAULT_MODEL_NAME = "gpt-4o"
DEFAULT_MAX_CONCURRENCY = 5
DEFAULT_BATCH_SIZE = 20
DEFAULT_TIMEOUT = 10  # seconds
DEFAULT_MAX_RETRIES = 3

# Global list to store failed responses.
failed_responses = []


def parse_args():
    parser = argparse.ArgumentParser(
        description="Process research paper pairs using GPT with robust error handling."
    )
    parser.add_argument(
        "--model", type=str, default=DEFAULT_MODEL_NAME, help="OpenAI model to use."
    )
    parser.add_argument(
        "--max_concurrency",
        type=int,
        default=DEFAULT_MAX_CONCURRENCY,
        help="Max number of concurrent API calls.",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help="Number of rows to process per batch.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help="Timeout for each API call in seconds.",
    )
    parser.add_argument(
        "--max_retries",
        type=int,
        default=DEFAULT_MAX_RETRIES,
        help="Maximum number of retries for each API call.",
    )
    return parser.parse_args()


def get_api_key():
    api_key = os.getenv("OPENAI_API_KEY_EXPERIMENTS")
    if not api_key:
        raise ValueError("Missing OpenAI API Key in environment variables.")
    return api_key


def initialize_chain(model_name, api_key):
    prompt = PromptTemplate(
        template=GPT4o_SAME_RESEARCH_TOPIC_PROMPT_v2,
        input_variables=["title_1", "abstract_1", "title_2", "abstract_2"],
    )
    llm = ChatOpenAI(model_name=model_name, openai_api_key=api_key)
    chain = prompt | llm | StrOutputParser()
    return chain


async def process_pair(row, semaphore, chain, max_retries, timeout):
    async with semaphore:
        input_data = {
            "title_1": row["title_1"],
            "abstract_1": row["abstract_1"],
            "title_2": row["title_2"],
            "abstract_2": row["abstract_2"],
        }
        response_str = "ERROR"
        for attempt in range(max_retries):
            try:
                # Enforce timeout for the API call.
                response_str = await asyncio.wait_for(
                    chain.ainvoke(input_data), timeout=timeout
                )

                # Clean response: remove markdown triple backticks and fix escape sequences.
                response_str = re.sub(
                    r"^```json\s*|\s*```$", "", response_str.strip(), flags=re.MULTILINE
                )
                response_str = response_str.encode("utf-8").decode("unicode_escape")

                # If response is JSON-like, parse it; otherwise, treat it as plain text.
                if response_str.startswith("{") and response_str.endswith("}"):
                    gpt_output = json.loads(response_str)
                    same_topic = gpt_output.get("same_topic", "Error")
                    explanation = gpt_output.get("explanation", "")
                else:
                    same_topic = "Unknown"
                    explanation = response_str
                true_label = "Yes" if str(row.get("label", "0")) == "1" else "No"
                return same_topic, explanation, true_label

            except asyncio.TimeoutError:
                error_message = "API timeout"
                logging.warning(
                    f"Timeout on attempt {attempt+1} for pair: {row['title_1']} | {row['title_2']}"
                )
            except json.JSONDecodeError:
                error_message = "Invalid JSON response"
                logging.warning(
                    f"JSON parse error on attempt {attempt+1} for pair: {row['title_1']} | {row['title_2']}"
                )
            except Exception as e:
                error_message = str(e)
                logging.error(
                    f"API error on attempt {attempt+1} for pair: {row['title_1']} | {row['title_2']} - {error_message}"
                )

            if attempt < max_retries - 1:
                # Wait with exponential backoff plus a random jitter.
                sleep_time = (2**attempt) + random.uniform(0, 1)
                await asyncio.sleep(sleep_time)
            else:
                # Final failure: log the error and record the failed response.
                failed_responses.append(
                    {
                        **input_data,
                        "gpt_raw_response": response_str,
                        "error": error_message,
                    }
                )
                true_label = "Yes" if str(row.get("label", "0")) == "1" else "No"
                return "Error", error_message, true_label


async def process_dataset_batches(
    test_df, max_concurrency, batch_size, chain, max_retries, timeout
):
    semaphore = asyncio.Semaphore(max_concurrency)
    for start in range(0, len(test_df), batch_size):
        batch = test_df.iloc[start : start + batch_size]
        tasks = [
            process_pair(row, semaphore, chain, max_retries, timeout)
            for _, row in batch.iterrows()
        ]
        results = [await future for future in asyncio.as_completed(tasks)]
        yield batch, results


def append_to_csv(df, filename):
    df.to_csv(
        filename,
        mode="a" if os.path.exists(filename) else "w",
        header=not os.path.exists(filename),
        index=False,
    )


async def main_async(
    df,
    chain,
    max_concurrency,
    batch_size,
    max_retries,
    timeout,
    results_filename,
    failed_filename,
):
    async for batch, results in process_dataset_batches(
        df, max_concurrency, batch_size, chain, max_retries, timeout
    ):
        predictions, explanations, true_labels = zip(*results)
        batch = batch.copy()
        batch["gpt_prediction"] = predictions
        batch["gpt_explanation"] = explanations
        batch["true_label"] = true_labels
        append_to_csv(batch, results_filename)
        logging.info(f"Processed batch ending at index {batch.index[-1]}")

    if failed_responses:
        append_to_csv(pd.DataFrame(failed_responses), failed_filename)
        logging.warning(f"{len(failed_responses)} failed responses logged.")


def main():
    args = parse_args()
    api_key = get_api_key()
    chain = initialize_chain(args.model, api_key)

    try:
        positive_df = pd.read_csv("positive_pairs_remaining.csv")
        negative_df = pd.read_csv("negative_pairs_remaining.csv")
    except Exception as e:
        logging.error(f"Error reading CSV files: {e}")
        return

    df = pd.concat([positive_df, negative_df], ignore_index=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_filename = f"{args.model}_classification_results_{timestamp}.csv"
    failed_filename = f"{args.model}_failed_responses_{timestamp}.csv"

    asyncio.run(
        main_async(
            df,
            chain,
            args.max_concurrency,
            args.batch_size,
            args.max_retries,
            args.timeout,
            results_filename,
            failed_filename,
        )
    )
    logging.info("Experiment completed.")


if __name__ == "__main__":
    main()
