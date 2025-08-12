# Simple ML House Price Prediction Project

## Clone the repository

```bash
git clone https://github.com/CIRCLECI-GWP/house-price-prediction
cd house-price-prediction
```

This repository is meant to be cloned as part of the steps of following the related CircleCI blog tutorial.

The `circleci` branch has the CircleCI config included that aligns with the tutorial when completed.

## 1.1 Set up the virtual environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## Set up the virtual env uv

```bash
uv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt

# OR 

uv pip install -r requirements.txt
```

## Running the Scripts

### Preprocess the data

```bash
python src/preprocess.py
```

### Train the model

```bash
python src/train.py
```

### Evaluate the model

```bash
python src/evaluate.py
```


## Using DVC to run the Scripts

```bash
dvc repro # To reproduce all the steps for the ML model
```

```bash
dvc repro preprocess # to run a specific stage
```

> [!IMPORTANT] To change the Parameters for the ML runs, edit the params.yaml, i.e, change model value to B, C or D.
