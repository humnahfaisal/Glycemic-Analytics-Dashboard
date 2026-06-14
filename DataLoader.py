import pandas as pd
import numpy as np
import streamlit as st
@st.cache_data
def load_data():
    """
    Load the Pima Indians Diabetes dataset.
    Try to read from diabetes.csv — if not found, generate sample data.
    """
    try:
        df = pd.read_csv("diabetes.csv")
        st.success("Real diabetes.csv file loaded successfully.")
    except FileNotFoundError:
        st.warning("diabetes.csv not found. Random sample data generated.")
        np.random.seed(42)
        n = 768
        outcome = np.random.binomial(1, 0.349, n)
        df = pd.DataFrame({
            "Pregnancies":              np.clip(np.random.poisson(3.8, n), 0, 17).astype(int),
            "Glucose":                  np.where(outcome == 0,
                                            np.random.normal(110, 25, n),
                                            np.random.normal(143, 30, n)).clip(50, 200).round(1),
            "BloodPressure":            np.where(outcome == 0,
                                            np.random.normal(70, 12, n),
                                            np.random.normal(75, 13, n)).clip(30, 122).round(1),
            "SkinThickness":            np.where(outcome == 0,
                                            np.random.normal(27, 12, n),
                                            np.random.normal(33, 14, n)).clip(0, 99).round(1),
            "Insulin":                  np.clip(np.random.exponential(100, n), 0, 846).round(1),
            "BMI":                      np.where(outcome == 0,
                                            np.random.normal(30.5, 7, n),
                                            np.random.normal(35.4, 7, n)).clip(18, 67).round(1),
            "DiabetesPedigreeFunction": np.clip(np.random.exponential(0.47, n), 0.078, 2.42).round(3),
            "Age":                      np.clip(np.random.gamma(5, 6.5, n), 21, 81).astype(int),
            "Outcome":                  outcome
        })

    return df