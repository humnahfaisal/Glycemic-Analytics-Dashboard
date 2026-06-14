import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def show(df):
    st.title("3. Descriptive Statistics & Confidence Intervals")
    st.markdown("---")
    numeric_cols =["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
    n=len(df)
    rows=[]
    for col in numeric_cols:
        s=df[col]
        mean_val=s.mean()
        std_val=s.std()
        se=std_val/np.sqrt(n)
        rows.append({
            "Variable":col,
            "Mean":round(mean_val,2),
            "Median":round(s.median(),2),
            "Std Dev":round(std_val,2),
            "Min":round(s.min(),2),
            "Max":round(s.max(),2),
            "95% CI Lower":round(mean_val-1.96*se,2),
            "95% CI Upper":round(mean_val+1.96*se,2),
        })
    stats_df = pd.DataFrame(rows)
    st.subheader("Summary Statistics Table (95% Confidence Intervals)")
    st.dataframe(stats_df.set_index("Variable"),use_container_width=True)
    st.markdown("""
    **How to read this table:**
    - **Mean** — average value across all 768 patients
    - **Std Dev** — how spread out the values are
    - **95% CI** — we are 95% confident the true population mean lies in this range
    - Formula used: `CI = Mean ± 1.96 × (SD / √n)`
    """)
    st.markdown("---")
    st.subheader("Detailed View — Pick a Variable")
    selected=st.selectbox("Select variable", numeric_cols)
    s=df[selected]
    mean_val=s.mean()
    std_val=s.std()
    se=std_val/np.sqrt(n)
    ci_low=mean_val-1.96*se
    ci_high=mean_val+1.96*se
    c1,c2,c3,c4,c5=st.columns(5)
    c1.metric("Mean",round(mean_val,2))
    c2.metric("Std Dev",round(std_val,2))
    c3.metric("95% CI Low",round(ci_low,2))
    c4.metric("95% CI High",round(ci_high,2))
    c5.metric("Sample Size",n)
    fig,ax=plt.subplots(figsize=(9,4))
    ax.hist(s,bins=25,color="steelblue",edgecolor="white",alpha=0.8)
    ax.axvline(mean_val,color="red",linestyle="--",linewidth=1.5,label=f"Mean ={mean_val:.2f}")
    ax.axvline(ci_low,color="green",linestyle=":",linewidth=1.5,label=f"95% CI Lower={ci_low:.2f}")
    ax.axvline(ci_high,color="green",linestyle=":",linewidth=1.5,label=f"95% CI Upper={ci_high:.2f}")
    ax.set_title(f"Distribution of {selected} with 95% CI")
    ax.set_xlabel(selected)
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)