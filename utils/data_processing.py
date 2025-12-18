"""Utility functions for data processing."""
import pandas as pd


def clean_track_name(name: str) -> str:
    """
    Clean track name by removing extraneous information such as text in brackets
    and dash-based suffixes.
    Args:
        name (str): Original track name.
    Returns:
        str: Cleaned track name.
    """

    # Handle missing values
    if pd.isna(name):
        return name

    # Ensure name is a string
    name = str(name)

    # Remove text in brackets
    for sep in [" (", " ["]:
        # Check if the separator is in the name
        if sep in name:
            # Take part before the separator
            name = name.split(sep, 1)[0]

    # Remove dash-based suffixes ONLY if space-dash-space or space-dash
    if " - " in name:
        # Take part before the first " - "
        name = name.split(" - ", 1)[0]

    # Remove trailing spaces
    return name.strip()


def load_data(file_path: str,
              string_cols: list | None = None,
              date_cols: list | None = None,
              rename_dict: dict | None = None,
              remove_cols: list | None = None) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.
    Args:
        file_path (str): Path to the CSV file.
        string_cols (list | None): List of columns to convert to string dtype.
        date_cols (list | None): List of columns to convert to datetime.
        rename_dict (dict | None): Dictionary for renaming columns.
        remove_cols (list | None): List of columns to remove.
    Returns:
        pd.DataFrame: Processed DataFrame.
    """

    # Set default values for optional parameters
    string_cols = string_cols or []  # list of string columns
    date_cols = date_cols or []  # list of date columns
    rename_dict = rename_dict or {}  # dictionary for renaming columns
    remove_cols = remove_cols or []  # list of columns to remove

    # Load the CSV file
    df = pd.read_csv(file_path)

    # Remove specified columns
    if remove_cols:
        df = df.drop(columns=remove_cols, errors='ignore')

    # Rename columns if a rename dictionary is provided
    if rename_dict:
        df = df.rename(columns=rename_dict)

    # Process string columns
    for col in string_cols or []:
        if col in df.columns:
            df[col] = df[col].astype("string")
            df[col] = df[col].str.lower()

    # Process date columns
    for col in date_cols or []:
        if col in df.columns:
            # Convert to datetime, coerce errors to NaT
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Convert remaining object columns to category dtype
    exclude_cols = set(string_cols + date_cols)
    object_cols = set(df.select_dtypes(include=['object']).columns)

    # Convert object columns to category dtype, excluding specified columns
    for col in object_cols - exclude_cols:
        if col in df.columns:
            df[col] = df[col].astype("category")

    # Clean track names if the column exists
    if 'name' in df.columns:
        df['name'] = df['name'].apply(clean_track_name)
        df["name"] = (
            df["name"]
            .str.lower()  # Convert to lowercase
            .str.strip()  # Remove leading/trailing whitespace
        )

    if 'artist_name' in df.columns:
        df['artist_name'] = df['artist_name'].str.lower().str.strip()

    df["artist_primary"] = (
        df["artists"].astype(str)
        .str.split(";", n=1)  # Split at the first semicolon
        .str[0]  # Take the first part as the primary artist
        .str.lower()  # Convert to lowercase
        .str.strip()  # Remove leading/trailing whitespace
    )

    df = (
        df.sort_values("popularity", ascending=False).drop_duplicates(
                subset=["name", "artist_primary"],
                keep="first"
            )  # Keep the most popular track version
        )  # Sort by popularity and remove duplicates based on track name and primary artist

    # Remove duplicates and rows with missing values
    df.drop_duplicates(inplace=True)

    # Remove rows with any missing values
    df.dropna(inplace=True)

    return df
