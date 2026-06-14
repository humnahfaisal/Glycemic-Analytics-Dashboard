import os
import streamlit as st
from DataLoader import load_data
st.set_page_config(
    page_title="Glycemic Analytics",
    page_icon="logo.jpeg",
    layout="wide"
)
df=load_data()
logoPath=os.path.join(os.path.dirname(__file__),"logo.jpeg")
st.sidebar.image(logoPath,width=280)
st.sidebar.markdown("**Diabetes Statistical Analysis**")
st.sidebar.markdown("---")
page=st.sidebar.radio(
    "Go to section",
    [
        "1. Overview & Dataset",
        "2. Visualizations",
        "3. Descriptive Statistics & CI",
        "4. Probability Distributions",
        "5. Regression & Prediction",
    ]
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Group: Glycemic Analytics**")
st.sidebar.markdown("24F-0673 Hadia Awan  \n24F-0726 Hamna Faisal  \n24F-0518 Nehal Aftab  \n24F-3043 M Saim Naveed  \n23F-3113 Ahmed Naeem")
st.sidebar.markdown("**Course:** MT2005  \n**Semester:** Spring 2026")
if page=="1. Overview & Dataset":
    from modules.overview import show
    show(df)
elif page=="2. Visualizations":
    from modules.visulaizations import show
    show(df)
elif page=="3. Descriptive Statistics & CI":
    from modules.descriptivestats import show
    show(df)
elif page=="4. Probability Distributions":
    from modules.distributions import show
    show(df)
elif page=="5. Regression & Prediction":
    from modules.regression import show
    show(df)