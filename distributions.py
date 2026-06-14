import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
def show(df):
    st.title("4. Probability Distributions")
    st.markdown("---")
    dist = st.selectbox("Choose a distribution", [
        "4.9  Normal Distribution",
        "4.10 Poisson Distribution",
        "4.11 Uniform Distribution",
        "4.12 Binomial Distribution",
    ])
    st.markdown("---")
    fig,ax=plt.subplots(figsize=(9,4))
    if dist=="4.9  Normal Distribution":
        x=np.linspace(-4,4,300)
        y=stats.norm.pdf(x)
        ax.plot(x,y,color="steelblue",linewidth=2)
        ax.fill_between(x,y,where=(x>=-1)&(x<=1),alpha=0.3,color="steelblue",label="68% (±1σ)")
        ax.fill_between(x,y,where=((x>=-2)&(x<-1))|((x>1)&(x<=2)),alpha=0.2,color="orange",label="95% (±2σ)")
        ax.set_title("Normal Distribution  (μ = 0, σ = 1)")
        ax.set_xlabel("x")
        ax.set_ylabel("Probability Density")
        ax.legend()
        st.pyplot(fig)
        st.info("The bell curve is symmetric around mean = 0. "
                "68% of values fall within ±1σ and 95% within ±2σ. "
                "In this dataset, Glucose and BMI approximately follow a normal distribution.")
    elif dist=="4.10 Poisson Distribution":
        lam=st.slider("Lambda (λ) — average count",1,15,4)
        x=np.arange(0,20)
        y=stats.poisson.pmf(x,lam)
        ax.bar(x,y,color="mediumpurple",edgecolor="white")
        ax.set_title(f"Poisson Distribution  (λ = {lam})")
        ax.set_xlabel("k (number of events)")
        ax.set_ylabel("P(X = k)")
        st.pyplot(fig)
        st.info(f"With λ = {lam}, the most likely count is around {lam} events. "
                "In this dataset, Pregnancies follows approximately a Poisson distribution.")
    elif dist=="4.11 Uniform Distribution":
        x=np.linspace(-0.5,1.5,400)
        y=stats.uniform.pdf(x,0,1)
        ax.plot(x, y, color="seagreen", linewidth=2)
        ax.fill_between(x,y,where=(x>=0)&(x<=1),alpha=0.2,color="seagreen")
        ax.set_ylim(0,1.5)
        ax.set_title("Uniform Distribution  U(0, 1)")
        ax.set_xlabel("x")
        ax.set_ylabel("Probability Density f(x) = 1")
        st.pyplot(fig)
        st.info("A uniform distribution gives equal probability to all values in [0, 1]. "
                "f(x) = 1/(b-a) = 1. It is used as a baseline/null model.")
    elif dist=="4.12 Binomial Distribution":
        n_trials=st.slider("n (number of trials)",5,30,10)
        p_success=st.slider("p (success probability)",0.1,0.9,0.5,step=0.05)
        x=np.arange(0,n_trials+1)
        y=stats.binom.pmf(x,n_trials,p_success)
        ax.bar(x,y,color="steelblue",edgecolor="white")
        ax.axvline(n_trials*p_success,color="red",linestyle="--",label=f"Mean={n_trials*p_success:.1f}")
        ax.set_title(f"Binomial Distribution  (n = {n_trials}, p = {p_success})")
        ax.set_xlabel("k (number of successes)")
        ax.set_ylabel("P(X = k)")
        ax.legend()
        st.pyplot(fig)
        st.info(f"With n={n_trials} trials and p={p_success}, the expected number of successes is "
                f"n×p = {n_trials*p_success:.1f}. The Outcome variable is a special case (n=1, Bernoulli).")