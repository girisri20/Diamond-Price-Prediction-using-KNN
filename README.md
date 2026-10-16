# 💎 Diamond Price Prediction Using KNN

An end-to-end Machine Learning project that predicts diamond prices based on their physical dimensions and quality characteristics. The project uses a **K-Nearest Neighbors (KNN) Regressor** and a Streamlit web application to provide interactive price predictions.

## 📌 Project Overview

The objective of this project is to build and deploy a machine learning regression model that estimates diamond prices using features such as carat, cut, color, clarity, depth, table, and physical dimensions.

The project covers data preprocessing, feature scaling, categorical encoding, model training, evaluation, serialization, and web application development.

## 🎯 Objectives

- Perform data preparation and exploratory analysis.
- Encode categorical features using `OneHotEncoder`.
- Scale numerical features using `StandardScaler`.
- Train a KNN regression model.
- Evaluate model performance using regression metrics.
- Save the trained pipeline using Pickle.
- Build an interactive web application using Streamlit.

## 📊 Dataset

The project uses a diamond dataset containing **53,940 records** and the following features:

| Feature | Description |
|---|---|
| `carat` | Diamond weight |
| `cut` | Quality of the diamond's cut |
| `color` | Diamond color grade |
| `clarity` | Diamond clarity grade |
| `depth` | Total depth percentage |
| `table` | Width of the top facet relative to the widest point |
| `x` | Length in millimeters |
| `y` | Width in millimeters |
| `z` | Depth in millimeters |
| `price` | Target variable: diamond price |

## 🛠️ Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- K-Nearest Neighbors (KNN) Regression
- OneHotEncoder
- StandardScaler
- Scikit-learn Pipeline and ColumnTransformer
- Pickle
- Streamlit
- Jupyter Notebook

## ⚙️ Machine Learning Workflow

1. Load the dataset and inspect its structure.
2. Separate input features from the target variable.
3. Split the dataset into training and testing sets using a 75:25 ratio.
4. Apply standard scaling to numerical features.
5. Apply one-hot encoding to categorical features.
6. Train the KNN Regressor with `n_neighbors=5`.
7. Evaluate predictions using MAE, RMSE, and R².
8. Save the trained preprocessing and prediction pipeline.
9. Load the model into a Streamlit application for interactive predictions.

## 📈 Model Evaluation

The model is evaluated using three regression metrics:

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted prices.
- **Root Mean Squared Error (RMSE):** Measures prediction error while penalizing larger errors more heavily.
- **R² Score:** Measures how well the model explains the variation in diamond prices.

Add the final evaluation results from your notebook here after confirming the metrics for the model you are deploying.

## 🌐 Streamlit Application

The application allows users to enter diamond characteristics and receive an estimated price.

**Features:**
- Interactive input fields
- Categorical selections for cut, color, and clarity
- Numerical inputs for carat, depth, table, and dimensions
- On-demand price prediction
- Display of the estimated diamond price

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## 📁 Project Structure

```text
Diamond-Price-Prediction/
├── app.py
├── model.pkl
├── requirements.txt
├── diamonds.csv
├── Diamond_Price_Prediction_using_KNN_and_Streamlit_Deployment.ipynb
└── README.md
```

## 🔮 Future Improvements

- Compare KNN with other regression algorithms.
- Tune hyperparameters using cross-validation.
- Improve feature selection and model performance.
- Add prediction visualizations and model comparison charts.
- Deploy the application publicly using Streamlit Community Cloud.

## 👨‍💻 Project Purpose

This project demonstrates practical machine learning skills, including preprocessing, regression modeling, model evaluation, pipeline development, and interactive application deployment.
