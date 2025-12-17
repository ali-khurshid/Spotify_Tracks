import streamlit as st

#Display banner at top


col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image("Images/banner_image.jpg", width = 1300)

st.markdown("""
Spotify tracks clustered by audio features.
Navigate using the sidebar to explore diffeent sections of this dashboard.      
         
- **Developed by:** AudioBuddy Inc.
- **Creators**: Ali Khurshid, Robert Steven Elliot , Collins, Tom Burgess
""")
#--------------Dataset section------------------#

st.subheader("Data Used")

st.markdown("""
            This dashboard is built using the Spotify tracks dataset downloaded from Kaggle: 
            
            https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset.
            
            It includes a range of over 125 different genres. Each track has some audio features associated with it.
            
            """)

st.subheader("Original Dataset")

st.markdown("""
The spotify tracks dataset includes audio features alongside names of artists and the popularity ratings of their songs.
This project aims to explore how the audio features are correlated to each other and the number of Hypotheses that can be created. 
These are then used for **Classification** purposes.
The dataset consists of the following features.
            """)
            
# Two columns for dataset features
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- `artists`  
- `name`  
- `popularity`  
- `duration_ms`  
- `explicit`  
- `danceability`  
- `energy`  
- `key`  
- `loudness`  
- `mode`  
""")

with col2:
    st.markdown("""
- `speechiness`  
- `acousticness`  
- `instrumentalness`  
- `liveness`  
- `valence`  
- `tempo`  
- `time_signature`  
- `genre`  
- `artist_primary`  
""")