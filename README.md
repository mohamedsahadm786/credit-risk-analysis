# 🧮 Credit Risk Analysis — Binary Classification & Scoring System  
**Python · scikit-learn · Risk Modeling · Model Deployment**

---

## 📌 Project Overview

This project builds a **credit risk classification system** to support **data-driven lending decisions** by predicting whether a loan applicant represents **LOW risk (GOOD)** or **HIGH risk (BAD)**.

The solution follows an **end-to-end machine learning workflow** — from **exploratory data analysis and feature engineering** to **model training, evaluation, and deployment-ready inference artifacts**.

The project is based on the **German Credit dataset**, a widely used benchmark for credit risk modeling, and is structured to reflect **real-world underwriting and risk analytics practices**.

---

## 🎯 Business Problem

Financial institutions must balance:
- **Risk minimization** (reducing defaults)
- **Operational efficiency** (faster approvals)
- **Consistent underwriting decisions**

Manual credit assessment is slow, subjective, and difficult to scale.

### Business Objective
> **Classify applicants into LOW-risk (GOOD) and HIGH-risk (BAD) segments to support consistent, automated, and data-driven credit approval decisions.**

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **scikit-learn**
- **Model serialization (pickle / joblib)**
- **Streamlit (deployment interface)**

---

## 📊 Dataset Summary

- **Source:** German Credit Dataset  
- **Target Variable:** `Risk` (GOOD / BAD)
- **Observations:** 1,000+ loan applicants
- **Feature Types:**
  - Demographic: Age, Sex, Job
  - Financial: Credit Amount, Duration
  - Account Information: Housing, Saving Accounts, Checking Account
  - Behavioral & Purpose-based attributes

---

## 🔄 Analytical Workflow

### 1️⃣ Exploratory Data Analysis (EDA)

Performed comprehensive EDA to understand data structure and risk patterns:

- Dataset shape, schema, and summary statistics
- Missing value analysis
- Distribution analysis:
  - Age
  - Job categories
  - Housing type
  - Saving and checking account status
- Risk distribution (GOOD vs BAD)
- Relationship analysis between:
  - Age and risk
  - Employment and risk
  - Account types and risk

EDA was used to guide **feature handling and model selection**, not just visualization.

---

### 2️⃣ Data Preprocessing & Feature Engineering

- Handled missing values in:
  - `Saving accounts`
  - `Checking account`
- Converted categorical variables using:
  - One-hot encoding (`pd.get_dummies`)
- Defined:
  - **Features (X)**
  - **Target (y)**
- Split data into:
  - Training set (70%)
  - Test set (30%)

---

### 3️⃣ Model Training & Evaluation

Multiple classification models were trained and compared:

#### 🔹 Logistic Regression
- Baseline, interpretable model
- Used as a reference for performance comparison

#### 🔹 Decision Tree Classifier
- Captured non-linear decision boundaries
- Evaluated trade-offs between interpretability and variance

#### 🔹 Random Forest Classifier
- Ensemble model for improved generalization
- Reduced overfitting compared to single-tree models
- Provided **feature importance rankings**

---

### 4️⃣ Model Evaluation Metrics

Models were evaluated using:
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix
- Class-wise performance comparison

Visual diagnostics included:
- Confusion matrix heatmaps
- Feature importance plots (Random Forest)

The final model was selected based on **risk discrimination performance**, not accuracy alone.

---

### 5️⃣ Feature Importance Analysis

Using the Random Forest model:
- Identified top predictors influencing credit risk
- Quantified feature impact on GOOD vs BAD classification
- Supported model transparency and underwriting explainability

---

### 6️⃣ Deployment-Ready Artifacts

To support real-time scoring:
- Trained model saved as `best_model.pkl`
- Encoders saved separately for categorical features:
  - Sex
  - Housing
  - Saving accounts
  - Checking account
  - Target label

These artifacts enable **consistent inference** outside the training environment.

---

### 7️⃣ Application Layer (Streamlit)

A lightweight **Streamlit application** was developed to:
- Accept applicant details
- Apply trained encoders
- Generate a real-time **GOOD / BAD risk classification**

The app simulates how such a model could be integrated into:
- Loan origination systems
- Credit underwriting workflows

---

## 📂 Repository Structure

```text
credit-risk-analysis/
│
├── app/
│   └── app.py
│
├── data/
│   └── german_credit_data.csv
│
├── models/
│   ├── best_model.pkl
│   ├── Checking_account_encoder.pkl
│   ├── Housing_encoder.pkl
│   ├── Saving_accounts_encoder.pkl
│   ├── Sex_encoder.pkl
│   └── target_encoder.pkl
│
├── notebook/
│   └── Credit_Risk.ipynb
│
├── requirements.txt
└── README.md
```

---

## 📈 Business Impact

- Enables **faster and more consistent credit decisions**
- Reduces dependency on manual underwriting
- Improves risk screening accuracy
- Provides a scalable foundation for automated credit scoring systems

---

## 🏁 Conclusion

This project demonstrates a **production-oriented credit risk modeling workflow**, combining:

- Statistical exploration
- Machine learning classification
- Model evaluation and interpretability
- Deployment-ready inference design

It reflects how **risk analytics and machine learning** are applied in real-world financial decision systems.

---

## 👤 Author

**Mohamed Sahad M**  
Master’s in Statistics  
Machine Learning | Risk Analytics | Python | scikit-learn  

