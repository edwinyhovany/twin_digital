# src/quality/data_quality.py
"""Data quality utilities.
Provides functions to assess missing values and duplicate rows.
"""

import pandas as pd

def check_missing_and_duplicates(df: pd.DataFrame) -> dict:
    """Return a dictionary summarizing missing values and duplicate rows.

    Returns:
        {
            "missing": {column: count, ...},
            "total_missing": int,
            "duplicate_rows": int,
            "duplicate_percentage": float,
        }
    """
    missing = df.isnull().sum()
    total_missing = int(missing.sum())
    duplicate_rows = int(df.duplicated().sum())
    duplicate_percentage = (duplicate_rows / len(df) * 100) if len(df) > 0 else 0.0
    return {
        "missing": missing.to_dict(),
        "total_missing": total_missing,
        "duplicate_rows": duplicate_rows,
        "duplicate_percentage": duplicate_percentage,
    }
