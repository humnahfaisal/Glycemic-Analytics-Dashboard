import streamlit as st
import pandas as pd
def show(df):
    st.title("1. Dataset Overview")
    st.markdown("**Source:** Pima Indians Diabetes Database (Kaggle / UCI)")
    st.markdown("---")
    st.subheader("Quick Summary")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Total Patients",len(df))
    c2.metric("Variables",len(df.columns))
    c3.metric("Diabetic Cases",int(df["Outcome"].sum()))
    c4.metric("Diabetes Rate",f"{df['Outcome'].mean()*100:.1f}%")
    st.markdown("---")
    st.subheader("Variable Descriptions")
    var_info = {
        "Variable": ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"],
        "Type": ["Integer","Continuous","Continuous","Continuous","Continuous","Continuous","Continuous","Integer","Binary"],
        "Description": ["Number of times pregnant","Plasma glucose concentration (mg/dL)","Diastolic blood pressure (mm Hg)","Triceps skin fold thickness (mm)","2-Hour serum insulin (mu U/ml)","Body Mass Index — weight(kg) / height(m)²","Diabetes pedigree function score","Age in years","0 = Non-Diabetic,  1 = Diabetic"]
    }
    st.table(pd.DataFrame(var_info))
    st.markdown("---")
    st.subheader("Raw Data Preview")
    st.dataframe(df.head(10),use_container_width=True)
    st.markdown("---")
    st.subheader("Class Distribution")
    counts=df["Outcome"].value_counts().rename({0:"Non-Diabetic",1:"Diabetic"})
    st.bar_chart(counts)