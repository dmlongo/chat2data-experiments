# Supplementary Material for Chat2Data Paper

This repository contains additional experiments and evaluations referenced in our paper. It includes datasets (where possible), full result tables, and discussions that further support the claims made in the main manuscript.

---

## 📌 Datasets Overview

We evaluate our methods on two types of datasets:

- **Industrial Datasets**
  - **Competitor Relationship Dataset**  
    🔒 *Private dataset. Not included in the repo due to confidentiality.*
  - **Product Substitution Dataset**  
    📂 Available at: [data/products_substitution.csv](data/products_substitution.csv)

- **Cross-Domain Datasets**  
  📂 Included in this repository:
  - [Disease Ontology](data/disease_ontology.csv)
  - [Drug-to-Drug Interactions](data/drug_interactions.csv)
  - [ArXiv Research Areas](data/arxiv_research_areas.csv)

For dataset details and access information, see [data/README.md](data/README.md).

---

## 📊 Additional Experimental Results

We provide summary tables for the main evaluation benchmarks below. For detailed analysis and full discussion of these results, please see the complete discussion in [verification/evaluations/README.md](verification/evaluations/README.md).

### Disease Ontology Dataset

| Model                                     | Accuracy | Precision | Recall | Specificity | F1   |
| ----------------------------------------- | -------- | --------- | ------ | ----------- | ---- |
| OpenAI embedding + Naive Bayes Classifier | 0.69     | 0.68      | 0.73   | 0.66        | 0.71 |
| OpenAI embedding + Logistic Regression    | 0.68     | 0.67      | 0.72   | 0.65        | 0.70 |
| OpenAI embedding + Multi-Layer Perceptron | 0.68     | 0.68      | 0.69   | 0.67        | 0.68 |
| Zeroshot GPT-4o                           | 0.83     | 0.74      | 0.88   | 0.79        | 0.80 |
| Zeroshot o1                               | 0.83     | 0.70      | 0.96   | 0.76        | 0.81 |
| Chat2Rel (using GPT-4o)                   | 0.95     | 1.00      | 0.90   | 1.00        | 0.95 |

**Discussion:**  
Traditional classifiers based on similarity embeddings underperform compared to LLMs. Negative pairs in this dataset often include reversed or sibling relationships, which LLMs like GPT-4o and o1 can distinguish more effectively. Chat2Rel further improves F1 score by introducing chain-of-thought reasoning, enhancing hierarchical understanding.

---

### Drug-to-Drug Interactions Dataset

| Model                      | Accuracy | Precision | Recall | Specificity | F1   |
| -------------------------- | -------- | --------- | ------ | ----------- | ---- |
| GCN (no node features)     | 0.68     | 0.89      | 0.41   | 0.95        | 0.56 |
| GCN + Molecular Embeddings | 0.71     | 0.88      | 0.51   | 0.93        | 0.64 |
| Zeroshot GPT-4o            | 0.46     | 0.47      | 0.67   | 0.25        | 0.55 |
| Zeroshot o1                | 0.76     | 0.82      | 0.67   | 0.85        | 0.74 |
| Chat2Rel (using GPT-4o)    | 0.69     | 0.70      | 0.66   | 0.72        | 0.68 |

**Discussion:**  
This is a challenging factual task. GCNs model chemical structures well, while LLMs like o1 incorporate semantic understanding of drug properties and interactions. Chat2Rel improves GPT-4o’s baseline by guiding its reasoning through few-shot examples, though o1 still outperforms it in this domain.

---

### ArXiv Research Areas Dataset

| Model                                     | Accuracy | Precision | Recall | Specificity | F1   |
| ----------------------------------------- | -------- | --------- | ------ | ----------- | ---- |
| OpenAI embedding + Naive Bayes Classifier | 0.63     | 0.59      | 0.73   | 0.54        | 0.65 |
| OpenAI embedding + Logistic Regression    | 0.64     | 0.60      | 0.74   | 0.55        | 0.66 |
| OpenAI embedding + Multi-Layer Perceptron | 0.55     | 0.53      | 0.58   | 0.52        | 0.55 |
| Zeroshot GPT-4o                           | 0.76     | 0.80      | 0.69   | 0.83        | 0.74 |
| Zeroshot o1                               | 0.76     | 0.83      | 0.65   | 0.87        | 0.73 |
| Chat2Rel (using GPT-4o)                   | 0.79     | 0.73      | 0.92   | 0.66        | 0.81 |

**Discussion:**  
While standard classifiers show balanced but limited performance, LLM-based models (GPT-4o, o1) and Chat2Rel significantly boost recall and F1. Chat2Rel’s higher recall indicates strong sensitivity in identifying topical similarity, while its lower specificity suggests occasional overprediction. Overall, Chat2Rel enhances relationship detection across subtle distinctions in research areas.

---

## 🔗 Links to Source Code

To reproduce or explore the experiments:

- **Verification**
  - 📄 [Classifier baselines (e.g., Naive Bayes, Logistic Regression)](verification/baselines/)
  - 📄 [GPT-based baselines](verification/baselines/)

- **Enrichment**
  - 📄 [Enrichment experiment scripts](enrichment/)

For dataset descriptions and access, see [data/README.md](data/README.md).

---

This document will be updated as more results become available or experiments are extended.

---

## 🗂️ Project Overview (for Developers)

Looking for repository structure, how to run the code, or implementation details?

👉 See [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
