
# 🍷 Wine Quality Prediction - MLOps Project

This is an end-to-end Machine Learning project built using a modular **MLOps architecture** to predict the quality of red wine. The project integrates data pipelines, configuration management, model training, validation, and deployment using Flask, making it both scalable and production-ready.

---

## 🔧 Tech Stack

- **Language**: Python 3.10
- **Libraries**: `scikit-learn`, `pandas`, `numpy`, `joblib`, `mlflow`, `flask`, `pyyaml`, `box`, `requests`
- **MLOps Tools**: Modular pipelines, configuration files (`YAML`), logging, artifact tracking
- **Frontend**: HTML + Flask templates
- **Model**: ElasticNet Regression

---

## 📊 Problem Statement

Predict the **quality of red wine** based on physicochemical properties like acidity, sugar, pH, alcohol, etc., using a regression-based ML model.

---

## 🗂️ Project Structure

```
.
├── config/
│   ├── config.yaml         # All pipeline stage settings
├── schema.yaml             # Data schema definition
├── params.yaml             # ML model hyperparameters
├── main.py                 # Pipeline trigger file
├── app.py                  # Flask web server
├── templates/
│   ├── index.html          # Input form UI
│   └── results.html        # Prediction output UI
├── src/
│   └── datascience/
│       ├── components/     # Modular logic for each ML pipeline stage
│       ├── config/         # Configuration manager
│       ├── pipeline/       # Stage-wise pipeline orchestration
│       ├── entity/         # Data classes for configs
│       ├── utils/          # Helper utilities
│       ├── constants/      # Constant path references
```

---

## ⚙️ How the Pipeline Works

Each ML pipeline stage is fully modularized and controlled via `config.yaml`. Here's the breakdown:

### 1️⃣ Data Ingestion
- Downloads ZIP from remote URL
- Extracts and stores the `winequality-red.csv` dataset

### 2️⃣ Data Validation
- Checks if columns match schema defined in `schema.yaml`

### 3️⃣ Data Transformation
- Splits data into train/test sets and stores as artifacts

### 4️⃣ Model Training
- Trains an ElasticNet regression model and saves it

### 5️⃣ Model Evaluation
- Logs MAE, RMSE, R² into metrics.json and MLflow

### 6️⃣ Web Deployment (Flask)
- Frontend form → backend prediction → result rendering

---

## 🚀 Quick Start

### 🧪 Local Setup

```bash
git clone https://github.com/your-username/wine-quality-mlops.git
cd wine-quality-mlops
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🏗️ Train the Model

```bash
python main.py
```

### 🌐 Launch Web App

```bash
python app.py
```
Visit `http://localhost:8080`

---

## ✅ Sample Inputs

- Fixed Acidity: `7.4`
- Volatile Acidity: `0.7`
- Citric Acid: `0.0`
- Residual Sugar: `1.9`
- Chlorides: `0.076`
- Free Sulfur Dioxide: `11.0`
- Total Sulfur Dioxide: `34.0`
- Density: `0.9978`
- pH: `3.51`
- Sulphates: `0.56`
- Alcohol: `9.4`

---

## 📬 Output

```
Predicted Wine Quality: 5.32
```

---

## 🧱 Modular Code Philosophy

Each pipeline step is decoupled into:
- `Entity` (Dataclasses) → inputs/configs
- `Component` → core logic
- `Pipeline` → executor
- `Utils` → common helpers (YAML, joblib, JSON)
- `Config` → bridges YAML to code

---

## 🔐 MLflow Integration

- Metrics are logged with `mlflow.log_metric()`
- Models are tracked via `mlflow.sklearn.log_model()`
- Uses DagsHub as a remote MLflow backend

---

## 📌 Configuration Examples

**config.yaml**
```yaml
model_trainer:
  root_dir: artifacts/model_trainer
  model_name: model.joblib
```

**params.yaml**
```yaml
ElasticNet:
  alpha: 0.2
  l1_ratio: 0.1
```

**schema.yaml**
```yaml
COLUMNS:
  fixed acidity: float64
  quality: int64
```

---

## ✨ Features

- ✅ Modular MLOps structure
- ✅ YAML-driven config
- ✅ Flask-based frontend
- ✅ MLflow + DagsHub integration

---

## 🙌 Credits

- [UCI Wine Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- Project inspired by Krish Naik's modular ML architecture
