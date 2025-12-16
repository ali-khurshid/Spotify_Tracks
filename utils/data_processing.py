import pandas as pd
from rapidfuzz import process, fuzz


def load_data(file_path: str,
              string_cols: list | None = None,
              date_cols: list | None = None) -> pd.DataFrame:
    """Load data from a CSV file into a pandas DataFrame."""

    string_cols = string_cols or []
    date_cols = date_cols or []

    df = pd.read_csv(file_path)

    for col in string_cols or []:
        if col in df.columns:
            df[col] = df[col].astype("string")

    for col in date_cols or []:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    exclude_cols = set(string_cols + date_cols)
    object_cols = set(df.select_dtypes(include=['object']).columns)

    for col in object_cols - exclude_cols:
        if col in df.columns:
            df[col] = df[col].astype("category")

    return df


def remove_unneeded_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Remove unneeded columns from the DataFrame."""

    return df.drop(columns=columns, errors='ignore')
