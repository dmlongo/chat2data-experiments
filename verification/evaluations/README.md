# Chat2Data Experiments Discussion

### Disease Ontology Dataset

To establish baseline performance and contextualize the efficacy of our proposed workflow, we employed established machine learning methodologies. Specifically, we utilized Naive Bayes, Logistic Regression, and Multi-layer Perceptron (MLP) classifiers, each trained on OpenAI embeddings derived from the 'childDefinition' and 'parentDefinition' columns of the Disease Ontology dataset.  

Furthermore, we evaluated the performance of our model using GPT-4o and o1 models in a zero-shot learning paradigm. This approach assessed the models' inherent capacity to discern hierarchical relationships without explicit training on the Disease Ontology dataset. We provided the official definition of the relationship along with the question whether the relationship is found between the child and parent disease. 

#### RESULTS


| Model                                      | Accuracy | Precision | Recall | Specificity | F1   |
|--------------------------------------------|----------|-----------|-------|-------------|------|
| OpenAI embedding + Naive Bayes Classifier  | 0.69     | 0.68      | 0.73  | 0.66        | 0.71 | 
 | OpenAI embeddings + Logistic Regression    | 0.68     | 0.67      | 0.72  | 0.65        | 0.7  |
| OpenAI embeddings + Multi-Layer Perceptron | 0.68     | 0.68      | 0.69  | 0.67        | 0.68 |
| Zeroshot gpt-4o                            | 0.83     | 0.74      | 0.88  | 0.79        | 0.80 |
| Zeroshot o1                                | 0.83     | 0.7       | 0.96  | 0.76        | 0.81 |
| Chat2Rel (using gpt-4o)                    | 0.95     | 1.0       | 0.9   | 1.0         | 0.95 |

Traditional classification methods that rely on similarity-based embeddings tend to underperform compared to large language model (LLM)–based methods in this dataset. One key reason is that the negative pairs in the dataset often have reversed directions or involve “sibling” diseases, which are closely related but placed incorrectly in the hierarchy. While traditional methods excel at leveraging similarity between diseases, they are less effective at capturing hierarchical relationships. In contrast, LLM-based approaches are inherently more explainable and can go beyond mere similarity to understand subtypes. Notably, introducing reasoning capabilities such as transitioning from GPT-4o to o1 and employing our workflow, which includes few-shot chain-of-thought (CoT) examples, improved the F1 score for this dataset.



### Drug-to-Drug Interactions Dataset


In our study on drug-drug interaction (DDI) prediction, we employed Graph Convolutional Networks (GCNs) under two distinct settings: one without node features and another incorporating molecular fingerprints as features.​

**GCN without Node Features:**
In the absence of specific node features, each drug is represented solely based on the graph's structural information, relying on the connectivity patterns within the DDI network. This approach allows the GCN to learn embeddings that capture the topological relationships between drugs, which can be indicative of potential interactions.

**GCN with Morgan Fingerprint Features:**
To enrich the model with chemical information, we utilized Morgan fingerprints as node features. Morgan fingerprints are a type of circular fingerprint that encodes the presence of substructures within a molecule, effectively capturing its chemical characteristics. In our implementation, the Morgan function computes these fingerprints for each drug based on its SMILES representation. In the Morgan function, the CircularFingerprint feature generator from the DeepChem library generates a 100-dimensional binary vector for each drug, reflecting the presence or absence of specific molecular substructures. These vectors serve as input features for the GCN, enabling the model to integrate both the structural topology of the DDI network and the chemical properties of individual drugs.

Drug information: https://deepchem.io/

GCN Model = https://arxiv.org/pdf/1609.02907

#### RESULTS

| Model                                      | Accuracy | Precision | Recall | Specificity | F1   |
|--------------------------------------------|----------|-----------|--------|-------------|------|
| Only GCN no node feature  | 0.68     | 0.89      | 0.41   | 0.95        | 0.56 | 
 | GCN + embeddings of features    | 0.71     | 0.88      | 0.51   | 0.93        | 0.64 |
| Zeroshot gpt-4o                            | 0.46     | 0.47      | 0.67   | 0.25        | 0.55 |
| Zeroshot o1                                | 0.76     | 0.82      | 0.67   | 0.85        | 0.74 |
| Chat2Rel (using gpt-4o)                 | 0.69     | 0.7       | 0.66   | 0.72        | 0.68 |

Drug-to-drug interaction constitutes a challenging, highly factual relationship. Graph Convolutional Networks (GCNs) harness topological features to model these interactions, whereas LLM-based models can draw upon their intrinsic knowledge of drug properties. While traditional methods (e.g., GCNs, regression-based algorithms) rely on optimized data-driven techniques, LLM-based methods enrich analysis through a deeper semantic understanding of the drugs themselves
Graph Convolutional Networks (GCN) focus on the chemical structure of drugs. They use a format called SMILES to capture how similar drugs are and how they connect to each other. On the other hand, Large Language Models (LLMs) can analyze drug interactions by looking at how drugs interact with biological targets or affect metabolic pathways in the body.
Our method helps to improve baseline gpt-4o knowledge by introducing few shots demonstrations on how to look for possible interactions between the drugs. However, o1's performance remains superior to our model.

### ArXiv Research Areas Dataset

We created paper pairs from the arXiv dataset for classification experiments. Positive pairs come from the same third-level subcategory, indicating a precise topical match. Negative pairs, or "hard negatives," are drawn from the same broad category but different third-level subcategories, sharing general topics but differing in specifics. We sampled the pairs to reflect the original distribution and saved the labeled pairs (1 for positive, 0 for negative) in CSV files.

To establish a baseline and assess our workflow's efficacy, we applied standard machine learning models, namely Naive Bayes, Logistic Regression, and Multi-layer Perceptron (MLP) classifiers, using OpenAI embeddings derived from the title and abstract of the arXiv dataset.

#### RESULTS


| Model                                      | Accuracy | Precision | Recall | Specificity | F1   |
|--------------------------------------------|----------|-----------|--------|-------------|------|
| OpenAI embedding + Naive Bayes Classifier  | 0.63     | 0.59      | 0.73   | 0.54        | 0.65 | 
 | OpenAI embeddings + Logistic Regression    | 0.64     | 0.6       | 0.74   | 0.55        | 0.66 |
| OpenAI embeddings + Multi-Layer Perceptron | 0.55     | 0.53      | 0.58   | 0.52        | 0.55 |
| Zeroshot gpt-4o                            | 0.76     | 0.8       | 0.69   | 0.83        | 0.74 |
| Zeroshot o1                                | 0.76     | 0.83      | 0.65   | 0.87        | 0.73 |
| Chat2Rel (using gpt-4o)                 | 0.79     | 0.73      | 0.92   | 0.66        | 0.81 |

The baseline models using OpenAI embeddings (Naive Bayes and Logistic Regression) perform similarly, with accuracies around 63–64% and F1 scores near 0.65–0.66. They maintain a balance between precision and recall but still leave room for improvement. The Multi-Layer Perceptron, however, shows lower performance with an accuracy of 55% and an F1 of 0.55.
In contrast, the Chat2Rel (using gpt-4o) reaches 79% accuracy, with a precision of 73%, recall of 92%, and an F1 score of 0.81. This indicates that Chat2Rel is more effective at capturing the relevant relationship, though its specificity of 0.66 implies a moderate number of false positives.

The zeroshot performance of gpt-4o and o1 outperforms the classical ML models, achieving better precision and F1 scores. However, Chat2Rel significantly improves recall and F1 score, albeit with a slight drop in precision. This result stems from the fact that Chat2Rel offers different perspectives through investigations based on diverse criteria.

Overall, these results suggest that while the baseline methods provide consistent performance, the specialized Chat2Rel approach offers notable improvements in detecting positive instances.


---

This document will be updated as more details become available.
