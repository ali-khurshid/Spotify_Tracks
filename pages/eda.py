"""
Exploratory Data Analysis Page
"""
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import plotly.express as px
import seaborn as sns
import streamlit as st
from utils.data_processing import load_data

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "clean"
INPUT_CSV = DATA_DIR / "spotify_clean.csv"
# load csv into dataframe
df = load_data(INPUT_CSV)

st.subheader("Exploratory Data Analysis")

tab1, tab2, tab3 = st.tabs(["🧼 Data Cleaning",
                            "🛠️ Feature Engineering",
                            " 🔗 Correlations"])

with tab1:
    st.title("Reasons for cleaning the data")
    st.markdown("""
                Data cleaning is essential to ensure that dashboard insights
                are accurate, consistent, and meaningful. Raw music datasets
                often contain duplicate tracks, inconsistent naming
                conventions (e.g. remastered, live, or explicit versions),
                mixed data types, and missing or malformed values. If left
                unaddressed, these issues can lead to misleading
                visualisations, inflated counts, and unreliable comparisons.

                To address this, the function standardises track and artist
                names, resolves duplicate entries by retaining the most
                popular version of each track per primary artist, and enforces
                consistent data types across columns. Categorical fields are
                converted to optimised data types to improve dashboard
                performance, while date fields are safely parsed to prevent
                runtime errors.

                The resulting DataFrame is clean, deduplicated, and
                analysis-ready, ensuring that all dashboard visualisations
                accurately reflect underlying music trends and support
                reliable, insight-driven exploration by end users.
            """)
    
with tab2:
    st.title("Feature Engineering")
    st.subheader("Audio Features")
    st.markdown("""An important first step for this dataset was to separate 
                out the numerical features for the clustering task and the 
                metadata""")
    st.markdown("""We want to cluster the data on the audio features 
                such as **energy** and **dancability** rather than 
                **popularity** or **song duration**""")
    st.markdown("""We also wanted to engineer some new features which could
                help us to categorise the songs these were\n - **Dance Energy 
                Index**: the average value of energy and dancability. This 
                captures “movement intensity”. It separates upbeat dance 
                tracks from calm ones.\n - **Acoustic Profile**: the average 
                of acousticness and instrumentalness. This helps identify 
                acoustic / instrumental tracks.\n - **Mood Index**: the average 
                of valance and energy. This captures the emotion of the 
                song, i.e. sad vs happy.\n - **Vocal Presence**: 
                1 - instrumentalness. separates instrumental tracks from
                those with lots of speaking i.e. rap tracks.
                """)
with tab3:
    st.title("Correlations")

    plt.figure(figsize=(10,8))
    correlation_matrix = df.corr(numeric_only=True)
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Heatmap of Audio Features')
    st.pyplot(plt.gcf())
    plt.clf()

    st.markdown("""The correlation heatmap shows that most audio features 
                have **weak relationships with popularity**, suggesting no single 
                feature strongly drives popularity on its own. Strong 
                correlations appear mainly **between audio features themselves**, 
                such as energy and loudness (strong positive) and energy and 
                acousticness (strong negative), indicating expected musical 
                relationships rather than direct links to popularity.
                """)