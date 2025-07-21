# 🎓 Student Performance Prediction

An end-to-end machine learning project to predict student academic performance based on various socio-demographic and academic features. This project leverages modern MLOps practices using **MLflow**, **DVC**, and **Dagshub** for experiment tracking, reproducibility, and collaboration.

---

## 🧠 Problem Statement

The goal is to build a regression model that accurately predicts student final performance (e.g., total score) using features such as parental education, study time, absences, test scores, and more.

---

## 📦 Tech Stack

| Category            | Tools/Libraries                 |
| ------------------- | ------------------------------- |
| Programming         | Python 3.x                      |
| Data Manipulation   | pandas, numpy                   |
| Visualization       | matplotlib, seaborn             |
| Model Development   | scikit-learn, xgboost, catboost |
| Experiment Tracking | MLflow                          |
| Version Control     | DVC                             |
| Remote Tracking     | Dagshub                         |
| Web Framework       | Flask                           |

---

## 📁 Project Structure

```
student-performance-prediction/
├── data/                        # Raw and processed data
├── artifacts/                  # Stored models and preprocessing objects
├── dvc.yaml                    # DVC pipeline
├── mlruns/                     # MLflow experiments
├── notebooks/                  # EDA and experiment notebooks
├── src/
│   ├── components/             # Data transformation and modeling logic
│   ├── pipelines/              # Training and prediction pipelines
│   ├── utils/                  # Utility functions
│   └── config/                 # Configuration management
├── templates/                  # HTML templates for Flask UI
├── app.py                      # Flask web app entry point
├── requirements.txt            # Project dependencies
├── setup.py                    # Project packaging
└── README.md                   # Project documentation
```

---

## 🔁 End-to-End Pipeline

1. **Data Ingestion**: Load data from source and split into train/test.
2. **EDA**: Visualize patterns, detect outliers, handle missing data.
3. **Data Transformation**:

   * Feature engineering
   * Categorical encoding
   * Missing value imputation
   * Scaling using `ColumnTransformer`
4. **Model Training**:

   * Train multiple regression models
   * Use GridSearchCV for hyperparameter tuning
   * Log experiments with **MLflow**
5. **Model Evaluation**:

   * Compare all models using R², RMSE, and MAE
   * Select best model
6. **Model Deployment**:

   * Flask UI to accept user input and show predictions
7. **MLOps Integration**:

   * Track data & model versions using **DVC** + **Dagshub**
   * Track experiments using **MLflow**

---

## 📊 Models Trained

| Model                   | Test R² | Train R² | Best Params               |
| ----------------------- | ------- | -------- | ------------------------- |
| **ElasticNet**          | 0.88076 | 0.87430  | alpha=0.01, l1\_ratio=0.9 |
| Linear Regression       | 0.88043 | 0.87432  | —                         |
| Lasso                   | 0.88070 | 0.87431  | alpha=0.01                |
| Ridge                   | 0.88045 | 0.87432  | alpha=0.1                 |
| Gradient Boosting       | 0.86794 | 0.88838  | lr=0.05, depth=3          |
| CatBoost Regressor      | 0.86778 | 0.88764  | lr=0.05, depth=4          |
| XGBoost Regressor       | 0.86448 | 0.90111  | depth=3                   |
| AdaBoost Regressor      | 0.85532 | 0.85268  | n\_est=200                |
| Decision Tree           | 0.82423 | 0.85501  | max\_depth=5              |
| Random Forest Regressor | 0.81151 | 0.97531  | max\_features=log2        |
| K-Neighbors Regressor   | 0.62865 | 0.99965  | n\_neighbors=7            |

✅ **Best Model (ElasticNet)**:

* **R² Score**: `0.88075`
* **MAE**: `4.21`
* **RMSE**: `5.39`

---

## 📈 Experiment Tracking

### 🧪 MLflow

* All experiments logged: metrics, parameters, models
* Easily compare model performance in UI

### 📂 DVC + Dagshub

* Track data versioning and model artifacts
* Push/pull data from remote Dagshub storage

---

## 🖥️ Web Application

* Built using Flask
* Accepts user inputs via web form
* Predicts final student performance using best model

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your_username/student-performance-prediction.git
cd student-performance-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start MLflow UI (Optional)

```bash
mlflow ui
```

### 4. Run the application

```bash
python app.py
```

---

## 📌 Future Improvements

* Integrate model monitoring and drift detection
* Deploy using Docker and CI/CD pipelines
* Add advanced interpretability (SHAP/LIME)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

[MIT License](LICENSE)

---

## 🙋‍♂️ Acknowledgements

* scikit-learn, XGBoost, CatBoost, MLflow, DVC, Dagshub
* Special thanks to the open-source community ✨

---

> *"Predicting performance is not just about numbers—it's about empowering better decisions."*
