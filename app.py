import streamlit as st
import pandas as pd
import pickle

# Page configuration
st.set_page_config(
    page_title="Diamond Price Prediction",
    page_icon="💎",
    layout="centered"
)

# Load the trained machine learning pipeline
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# App title and description
st.title("💎 Diamond Price Prediction")
st.write(
    "Enter the diamond's characteristics below to estimate its price "
    "using a K-Nearest Neighbors (KNN) regression model."
)

st.subheader("Diamond Details")

# Input fields
carat = st.number_input(
    "Carat",
    min_value=0.1,
    max_value=5.0,
    value=0.5,
    step=0.01
)

cut = st.selectbox(
    "Cut",
    ["Fair", "Good", "Very Good", "Premium", "Ideal"],
    index=4
)

color = st.selectbox(
    "Color",
    ["D", "E", "F", "G", "H", "I", "J"],
    index=3
)

clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"],
    index=2
)

depth = st.number_input(
    "Depth (%)",
    min_value=40.0,
    max_value=80.0,
    value=61.5,
    step=0.1
)

table = st.number_input(
    "Table (%)",
    min_value=40.0,
    max_value=80.0,
    value=57.0,
    step=0.1
)

x = st.number_input(
    "Length (mm)",
    min_value=0.0,
    max_value=15.0,
    value=5.0,
    step=0.1
)

y = st.number_input(
    "Width (mm)",
    min_value=0.0,
    max_value=15.0,
    value=5.0,
    step=0.1
)

z = st.number_input(
    "Depth (mm)",
    min_value=0.0,
    max_value=15.0,
    value=3.1,
    step=0.1
)

# Predict the diamond price
if st.button("Predict Diamond Price", type="primary"):
    input_data = pd.DataFrame([{
        "carat": carat,
        "cut": cut,
        "color": color,
        "clarity": clarity,
        "depth": depth,
        "table": table,
        "x": x,
        "y": y,
        "z": z
    }])

    try:
        predicted_price = model.predict(input_data)[0]
        st.success(f"Estimated Diamond Price: ${predicted_price:,.2f}")
        st.caption(
            "This is a model estimate, not a guaranteed market price."
        )
    except Exception as error:
        st.error("Prediction failed. Please check the saved model and input features.")
        st.exception(error)
