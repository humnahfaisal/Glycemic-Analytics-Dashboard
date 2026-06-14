import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
def show(df):
    st.title("2. Graphical Visualizations")
    st.markdown("---")
    chart=st.selectbox("Choose a visualization",[
        "4.1 Histogram of Glucose",
        "4.2 BMI vs Age Scatter Plot",
        "4.5 Histogram of BMI",
        "4.6 Boxplot of Glucose by Outcome",
        "4.7 Correlation Matrix Heatmap",
        "4.8 Pie Chart of Outcome",
    ])
    st.markdown("---")
    fig,ax=plt.subplots(figsize=(9,4))
    if chart=="4.1 Histogram of Glucose":
        ax.hist(df["Glucose"], bins=25, color="steelblue", edgecolor="white")
        ax.axvline(df["Glucose"].mean(), color="red", linestyle="--",label=f"Mean = {df['Glucose'].mean():.1f}")
        ax.set_xlabel("Glucose (mg/dL)")
        ax.set_ylabel("Count")
        ax.set_title("Histogram of Glucose")
        ax.legend()
        st.pyplot(fig)
        st.info("""This histogram shows the distribution of glucose values. 
                The distribution is slightly right-skewed. The red line marks the mean (~121 mg/dL). 
                Values above 140 mg/dL are considered in the diabetic range.""")
    elif chart=="4.2 BMI vs Age Scatter Plot":
        colors=df["Outcome"].map({0:"steelblue",1:"tomato"})
        ax.scatter(df["Age"],df["BMI"],c=colors,alpha=0.5, s=20)
        ax.set_xlabel("Age (years)")
        ax.set_ylabel("BMI")
        ax.set_title("BMI vs Age (Blue = Non-Diabetic, Red = Diabetic)")
        st.pyplot(fig)
        st.info("Diabetic patients (red) tend to cluster at higher BMI values. "
                "Higher BMI combined with older age increases diabetes risk.")
    elif chart=="4.5 Histogram of BMI":
        ax.hist(df["BMI"],bins=25,color="orange",edgecolor="white")
        ax.axvline(df["BMI"].mean(), color="red", linestyle="--",label=f"Mean={df['BMI'].mean():.1f}")
        ax.axvline(30, color="green", linestyle=":", label="Obesity threshold (30)")
        ax.set_xlabel("BMI")
        ax.set_ylabel("Count")
        ax.set_title("Histogram of BMI")
        ax.legend()
        st.pyplot(fig)
        st.info("The green dotted line marks BMI = 30 (obesity threshold). "
                "Most patients fall in the overweight or obese range.")
    elif chart=="4.6 Boxplot of Glucose by Outcome":
        df["Outcome_Label"]=df["Outcome"].map({0: "Non-Diabetic", 1: "Diabetic"})
        sns.boxplot(data=df, x="Outcome_Label", y="Glucose",palette={"Non-Diabetic":"steelblue","Diabetic":"tomato"},ax=ax)
        ax.set_xlabel("Outcome")
        ax.set_ylabel("Glucose (mg/dL)")
        ax.set_title("Boxplot of Glucose by Outcome")
        st.pyplot(fig)
        st.info("Diabetic patients have significantly higher glucose levels. "
                "The median glucose for diabetic patients is ~140 mg/dL vs ~105 mg/dL for non-diabetic.")
    elif chart=="4.7 Correlation Matrix Heatmap":
        plt.close()
        fig,ax=plt.subplots(figsize=(9,6))
        corr = df.drop(columns=["Outcome_Label"], errors="ignore").corr()
        sns.heatmap(corr, annot=True,fmt=".2f", cmap="Blues",linewidths=0.5,ax=ax)
        ax.set_title("Correlation Matrix Heatmap")
        st.pyplot(fig)
        st.info("Glucose has the strongest positive correlation with Outcome. "
                "BMI and Age also show moderate correlation with diabetes.")
    elif chart=="4.8 Pie Chart of Outcome":
        counts=df["Outcome"].value_counts()
        ax.pie(counts,labels=["Non-Diabetic","Diabetic"],autopct="%1.1f%%",colors=["steelblue","tomato"],
               startangle=140)
        ax.set_title("Proportion of Diabetic vs Non-Diabetic")
        st.pyplot(fig)
        st.info("Approximately 65% of patients are non-diabetic and 35% are diabetic. "
                "This class imbalance is important for model building.")