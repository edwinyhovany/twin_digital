# src/validation/validation.py
"""Data validation utilities.
Provides functions to validate numeric ranges and categorical consistency.
"""

import pandas as pd
import numpy as np

def validate_numeric_ranges(df: pd.DataFrame, ranges: dict) -> dict:
    """Check that numeric columns fall within specified *ranges*.

    *ranges* is a dict ``column -> (min, max)``.
    Returns a dict ``column -> {'out_of_range': int, 'total': int}``.
    """
    results = {}
    for col, (min_val, max_val) in ranges.items():
        if col not in df.columns:
            continue
        if not pd.api.types.is_numeric_dtype(df[col]):
            continue
        out_of_range = (~df[col].between(min_val, max_val)).sum()
        results[col] = {"out_of_range": int(out_of_range), "total": int(len(df))}
    return results

def validate_categorical_consistency(df: pd.DataFrame, allowed_values: dict) -> dict:
    """Validate that categorical columns contain only allowed values.

    *allowed_values* is a dict ``column -> set([...])``.
    Returns a dict ``column -> {'invalid': int, 'total': int}``.
    """
    results = {}
    for col, allowed in allowed_values.items():
        if col not in df.columns:
            continue
        invalid = (~df[col].isin(allowed)).sum()
        results[col] = {"invalid": int(invalid), "total": int(len(df))}
    return results
