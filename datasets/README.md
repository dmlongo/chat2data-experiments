# Datasets for Chat2Data Experiments

This document provides details on the datasets used for evaluating verification and enrichment workflows. The datasets are categorized into **industrial datasets** (Competitor Relationship and Product Substitution) and **cross-domain datasets** (Disease Ontology, Drug-to-Drug Interactions, and ArXiv Research Areas) to assess our methods across diverse domains.

## Industrial Datasets

### Competitor Relationship Dataset
This dataset was constructed from the **Owler Competitors Database**, one of the world's largest collections of company relationship data. It includes:
- **200 challenging competitor pairs** selected from the Owler dataset.
- **Ground truth labels** corrected by domain experts after being initially misclassified by an internal rule-based system.
- **Entities from the same industry** with similar features, making classification difficult.
- **Challenges addressed:** 
  - The difficulty of determining competitor relationships, even for human experts.
  - The cost and inaccuracy of crowdsourced data.
  - The need for automated verification and enrichment.

*Note: Due to data privacy considerations, this dataset is not publicly available. Researchers may request access through appropriate agreements.*

### Product Substitution Relationship Dataset
This dataset was created from the **Amazon Shopping Queries Dataset** and contains:
- **400 product pairs** labeled as *substitutes* or *not substitutes*.
- **Product titles and descriptions** used for semantic matching.
- **Eight product categories** defined for sampling:
  1. Clothing
  2. Jewelry & Accessories
  3. Shoes
  4. Home, Kitchen & Appliances
  5. Audio & Video Electronics
  6. Hobbies, Toys & Musical Instruments
  7. Health & Personal Care
  8. Sports & Outdoors

## Cross-Domain Datasets

### Disease Ontology Dataset
This dataset is derived from the **Disease Ontology 2015 update**, a structured biomedical knowledge base of human diseases. It focuses on **hierarchical `is_a` relationships**, where a *child disease* is a subtype of a *parent disease*.
- **Example:** *Juvenile rheumatoid arthritis* is a child disease of *rheumatoid arthritis*.
- **Dataset Preparation:**
  - Filtered instances where lexical similarities biased the evaluation.
  - Generated **negative samples** using three methods:
    1. **Random Mismatch:** Pairing child diseases with incorrect parent diseases.
    2. **Role Reversal:** Reversing parent-child relationships.
    3. **Sibling Substitution:** Selecting incorrect parent diseases from the same broader category.

### Drug-to-Drug Interactions Dataset
This dataset is derived from **DrugBank**, a comprehensive database providing detailed chemical, pharmacological, and pharmaceutical data on drugs and their targets. 

- **Dataset Focus:** Drug-drug interactions (DDIs), which occur when one drug alters the effect of another, leading to enhanced, diminished, or new effects.
- **SMILES Notation:** Each drug is represented using the **Simplified Molecular Input Line Entry System (SMILES)**, allowing computational modeling and analysis.
- **Graph Representation:**
  - Nodes represent drugs.
  - Edges represent known drug-drug interactions.
  - Positive samples are actual known interactions, while negative samples are drug pairs without a known interaction.
- **Sampling Strategy:**
  - **100 positive edges** (known interactions)
  - **100 negative edges** (randomly sampled non-interacting drugs)
  - Each drug includes definitions and SMILES notation as features.

### ArXiv Research Areas Dataset
This dataset was built from **arXiv metadata** containing information on over **2 million scholarly articles** across various scientific fields. The dataset contains:
- **203,961 titles and abstracts** categorized into **130 distinct classes**.
- **Hierarchical structure** following arXiv's category taxonomy.
- **Sampling Strategy:**
  - **500 positive pairs**: Papers from the same third-level subcategory.
  - **500 hard negative pairs**: Papers from the same broader subcategory but different third-level categories.

*Citations needed for this dataset.*

---

This document will be updated as more details become available.

