"""Utility functions for data processing."""
import pandas as pd


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
    string_cols = string_cols or []
    date_cols = date_cols or []
    rename_dict = rename_dict or {}
    remove_cols = remove_cols or []

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
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Convert remaining object columns to category dtype
    exclude_cols = set(string_cols + date_cols)
    object_cols = set(df.select_dtypes(include=['object']).columns)

    # Convert object columns to category dtype, excluding specified columns
    for col in object_cols - exclude_cols:
        if col in df.columns:
            df[col] = df[col].astype("category")

    # Remove duplicates and rows with missing values
    df.drop_duplicates(inplace=True)

    # Remove rows with any missing values
    df.dropna(inplace=True)

    return df
