# Chat2Data Experiments Repository

This repository contains the source code, datasets, and results for the experiments conducted in our research on **Chat2Data**. The goal is to provide a reproducible environment for our research, including classifiers, datasets, and evaluation results.

## Repository Structure

```
chat2data-experiments/
│── experiments/             # Scripts to run experiments and generate results
│── datasets/                # Data used in experiments (excluding competitors' data)
│   ├── dataset1/
│   ├── dataset2/
│   ├── dataset3/
│   ├── README.md            # Explanation of datasets, chosen pairs, and statistics
│── results/                 # Additional evaluation results
│── logs/                    # Log files from experiments
│── README.md                # Main documentation of the repo
│── requirements.txt         # Dependencies (if applicable)
│── scripts/                 # Utility scripts for pre-processing, evaluation, etc.
│── LICENSE                  # License file (if needed)
```

## Getting Started

### Prerequisites
Ensure you have the required dependencies installed before running the experiments.

```sh
pip install -r requirements.txt
```

### Running the Experiments
1. Clone this repository:
   ```sh
   git clone https://github.com/dmlongo/chat2data-experiments.git
   cd chat2data-experiments
   ```
2. Run classifiers:
   ```sh
   python classifiers/train.py --dataset datasets/dataset1
   ```
3. Evaluate results:
   ```sh
   python experiments/evaluate.py --results results/
   ```

## Datasets

This repository contains datasets used for the experiments (except competitor datasets). Each dataset folder includes:
- Raw data files
- Preprocessed versions (if applicable)
- Explanation of why the dataset was chosen
- Statistics about the dataset and chosen pairs

**Note:** Some datasets contain private/enterprise data and cannot be shared publicly.

## Results

- **Additional Evaluation Results**: Stored in `results/`
- **Mistake Analysis**: Cases where the system made errors can be found in `results/mistakes/`
- **Comparison with Other Methods**: Includes evaluations against alternative approaches in `results/comparisons/`

## Contact
For any inquiries, reach out to [Your Name] at [Your Email].

