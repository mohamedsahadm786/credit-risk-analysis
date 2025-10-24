# 🧮 Credit Risk Analysis (Binary Classification) — Streamlit App + Notebook

## 📌 Overview
A practical **credit risk classification** project that predicts whether granting credit to an applicant is **GOOD** (low risk) or **BAD** (high risk).  
Built with a full analytics workflow — **Python (EDA + Modeling)** and a **Streamlit** web app for real-time scoring.

---

## 🎯 Business Problem
Financial institutions need to **minimize default risk** while **maximizing approval throughput**.  
This solution helps **separate low-risk (GOOD)** applicants from **high-risk (BAD)** ones to support **data-driven lending decisions**, reduce **NPLs**, and improve **portfolio quality**.

---

## 🧩 Tech Stack & Keywords (ATS-Friendly)
**Python**, **Pandas**, **NumPy**, **scikit-learn**, **Joblib**, **Streamlit**, **Label Encoding**, **Binary Classification**, **Model Deployment**, **Risk Scoring**, **Feature Engineering**, **ML Pipeline**, **EDA**, **Imbalanced Learning** (if applicable), **MLOps (lightweight)**.

---

## 🗂️ Features Used (Model Inputs)
- `Age` (numeric)  
- `Sex` (categorical: *male/female*)  
- `Job` (ordinal: *0–3*)  
- `Housing` (categorical: *own/rent/free*)  
- `Saving accounts` (categorical: *little/moderate/rich/quite rich*)  
- `Checking account` (categorical: *little/moderate/rich*)  
- `Credit amount` (numeric)  
- `Duration` (months, numeric)

> Categorical variables are **encoded** via pre-trained encoders saved as `"{col}_encoder.pkl"`. The model is loaded from `best_model.pkl`.  

---

## 🧠 Modeling Pipeline (Notebook)
1. **Data Ingestion & EDA** — schema checks, missing values, distributions, correlations.  
2. **Preprocessing** — type casting, categorical encoding (**LabelEncoder**/equivalent), train/test split.  
3. **Modeling** — train a classifier (e.g., Logistic Regression / Random Forest / XGBoost, as per notebook), tune hyperparameters, evaluate on hold-out set.  
4. **Serialization** — persist **`best_model.pkl`** and **encoders** (`Sex`, `Housing`, `Saving accounts`, `Checking account`) using **Joblib**.  
5. **App Integration** — wire the trained artifacts to the Streamlit UI for instant predictions.

> **Prediction Meaning:** `GOOD` = credit can be granted; `BAD` = high risk (do not grant).

---

## 🖥️ Streamlit App (Interactive Scoring)
The app collects applicant info, applies the **saved encoders**, creates a feature vector, and returns a **GOOD/BAD** decision instantly.

**UI Inputs:** Age, Sex, Job, Housing, Saving accounts, Checking account, Credit amount, Duration  
**Output:**  
- ✅ **GOOD** — low risk  
- ❌ **BAD** — high risk

---

## 🧪 Local Setup & Run
```bash
# 1) Create & activate env
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt
# If you don't have a requirements file yet:
# pip install streamlit pandas scikit-learn joblib

# 3) Place trained artifacts in project root
#   - best_model.pkl
#   - Sex_encoder.pkl
#   - Housing_encoder.pkl
#   - Saving accounts_encoder.pkl
#   - Checking account_encoder.pkl

# 4) Launch Streamlit
streamlit run app.py
```

---

## 📁 Suggested Repository Structure
```
credit-risk-analysis/
├── notebooks/
│   └── Credit Risk.ipynb
├── app/
│   └── app.py
├── models/
│   ├── best_model.pkl
│   ├── Sex_encoder.pkl
│   ├── Housing_encoder.pkl
│   ├── Saving accounts_encoder.pkl
│   └── Checking account_encoder.pkl
├── data/
│   ├── raw/        # (optional)
│   └── processed/  # (optional)
├── reports/
│   └── model_card.md
├── requirements.txt
└── README.md
```

---

## 🧾 Example: Minimal `requirements.txt`
```txt
streamlit
pandas
scikit-learn
joblib
numpy
```

---

## 📊 (Optional) Model Card Essentials
- **Objective:** Binary classification — predict **GOOD/BAD** credit risk.  
- **Training Data:** (dataset source/shape, features, timeframe)  
- **Algorithm:** (e.g., Logistic Regression / Random Forest / XGBoost)  
- **Evaluation:** Accuracy, Precision/Recall (BAD class), F1, ROC-AUC, Confusion Matrix  
- **Fairness:** Check performance across `Sex`, `Age` brackets, and `Housing` groups.  
- **Limitations:** Shift risk, data quality, missing bureau signals.

---

## 🚀 Resume-Ready Impact Bullets (Copy for your CV)
- **Built and deployed a credit risk classifier** with a Streamlit app, transforming applicant data via **label encoders** and serving real-time **GOOD/BAD** risk decisions; productionized artifacts with **Joblib** for fast, consistent inference.  
- **Engineered a reproducible ML pipeline** (EDA → preprocessing → training → serialization → app), reducing manual scoring time and enabling **instant lending decisions** with explainable, auditable inputs.

---

## 🔖 Repo Topics (GitHub SEO)
`credit-risk`, `binary-classification`, `streamlit-app`, `python`, `scikit-learn`, `joblib`, `feature-engineering`, `model-deployment`, `risk-scoring`, `mlops-lite`
