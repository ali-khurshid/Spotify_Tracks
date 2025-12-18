import streamlit as st

#Display banner at top


with st.container():
    st.image("Images/banner_image.jpg", use_container_width=True)
    
    st.markdown(
        """
        <div style='text-align:center; white-space: nowrap; font-size:40px; font-weight:bold; color:black; margin-top:20px;'>
        Spotify Tracks Cluster Analysis Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

st.markdown("""

            **Navigate using the sidebar to explore diffeent sections of this dashboard.**      
         
**Developed by:** AudioBuddy Inc.

**Creators:** Ali Khurshid, Robert Elliott, Tom Burgess
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
            This project aims to:

**1.** Explore correlations between audio features.

**2.** Create hypotheses for analysis.

**3** Use insights for **classification and recommendation purposes.**
            
            """)

st.markdown("""
The spotify tracks dataset includes audio features alongside names of artists and the popularity ratings of their songs.
This project aims to explore how the audio features are correlated to each other and the number of Hypotheses that can be created. 
These are then used for **Classification** purposes.
            """)

st.subheader("Dataset Features")
            
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