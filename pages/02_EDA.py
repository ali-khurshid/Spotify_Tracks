"""
Exploratory Data Analysis Page
"""

import streamlit as st


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
