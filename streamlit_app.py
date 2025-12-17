import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu

#---------------------Main entry page------------------------------------#

st.set_page_config(
    page_title = "Spotify Track Recommendation Engine",
    page_icon = "🎵",
    layout = "wide",
    initial_sidebar_state="expanded",
)
# #---------------Hide default sidebar---------------------#
# st.markdown(
#     """
#     <style>
#     [data-testid="stSidebarNav"] {
#         display: none;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

#Display banner at top

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image("Images/banner_image.jpg", width = 1300)

st.markdown("""
         
        Spotify Track Recommendation Engine.
         Navigate using the sidebar to explore diffeent sections of this dashboard.
         - **Developed by:** AudioBuddy Inc.
            - **Creators**: Ali Khurshid, Robert, Collins, Thomas
         """)


#-----------Define pages for navigation--------------------------#

homepage = st.page("pages/01_home.py",
                   title = "Home",
                   icon = ":material/home:")
EDA = st.page("pages/02_EDA.py",
                   title = "Exploratory Data Analysis",
                   icon = ":material/bar chart:")
Hypotheses = st.page("pages/03_Hypotheses.py",
                   title = "Hypotheses",
                   icon = ":material/experiment:")
Clustering = st.page("pages/04_Clustering.py",
                   title = "Clustering",
                   icon = ":material/hive:")


#setup navigation

nav = st.navigation({
"home":"Overview",
"EDA" : "Exploratory Data Analysis"
 "Hypotheses": [
        hypothesis1,
        hypothesis2,
        hypothesis3,
        hypothesis4,
    ],
"Analysis":[
    clustering
    ],
})
