GPT4o_SAME_RESEARCH_TOPIC_PROMPT_v1 = """
You are given two research papers, each described by their titles and abstracts. Your task is to determine whether these two papers focus on exactly the same narrowly-defined research topic. Papers belong to the same narrowly-defined topic if their research is closely aligned at a very specific level, rather than just broadly related.

Paper 1:
Title: {title_1}
Abstract: {abstract_1}

Paper 2:
Title: {title_2}
Abstract: {abstract_2}

Provide your answer in JSON format without any additional text.
Output plain JSON without markdown formatting. Format as follows:
{{
  "same_topic": "Yes" or "No",
  "explanation": "Brief explanation of your reasoning."
}}
"""

GPT4o_SAME_RESEARCH_TOPIC_PROMPT_v2 = """
You are given two research papers, each described by its title and abstract. Your task is to determine whether the two papers focus on the same research topic. Two papers are considered to share a topic if they address a similar research question or tackle a similar problem statement.

Paper 1:
Title: {title_1}
Abstract: {abstract_1}

Paper 2:
Title: {title_2}
Abstract: {abstract_2}

Provide your answer in JSON format without any additional text.
Output plain JSON without markdown formatting. Format as follows:
{{
  "same_topic": "Yes" or "No",
  "explanation": "Brief explanation of your reasoning."
}}
"""