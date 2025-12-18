import streamlit as st
import pandas as pd
import sys
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from utils.data_processing import load_data
from utils.visualisation import plot_scatter

st.subheader("🎵 Hypothesis 1: Features vs. Popularity")


st.markdown("""
$H_{0}$ : There is no statistically significant relationship between a track’s danceability or energy and its popularity score.
            """)
st.markdown("""
$H_{1}$ : Tracks with higher danceability and energy have significantly higher popularity scores than tracks with lower values.
""")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "clean"

INPUT_CSV = DATA_DIR / "spotify_clean.csv"

df = load_data(INPUT_CSV)
df_sample = df.sample(n=1000, random_state=42)

r_dance, p_dance = pearsonr(df["danceability"], df["popularity"])
r_energy, p_energy = pearsonr(df["energy"], df["popularity"])

st.subheader("Popularity vs. Danceability")

st.markdown(f"Popularity vs. Danceability: $r = {r_dance:.3f}, p = {p_dance:.4f}$")


fig1 = plot_scatter(
    df_sample,
    x_col="danceability",
    y_col="popularity",
    title="Danceability vs Popularity with Regression Line",
    xlabel="Danceability",
    ylabel="Popularity",
    trend=True
)

st.plotly_chart(fig1)

fig2 = plot_scatter(
    df_sample,
    x_col="energy",
    y_col="popularity",
    title="Energy vs Popularity with Regression Line",
    xlabel="Energy",
    ylabel="Popularity",
    trend=True
)

st.subheader("Popularity vs. Energy")

st.markdown(f"Popularity vs Energy: $r = {r_energy:.3f}, p = {p_energy:.4f}$")

st.plotly_chart(fig2)

st.markdown("""
##### What this means:

**Danceability**

- The correlation is positive but weak.
- The very small p-value indicates the relationship is statistically significant.
- However, the effect size is small, meaning:
    - Danceability does influence popularity, but only slightly.
    - It is not a strong predictor on its own.

✅ Statistically significant

⚠️ Practically weak

**Energy**

- The correlation coefficient is close to zero.
- Despite the p-value being below 0.05, the effect size is negligible.
- This suggests:
    - With a large dataset, even tiny relationships can appear significant.
    - Energy alone does not meaningfully explain popularity.

⚠️ Statistically significant but not practically meaningful
            """)


st.subheader("🧪 Hypothesis Decision")

st.markdown("""
        Null Hypothesis ($H_{0}$)

There is no statistically significant relationship between danceability or energy and popularity.

#### Decision

- Danceability: ❌ Reject H₀ (weak but significant relationship)
- Energy: ⚠️ Fail to reject H₀ in practical terms (effect ≈ 0)
           
           
           
           """)