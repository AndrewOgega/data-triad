<h1 align="center">Credit Card Default Prediction</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-00e9ed?logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-e06666?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Docker-8cc1f0?logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/BigQuery-4285F4?logo=googlebigquery&logoColor=white" alt="BigQuery">
  <img src="https://img.shields.io/badge/Classification-ML-brightgreen" alt="ML">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
</p>

---

## 📌 Project Overview

This project builds a machine learning pipeline to predict credit card defaulting using open-source BigQuery data. It combines data engineering, exploratory data analysis (EDA), and ensemble ML modeling using tools like **XGBoost**, **CatBoost**, and **LightGBM**. The models are trained with class imbalance handling, evaluated with classification metrics, and saved for downstream use.

An optional **FastAPI** backend and **Streamlit** interface are also included for for model deployment and user interaction.

---

## 🔧 Technologies Used

* **Python 3.10**
* **FastAPI** (for serving predictions)
* **Docker** (for containerization)
* **Pandas, Seaborn, Matplotlib** (EDA)
* **XGBoost, CatBoost, LightGBM** (ML models)
* **Scikit-learn, Imbalanced-learn** (preprocessing, pipelines)
* **Google BigQuery** (data source)
* **Streamlit** (for frontend interface)

---

## 📁 Project Structure

```bash
credit-default-prediction/
├── data_pipeline.py            # Data ingestion from BigQuery or local CSV
├── modeling_notebook.ipynb     # Full training pipeline, EDA, evaluation
├── models/                     # Pickled models (xgb, catboost, lgbm, stacked)
├── .env                        # Contains BigQuery service account key path
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/AndrewOgega/data-triad
cd credit-default-prediction
```

### 2. Setup environment

```bash
poetry install
```

### 3. Configure BigQuery Access

Create a `.env` file with the following content:

```env
BQ_KEY="path/to/your/service-account-key.json"
```

### 4. Run the modeling pipeline

Open `modeling_notebook.ipynb` in Jupyter or VS Code and run all cells.

Models will be saved automatically to the `models/` directory.

---

## ✅ Features

* Loads public dataset from **BigQuery**, falls back to CSV
* Cleans, transforms, and visualizes data
* Detects and handles class imbalance with:

  * `RandomOverSampler`
  * `scale_pos_weight`
* Trains models with `RandomizedSearchCV` hyperparameter tuning
* Combines top models using **StackingClassifier**
* Stores final models using `pickle`

---

## 🧠 Future Enhancements

* Add CI/CD with Docker + GitHub Actions
* Integrate MLFlow or DVC for experiment tracking

---

## 📊 Sample Visuals

******

---

## 📚 License

MIT License

---

## ✍🏾 Author

* Andrew Ogega

---

## 🔖 Tags

`python` · `fastapi` · `streamlit` · `docker` · `machine-learning` · `credit-scoring` · `xgboost` · `catboost` · `lightgbm` · `bigquery`

---

## 🤝 Contributions

Feel free to open issues or PRs — contributions are welcome!

---
