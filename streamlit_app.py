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
    icon=":material/house:"
)

eda = st.Page(
    "pages/02_eda.py",
    title="Exploratory Data Analysis",
    icon=":material/analytics:"
)

hypothesis1 = st.Page(
    "pages/03_hypothesis1.py",
    title="Hypothesis 1",
    icon=":material/biotech:"
)

hypothesis2 = st.Page(
    "pages/04_hypothesis2.py",
    title="Hypothesis 2",
    icon=":material/biotech:"
)

hypothesis3 = st.Page(
    "pages/05_hypothesis3.py",
    title="Hypothesis 3",
    icon=":material/biotech:"
)

clustering = st.Page(
    "pages/06_clustering.py",
    title="Clustering",
    icon=":material/bubble_chart:"
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
