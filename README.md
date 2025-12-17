# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Project Bookmarks:

-   [README](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/README.md)
-   [Project board](https://github.com/users/ali-khurshid/projects/8)
-   [Data](https://github.com/ali-khurshid/Spotify_Tracks/tree/main/data)
-   [Data Cleaning Jupyter Notebook](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/01_data_cleaning.ipynb)
-   [Feature engineering Jupyter Notebook](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/03_feature_engineering.ipynb)
-   [Hypothesis 1 Features vs popularity](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/04_H1_features_vs_popularity.ipynb)
-   [Hypothesis 2 Explicit vs Non-explicit Tracks](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/05_H2_explicit_vs_nonexplicity.ipynb)
-   [Hypothesis 3 Acousticness vs Energy and popularity](https://github.com/ali-khurshid/Spotify_Tracks/blob/main/notebooks/06_H3_acousticness_vs_energy_and_popularity.ipynb)
-   [Streamlit]()
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
-   [Unfixed Bugs and Challenges Faced](#unfixed-bugs-and-challenges-faced)
-   [Development Roadmap](#development-roadmap)
-   [Main data Analysis Libraries](#main-data-analysis-libraries)
-   [Findings](#findings)
-   [Conclusion and Discussion](#conclusion-and-discussion)
-   [Credits](#credits)
-   [Acknowledgements](#acknowledgements)

## Project Overview

---

## Dataset Content

The [Spotify Track Records](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) downloaded from kaggle contains patient records including demographic information, health indicators, and lifestyle factors. Key features include:

-   **Numerical:**

    -   `age`
    -   `avg_glucose_level`
    -   `bmi`

-   **Categorical:**

    -   `gender`
    -   `hypertension`
    -   `heart_disease`
    -   `ever_married`
    -   `work_type`
    -   `residence_type`
    -   `smoking_status`

-   **Target:**

    -   `stroke` (0 = no stroke, 1 = stroke)

---

## Business Requirements

-   Identify the features most associated with stroke risk.
-   Provide clear visualizations to support ML model creation
-   Ensure the analysis is reproducible and interpretable.
-   Understand imbalanced data impact
-   Check if prediction works for educational purposes or real life application
-   Ensure AI & ML ethical attributes are considered.

---

## Hypothesis Testing and Validation

---

## The rationale to map the business requirements to the data visualisations

## Project Plan

| Day       |                    Plan                     |                                                  Responsibility                                                   |
| :-------- | :-----------------------------------------: | :---------------------------------------------------------------------------------------------------------------: |
| Monday    |          Load data, clean and EDA           |                             Perform EDA and understand relationships. Clean the data                              |
| Tuesday   | Hypothesis creation and Feature Engineering | Based on audio feature distribution charts, create a set of hypothesis and run it past feature engineering tasks. |
| Wednesday |         Cluster and Model creation          |                        Cluster creation, visualisation and data preparation for the model                         |
| Thursday  |     Hyperparameter Tuning and Dashboard     |                                 Using best performance parameters for clustering                                  |
| Friday    |                Presentation                 |                                                   Presentation                                                    |

## Project Board

A snapshot of the project board midway through my capstone project.

---

## Ethical Considerations

-   Data anonymization: No personally identifiable information is used.

---

## Streamlit App

I created a Streamlit app to allow

The app is a multi-paged dashboard consisting of:

## Unfixed Bugs

---

## Development Roadmap

<u>**Challenges Faced**</u>

<u>**What Next**</u>

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

## Conclusion and Discussion

## Credits

### Content

-   ChatGPT helped me rephrase my englih and sentence construction in this document.
-   ChatGPT was used to help create code and debug errors. It alsohelped unblock deployment of my Streamlit app to the cloud, which took several hours to complete.
-   Dataset downloaded from [Kaggle](https://www.kaggle.com/datasets).

### Media

-   Streamlit banner image taken from [Freepik](https://www.freepik.com/)

## Acknowledgements

-   Special thanks to our facilitator Emma Lamont, Our Tutors Neil, Michael and Spencer for making this course easy to learn.
-   I'd like to thank all my colleagues for being a fun group to work with.
    https://www.freepik.com/
