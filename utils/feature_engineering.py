import pandas as pd

def add_interaction_terms(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds interaction terms between all pairs of numerical features in the DataFrame.
    Args:
        df (pd.DataFrame): Input DataFrame with numerical features.
    Returns:
        pd.DataFrame: DataFrame with added interaction terms.
    """

    if "danceability" in df.columns and "energy" in df.columns:
        df["danceability_energy_index"] = (df["danceability"] * df["energy"]) / 2

    if "acousticness" in df.columns and "instrumentalness" in df.columns:
        df["acoustic_profile"] = (df["acousticness"] * df["instrumentalness"]) / 2

    if "energy" in df.columns and "valence" in df.columns:
        df["mood_index"] = (df["energy"] * df["valence"]) / 2
    
    if "instrumentalness" in df.columns:
        df["vocal_presence"] = 1 - df["instrumentalness"]

    return df