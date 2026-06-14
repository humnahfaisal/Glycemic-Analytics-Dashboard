import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, confusion_matrix,classification_report)
@st.cache_data
def trainModel(df):
    X=df[["Glucose","BMI"]]
    y=df["Outcome"]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    model=LogisticRegression(max_iter=500)
    model.fit(X_train,y_train)
    yPred=model.predict(X_test)
    return model,X_test,y_test,yPred
def show(df):
    st.title("5. Regression & Prediction")
    st.markdown("---")
    model,X_test,y_test,yPred=trainModel(df)
    intercept=model.intercept_[0]
    coefGlucose=model.coef_[0][0]
    coefBmi=model.coef_[0][1]
    accuracy=accuracy_score(y_test,yPred)
    tab1,tab2,tab3=st.tabs([
        "5.1  Model Summary",
        "5.2  Model Evaluation",
        "5.3  Live Prediction",
    ])
    with tab1:
        st.subheader("Logistic Regression Summary")
        st.markdown("**Model:** `Outcome ~ Glucose + BMI`")
        coefDf=pd.DataFrame({
            "Term":["Intercept", "Glucose", "BMI"],
            "Coefficient":[round(intercept, 4),round(coefGlucose, 4),round(coefBmi, 4)],
            "Interpretation":[
                "Log-odds when Glucose = 0 and BMI = 0",
                f"Each +1 mg/dL glucose increases log-odds by {coefGlucose:.4f}",
                f"Each +1 unit BMI increases log-odds by {coefBmi:.4f}",
            ]
        })
        st.table(coefDf)
        st.markdown(f"""
**Model equation:**
```
log( p / 1-p ) = {intercept:.4f}+{coefGlucose:.4f}×Glucose+{coefBmi:.4f} × BMI
```
**Test-set Accuracy:** `{accuracy*100:.1f}%`
        """)
        st.markdown("---")
        st.markdown("**Predicted Probability vs Glucose (for different BMI values)**")
        fig,ax=plt.subplots(figsize=(9,4))
        glucRange=np.linspace(50,200,300)
        for bmiVal,color,label in [(25,"steelblue","BMI = 25"),(32,"orange","BMI=32"),(40,"tomato","BMI=40")]:
            z=intercept+coefGlucose*glucRange+coefBmi*bmiVal
            prob=1/(1+np.exp(-z))
            ax.plot(glucRange,prob,color=color,linewidth=2,label=label)
        ax.axhline(0.5, color="gray", linestyle="--", linewidth=1,label="Decision threshold (0.5)")
        ax.set_xlabel("Glucose (mg/dL)")
        ax.set_ylabel("P(Diabetic)")
        ax.set_title("Logistic Regression — Sigmoid Curves")
        ax.legend()
        st.pyplot(fig)
    with tab2:
        st.subheader("Model Evaluation")
        report=classification_report(y_test,yPred,output_dict=True)
        c1,c2,c3,c4=st.columns(4)
        c1.metric("Accuracy",f"{accuracy*100:.1f}%")
        c2.metric("Precision (Diabetic)",f"{report['1']['precision']*100:.1f}%")
        c3.metric("Recall (Diabetic)",f"{report['1']['recall']*100:.1f}%")
        c4.metric("F1-Score (Diabetic)",f"{report['1']['f1-score']*100:.1f}%")
        st.markdown("---")
        st.markdown("**Confusion Matrix**")
        cm = confusion_matrix(y_test, yPred)
        fig,ax=plt.subplots(figsize=(5,4))
        sns.heatmap(cm,annot=True,fmt="d",cmap="Blues",xticklabels=["Non-Diabetic","Diabetic"],yticklabels=["Non-Diabetic","Diabetic"],ax=ax,linewidths=0.5)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        ax.set_title("Confusion Matrix")
        st.pyplot(fig)
        st.markdown("""
**How to read the confusion matrix:**
- **Top-left** — Correctly predicted Non-Diabetic (True Negative)
- **Bottom-right** — Correctly predicted Diabetic (True Positive)
- **Top-right** — Non-Diabetic predicted as Diabetic (False Positive)
- **Bottom-left** — Diabetic predicted as Non-Diabetic (False Negative)
        """)
    with tab3:
        st.subheader("Live Diabetes Prediction")
        st.markdown("Enter patient values below to get an instant prediction.")
        st.markdown("---")
        col1,col2=st.columns(2)
        with col1:
            glucoseInput=st.slider("Glucose Level (mg/dL)",50,200,120)
        with col2:
            bmiInput=st.slider("BMI",15.0,67.0,32.0,step=0.5)
        st.markdown("---")
        if st.button("Predict"):
            prob=model.predict_proba([[glucoseInput,bmiInput]])[0][1]
            predicted=int(prob>0.5)
            if predicted==1:
                st.error(f"**Predicted Outcome: 1 — Diabetic**  \n"
                         f"Diabetes probability: **{prob*100:.1f}%**  \n"
                         f"Please consult a healthcare professional.")
            else:
                st.success(f"**Predicted Outcome: 0 — Non-Diabetic**  \n"
                           f"Diabetes probability: **{prob*100:.1f}%**  \n"
                           f"Values appear within a healthy range.")
            st.markdown("**Risk Probability Gauge**")
            fig,ax=plt.subplots(figsize=(9,1.2))
            ax.barh([""],[prob],color="tomato",height=0.4,label="Diabetic risk")
            ax.barh([""],[1 - prob],color="steelblue",height=0.4,left=[prob],label="Non-diabetic")
            ax.axvline(0.5,color="gray",linewidth=1.5,linestyle="--")
            ax.set_xlim(0,1)
            ax.set_xticks([0,0.25,0.5,0.75,1.0])
            ax.set_xticklabels(["0%","25%","50%","75%","100%"])
            ax.set_title(f"Predicted probability of diabetes: {prob*100:.1f}%")
            ax.legend(loc="upper right")
            st.pyplot(fig)
