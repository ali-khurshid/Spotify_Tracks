import streamlit as st
import sys
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
from utils.data_processing import load_data
from utils.visualisation import plot_scatter



st.subheader("🎵 Hypothesis 3: Acousticness vs. Energy and Popularity")

st.markdown("""
$H_{0}$ : There is no statistically significant relationship between acousticness and either energy or popularity.
            """)
st.markdown("""
$H_{1}$ : Tracks with high acousticness have lower energy and lower popularity.

             """)
    

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "clean"

INPUT_CSV = DATA_DIR / "spotify_clean.csv"

df = load_data(INPUT_CSV)
df_sample = df.sample(n=1000, random_state=42)

r1, p1 = spearmanr(df["acousticness"], df["energy"])
r2, p2 = spearmanr(df["acousticness"], df["popularity"])


st.subheader("Acousticness vs Energy")

st.markdown(f"Acousticness vs Energy: ρ={r1:.3f}, p={p1:.4f}")

fig1 = plot_scatter(
    df_sample,
    x_col="energy",
    y_col="acousticness",
    title="Energy vs Acousticness with Regression Line",
    xlabel="Energy",
    ylabel="Acousticness",
    trend=True
)

st.plotly_chart(fig1)

st.subheader("Acousticness vs Popularity")

st.markdown(f"Acousticness vs Popularity: ρ={r2:.3f}, p={p2:.4f}")

fig2 = plot_scatter(
    df_sample,
    x_col="popularity",
    y_col="acousticness",
    title="Popularity vs Acousticness with Regression Line",
    xlabel="Popularity",
    ylabel="Acousticness",
    trend=True
)

st.plotly_chart(fig2)

st.markdown("""
            #### What this means

Acousticness vs Energy
- The correlation is strong and negative.
- This indicates:
    - As acousticness increases, energy decreases substantially.
    -This aligns perfectly with musical intuition (acoustic tracks tend to be calmer).


##### Acousticness vs Popularity

- The correlation is extremely weak (close to zero).
- Despite statistical significance:
    - The effect size is negligible.
    - Popularity is not meaningfully related to acousticness alone.
            """)

st.markdown("""
            Null Hypothesis ($H_{0}$)

There is no statistically significant relationship between acousticness and either energy or popularity.
            """)

st.subheader("🧪 Hypothesis Decision")

st.markdown("""

- Energy: ❌ Reject H₀ (strong inverse relationship)
- Popularity: ⚠️ Fail to reject H₀ in practical terms

So:
- Hypothesis 3 is partially supported.
            """)