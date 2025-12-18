# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<p align="center">
  <img src="Images/banner_image.jpg" alt="Spotify Banner" width="800"/>
</p>

<h1 align="center">Spotify Tracks Unsupervised Clustering</h1>

## Project Members

| Name        | Responsibility|
|---------------|-------------|
| Robert      | Data Architect |
| Ali     | Project Manager |
| Tom     | Data Analyst |
| Project Type: |	Hackathon 2 |
| Date:         |	December 2025 |

## Project Bookmarks:

-   [README](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/README.md)
-   [Project board](https://github.com/users/ali-khurshid/projects/8)
-   [Data](https://github.com/ali-khurshid/Spotify_Tracks/tree/main/data)
-   [Data Cleaning Jupyter Notebook](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/01_data_cleaning.ipynb)
-   [Feature engineering Jupyter Notebook](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/03_feature_engineering.ipynb)
-   [Hypothesis 1 Features vs popularity](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/04_H1_features_vs_popularity.ipynb)
-   [Hypothesis 2 Explicit vs Non-explicit Tracks](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/05_H2_explicit_vs_nonexplicity.ipynb)
-   [Hypothesis 3 Acousticness vs Energy and popularity](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/06_H3_acousticness_vs_energy_and_popularity.ipynb)
-   [Streamlit](https://spotify-clustering-project.streamlit.app/)
-   [Conclusion and Discussion](#conclusion-and-discussion)

## Table of Contents:

-   [Project Overview](#project-overview)
-   [Dataset Content](#dataset-content)
-   [Business Requirements](#business-requirements)
-   [Hypothesis Testing and Validation](#hypothesis-testing-and-validation)
-   [Rationale to map business requirements](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations)
-   [Analysis Techniques Used](#analysis-techniques-used)
-   [Project Plan](#project-plan)
-   [Project Board](#project-board)
-   [Ethical Consideration](#ethical-considerations)
-   [Streamlit App](#streamlit-app)
-   [Deployment to the Streamlit Cloud](#deployment-to-streamlit-cloud)
-   [Unfixed Bugs and Challenges Faced](#unfixed-bugs-and-challenges-faced)
-   [Development Roadmap](#development-roadmap)
-   [Main data Analysis Libraries](#main-data-analysis-libraries)
-   [Findings](#findings)
-   [Conclusion and Discussion](#conclusion-and-discussion)
-   [Credits](#credits)
-   [Acknowledgements](#acknowledgements)

## Project Overview

This project analyzes a dataset of Spotify tracks, including audio features, artist information, and song popularity. Through exploratory data analysis (EDA), it explores distributions and relationships between features, uncovering patterns that influence track popularity.

The project also performs correlation analysis to examine how attributes like danceability, energy, and tempo relate to popularity, and applies clustering techniques to group tracks with similar audio characteristics. These insights can inform playlist curation and music recommendation strategies.

---

## Dataset Content

The [Spotify Track Records](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset/data) downloaded from kaggle contains dataset of Spotify songs with different genres and their audio features.
The dataset columns can be split into two categories metadata and audio features:

-   **Metadata:**

    -   `track_id` - The Spotify ID for the track
    -   `artists` - the name(s) of the performer(s)
    -   `album_name` The album name in which the track appears
    -   `track_name` - the name of the track
    -   `popularity` - a rating from 0 to 100 which indicates trak popularity
    -   `duration_ms` - song length in milliseconds
    -   `explicit` - boolean representing whether the track has explicit lyrics
    -   `genre` - song category from spotify (e.g. pop)

-   **Audio Features:**

    -   `danceability` - Danceability describes how suitable a track is for dancing
    -   `energy` - Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity
    -   `key` - The key the track is in
    -   `loudness` - The overall loudness of a track in decibels (dB)
    -   `mode` - major or minor
    -   `speechiness` - Speechiness detects the presence of spoken words in a track.
    -   `acousticness` - A measure from 0.0 to 1.0 of whether the track is acoustic
    -   `instrumentalness` - Predicts whether a track contains no vocals.
    -   `liveness` - Detects the presence of an audience in the recording
    -   `valence` - A measure from 0.0 to 1.0 describing the musical positiveness
    -   `tempo` - The overall estimated tempo of a track in beats per minute (BPM)
    -   `time_signature` - An estimated time signature

---

## Business Requirements

-   Predict the popularity of a song based on its audio features. Which features in songs (e.g. dancability or energy) lead to songs being more popular. Can we predict what songs will get lots of streams and make lots of money
-   Set up the infrastructure to make a recommendation engine. Can similar songs be categorised based on their audio features and so could we use this to recommend songs to users based on their listening history.

---

## Hypothesis Testing and Validation

**Hypothesis 1:** Tracks with higher danceability and energy have significantly higher popularity scores than tracks with lower values.

-   Correlation analysis to see if there is a correlation between dancability and popularity

**Hypothesis 2:** Explicit tracks are, on average, more popular than non-explicit tracks.

-   Correlation analysis between explicit tracks (those that contain explicit language) and popularity to see if there is a correation between the explicit nature of the song and popularity.

**Hypothesis 3:** Tracks with high acousticness have lower energy and lower popularity.

-   Calculate the correlation between acousticness and energy and acousticness and popularity

**Hypothesis 4:** Tracks cluster into distinct musical profiles that differ significantly in popularity.

-   Perform an unsupervised clustering task on the audio features to group track into distinct groups.
-   Use a statistical test (depending on normality) to see if the popularity of the different clusters differs significantly.

## The rationale to map the business requirements to the data visualisations

| Analysis Step                      | Visualization                                                         | Purpose / Insight                                                                                                |
| ---------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Feature Exploration**            | Histograms / Boxplots of audio features                               | Understand distributions, ranges, and detect outliers in key features like energy, danceability, tempo, loudness |
| **Categorical Feature Comparison** | Bar charts / Count plots (Explicit vs Non-explicit, Key distribution) | Compare counts across categories to understand feature prevalence and patterns                                   |
| **Feature Relationships**          | Scatter plots (Danceability vs Popularity, Energy vs Popularity)      | Identify relationships between audio features and track popularity; visually assess correlations                 |
| **Correlation Analysis**           | Correlation heatmap                                                   | Show which numerical features are strongly correlated; guide further analysis and feature selection              |
| **Clustering Validation**          | Elbow plot & Silhouette scores                                        | Evaluate different k values to select the most appropriate number of clusters for grouping tracks                |
| **Cluster Formation**              | Clustering plots (scatter with clusters / PCA)                        | Visualize clusters of tracks based on audio features; understand how tracks group together                       |
| **Cluster Popularity Analysis**    | Boxplots & Violin plots of Popularity by Cluster                      | Compare popularity distributions across clusters; identify clusters with higher listener engagement              |
| **Cluster Feature Profiles**       | Radar / Spider plots of audio features by cluster                     | Highlight characteristic audio feature patterns of each cluster; identify unique cluster signatures              |
| **Track Recommendations**          | Recommendation table (based on radar plot clusters)                   | Suggest tracks similar to a given profile; enable playlist curation and personalized recommendations             |


## Project Plan

| Day       |                                Plan                                 |                                              Responsibility                                               |
| :-------- | :-----------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------: |
| Tuesday   | Load data, clean, hypothesis creation, EDA, and feature engineering | Perform EDA and understand relationships. Generate 4 hypotheses including an unsupervised clustering task |
| Wednesday |       Classification model creation and hyperparameter tuning       |                    Cluster creation, visualisation and data preparation for the model                     |
| Thursday  |                     Dashboard and documentation                     |                      Make an engaging streamlit dashboard and update readme sections                      |
| Friday    |                            Presentation                             |                                               Presentation                                                |

## Project Board

Our project board on Day 2 of the hackathon.

![alt text](Images/project_board.jpg)

## Ethical Considerations

-   **Data anonymization –** No personally identifiable information is used.

- **Fairness and bias –** The model and analyses do not discriminate against any genre, artist, or demographic. Any clustering or recommendations are based purely on audio features and popularity metrics.

- **Transparency –** All datasets, methods, and algorithms are clearly documented, and code is shared for reproducibility.

- **Responsible recommendations –** Suggested tracks are intended for exploration and playlist curation; the system does not influence user behavior beyond general recommendations.

- **Data source acknowledgement –** The dataset is publicly available on Kaggle and used in compliance with its terms of use.

---

## Streamlit App

We created a **Streamlit app** to allow interactive exploration and analysis of Spotify tracks.

The app is a **multi-page dashboard** consisting of:

- **Homepage** – Introduction to the dataset, project goals, and key features.

- **EDA (Exploratory Data Analysis)** – Visualizations of feature distributions, correlations, and relationships with popularity.

- **Analysis ➡️ Hypothesis Testing** – Statistical analysis to test relationships between track features and popularity.

- **Clustering** – Clustering tracks based on audio features with PCA and cluster visualizations. This also includes personalized track recommendations based on cluster profiles and audio features.

## Deployment to Streamlit Cloud

- **“Experience the interactive Streamlit app here:”** https://spotify-clustering-project.streamlit.app/

---

## Unfixed Bugs

No unfixed bugs to report.

## Development Roadmap

<u>**Challenges Faced**</u>

- The original dataset was very messy with lots of duplicate track names. This posed a challenge during the data cleaning process.

- The column names were difficult to interpret which caused feature engineering to become a bit tough.

- Our k-value changed from 6 to 5 with no reason. We are still unable to explain why it happened.

<u>**What Next**</u>

We plan to apply our cluster model on unseen Spotify data to evaluate its performance in practice. This will help us:

- Identify any tweaks or improvements needed in clustering or recommendation logic.

- Ensure the model is generalizable beyond the original dataset.

- Test whether the recommendations remain relevant and accurate for new tracks.

---

## Main Data Analysis Libraries

The following libraries were used in my project.

-   `helpers`
-   `joblib`
-   `matplotlib` . `pyplot`
-   `numpy`
-   `os`
-   `Pandas`
-   `pyexpat`
-   `plotly` . `express`
-   `plotly` . `graph_objects`
-   `scipy` . `stats`
-   `seaborn`
-   `sklearn` . `pipeline`
-   `sklearn` . `compose`
-   `sklearn` . `preprocessing`
-   `sklearn` . `impute`
-   `sklearn` . `linear_model`
-   `sklearn` . `metrics`
-   `imblearn` . `oversampling`
-   `sklearn` . `model_selection`
-   `sklearn` . `ensemble`
-   `streamlit`

---

## Findings

- It was possible to group the cleaned and processed data into clusters.

- ChatGPT was able to identify the musical characteristics of each cluster.

- We used the 5 clusters to identify the top 5 songs from our dataset.

## Conclusion and Discussion

| Hypothesis | Analysis / Method | Conclusion |
|------------|-----------------|------------|
| **H1:** Tracks with higher danceability and energy have significantly higher popularity scores than tracks with lower values. | Correlation analysis between `danceability` & `popularity` and `energy` & `popularity` | Hypothesis 1 is partially supported. Danceability shows a weak but statistically significant positive relationship with popularity, suggesting it contributes marginally to a track’s success. Energy, however, demonstrates a negligible correlation with popularity despite statistical significance, indicating it is not a meaningful standalone predictor. Overall, audio features alone are insufficient to explain popularity, highlighting the influence of external factors such as marketing, artist reputation, and listener trends. Given the weak effect sizes, popularity is likely driven by a combination of musical, social, and industry factors rather than individual audio characteristics. |
| **H2:** Explicit tracks are, on average, more popular than non-explicit tracks. | Correlation analysis between `explicit` tracks and `popularity` |Hypothesis 2 is supported. A Mann–Whitney U test indicates a statistically significant difference in popularity between explicit and non-explicit tracks (p < 0.001). This suggests that explicit content is associated with different popularity outcomes, potentially reflecting listener preferences or broader cultural trends. However, effect size analysis would be required to assess the practical importance of this difference.  |
| **H3:** Tracks with high acousticness have lower energy and lower popularity. | Correlation between `acousticness` & `energy` and `acousticness` & `popularity` | Hypothesis 3 is partially supported. Acousticness shows a strong and statistically significant negative relationship with energy (ρ = −0.715, p < 0.001), confirming that more acoustic tracks tend to be lower in energy. However, the relationship between acousticness and popularity is negligible (ρ = 0.020), indicating that acoustic qualities alone do not meaningfully influence a track’s popularity. This suggests that musical style affects track characteristics but does not directly translate into commercial success.  |
| **H4:** Tracks cluster into distinct musical profiles that differ significantly in popularity. | Unsupervised clustering on audio features to form clusters; statistical test (e.g., ANOVA or Kruskal-Wallis) to compare popularity across clusters | Hypothesis 4 is supported. The clustering analysis identified distinct musical profiles based on audio features, and these clusters exhibit statistically significant differences in track popularity. The Kruskal–Wallis test confirmed that popularity distributions vary across clusters, while post-hoc Mann–Whitney U tests showed that several clusters differ significantly from others even after controlling for multiple comparisons. Visual evidence from boxplots, violin plots, and cluster summaries further reinforces that popularity is systematically associated with specific combinations of musical characteristics. This indicates that track popularity is not randomly distributed, but is meaningfully influenced by underlying audio feature profiles. |


## Credits

### Content

-   ChatGPT was used to help create code and debug errors.
-   Microsoft Co-Pilot was used to help with code suggestions for the clustering.
-   Dataset downloaded from [Kaggle](https://www.kaggle.com/datasets).

### Media

-   Streamlit banner image taken from [Freepik](https://www.freepik.com)
-   Code Institute Logo taken from Code Institute website.
-   For presention purposes [Website Mockup Generator](https://websitemockupgenerator.com/) used.

## Acknowledgements

-   Special thanks to our facilitator Emma Lamont, Our Tutors Neil, Michael, Mark and Spencer for making this course easy to learn.
-   I'd like to thank all my colleagues for being a fun group to work with.

