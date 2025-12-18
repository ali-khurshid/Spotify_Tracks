import pandas as pd
from pathlib import Path
import plotly.express as px
from scipy.stats import mannwhitneyu
import streamlit as st

from utils.data_processing import load_data
from utils.visualisation import plot_violin

st.title("🎵 Hypothesis 2 — Popularity of Explicit vs Non-Explicit Tracks")

st.markdown("""$H_0$: There is no statistically significant difference in average 
            popularity between explicit and non-explicit tracks.""")

st.markdown("""$H_1$: Explicit tracks are, on average, more popular than 
            non-explicit tracks.""")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "clean"
INPUT_CSV = DATA_DIR / "spotify_clean.csv"
# load csv into dataframe
df = load_data(INPUT_CSV)
# take a sample of the dataframe 
df_sample = df.sample(n=1000, random_state=42)

# perform statistical test
explicit = df[df["explicit"] == True]["popularity"]
clean = df[df["explicit"] == False]["popularity"]

stat, p = mannwhitneyu(explicit, clean, alternative="two-sided")

fig = plot_violin(df,
            x_col="explicit",
            y_col="popularity",
            title="Popularity Distribution by Explicit Content",
            xlabel="Explicit Content",
            ylabel="Popularity",
            points=None)
st.plotly_chart(fig)

st.subheader("Mann-Whitney U test")

st.markdown("""We can check for a statistical difference between 
            the two groups by using a Mann-Whitney U test""")
st.markdown(f"p value: **{p:.2e}**")
st.markdown("""A p-value this low (≪ 0.05) in a Mann-Whitney U test 
            indicates very strong evidence against the null hypothesis, 
            meaning the distributions of the two groups are statistically 
            significantly different and the observed difference is 
            extremely unlikely to have occurred by chance.
            """)