import streamlit as st

st.set_page_config(
    page_title="Spotify Track Recommendation Engine",
    page_icon="🎵",
    layout="wide",
)


# ---------- Define pages ----------
home = st.Page(
    "pages/01_home.py",
    title="Home",
)

eda = st.Page(
    "pages/02_eda.py",
    title="Exploratory Data Analysis",
)

hypothesis1 = st.Page(
    "pages/03_hypothesis1.py",
    title="Hypothesis 1",
)

hypothesis2 = st.Page(
    "pages/04_hypothesis2.py",
    title="Hypothesis 2",
)

hypothesis3 = st.Page(
    "pages/05_hypothesis3.py",
    title="Hypothesis 3",
)

clustering = st.Page(
    "pages/06_clustering.py",
    title="Clustering",
)

# ---------- Navigation ----------
nav = st.navigation(
    {
        "Main": [home],
        "EDA": [eda],
        "Analysis": [hypothesis1, hypothesis2, hypothesis3],
        "Clusters": [clustering],
    }
)

# ---------- REQUIRED ----------
nav.run()
