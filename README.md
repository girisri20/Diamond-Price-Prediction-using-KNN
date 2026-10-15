# Diamond-Price-Prediction-using-KNN
End-to-end Machine Learning web application for Diamond Price Prediction built using Scikit-Learn (KNN Regressor) and deployed on Streamlit Cloud.

# About the Project 
# 💎 Diamond Price Prediction App

An end-to-end Machine Learning project that predicts the price of diamonds based on their physical attributes (carat, cut, color, clarity, dimensions) using a **K-Nearest Neighbors (KNN) Regressor**. The model is packaged into an interactive web application and deployed using **Streamlit Cloud**.

---

## 🚀 Project Overview
* **Objective:** Build a complete ML pipeline from data loading and preprocessing to model training, evaluation, and cloud deployment.
* **Algorithm:** K-Nearest Neighbors (KNN) Regression
* **Deployment Platform:** Streamlit Cloud

---

## 📂 Project Structure
```text
├── diamonds.csv          # Dataset containing diamond characteristics and prices
├── description.txt       # Dataset feature documentation
├── train.py              # ML pipeline script (Preprocessing, Training, Evaluation, Saving)
├── model.pkl             # Serialized trained KNN Regressor pipeline
├── app.py                # Streamlit web application script
└── requirements.txt      # Project dependencies for cloud deployment
