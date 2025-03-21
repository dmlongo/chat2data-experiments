# Chat2Data: Experiments & Evaluations

This repository contains experiments, baselines, and evaluations for **Chat2Data**, focusing on **data verification** and **data enrichment** tasks across multiple datasets. It includes both the experiments from our paper and additional ones that could not be included due to space constraints.

We provide code for:
- Running **baseline classifiers** (e.g., Logistic Regression, GaussianNB, MLP)
- Evaluating **GPT-based baselines**
- Performing enrichment and verification workflows

> 📌 **Note:** Some datasets are proprietary or too large to include directly in the repository. See [data/README.md](data/README.md) for details and instructions.

---

## 🔍 Tasks Overview

### **1. Data Verification**
- Goal: Identify whether a semantic relationship (e.g., competitor, substitution) between two entities is valid.
- Models: Traditional classifiers and GPT-based approaches.
- Datasets: Industrial and cross-domain.

### **2. Data Enrichment**
- Goal: Generate or suggest new candidate entities for semantic relationships.
- Models: Primarily GPT-based.
- Datasets: Only industrial.

---

## 📁 Repository Structure

```
.
├── data/
├── enrichment/
├── verification/
```

- **`data/`**  
  Contains datasets (when possible), links to external or private datasets, and metadata. See `data/README.md` for full details.

- **`verification/`**  
  Code and notebooks for data verification experiments, including traditional classifiers and GPT-based evaluations.

- **`enrichment/`**  
  Scripts and resources related to data enrichment experiments, primarily using generative models.

---

## 📊 Datasets

The following datasets are used across tasks:

- **Industrial Datasets:**
  - Competitor Relationship *(private)*
  - Product Substitution *(included as `products_substitution.csv`)*

- **Cross-Domain Datasets:**
  - Disease Ontology
  - Drug-to-Drug Interactions
  - ArXiv Research Areas

👉 See [data/README.md](data/README.md) for descriptions, access information, and citations.

---

## 🧪 Running the Experiments

### Prerequisites
Install dependencies:
```bash
pip install -r requirements.txt
```

### Baseline Classifiers
Classifier baselines for each dataset are provided as Jupyter notebooks inside `verification/baselines/`.

Example:
```bash
jupyter notebook verification/baselines/products_substitution_classifiers.ipynb
```

### GPT Baselines
Evaluation scripts and instructions for GPT-based baselines are in:
```
verification/evaluations/
```

### Data Enrichment
Enrichment-specific scripts are located under:
```
enrichment/
```

---

## 📎 License

This code is distributed for research purposes. License terms coming soon.

---

## ✏️ Citation

If you use this codebase, please cite the original paper (to be added upon publication).

---

For questions or collaboration inquiries, feel free to reach out!
