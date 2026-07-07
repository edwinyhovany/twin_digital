# src/profiling/profiling.py
"""Data profiling utilities.
Provides functions to generate basic descriptive statistics for a pandas DataFrame.
These are lightweight and do not require heavy profiling libraries.
"""

import pandas as pd

def basic_profile(df: pd.DataFrame) -> dict:
    """Return a dictionary with basic profiling information.

    The dictionary includes:
    - row_count
    - column_count
    - column_names
    - dtypes (as a dict)
    - missing_counts (per column)
    - unique_counts (per column)
    - descriptive_stats (result of df.describe(include='all').to_dict())
    """
    profile = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "column_names": list(df.columns),
        "dtypes": {col: str(df[col].dtype) for col in df.columns},
        "missing_counts": df.isnull().sum().to_dict(),
        "unique_counts": df.nunique().to_dict(),
        "descriptive_stats": df.describe(include='all').to_dict(),
    }
    return profile
