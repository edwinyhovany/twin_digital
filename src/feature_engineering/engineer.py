# src/feature_engineering/engineer.py
"""Feature engineering utilities.

This module provides simple example engineered features that can be expanded later.
"""

import pandas as pd

def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """Create an "age_group" categorical column based on "age".
    
    Bins: <30, 30-50, >50. Adjust as needed.
    """
    if "age" not in df.columns:
        return df
    bins = [0, 30, 50, 150]
    labels = ["<30", "30-50", ">50"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)
    return df

def add_payment_per_day(df: pd.DataFrame) -> pd.DataFrame:
    """Create a derived feature "payment_per_day" if "total_payment" and "days_in_period" exist.
    """
    if {"total_payment", "days_in_period"}.issubset(df.columns):
        df["payment_per_day"] = df["total_payment"] / df["days_in_period"]
    return df

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all default feature engineering steps.
    """
    df = add_age_group(df)
    df = add_payment_per_day(df)
    return df
