# src/cleaning/clean_data.py
"""Data cleaning utilities.

Provides basic cleaning steps that can be applied to a pandas DataFrame:
- Type coercion (using a provided schema)
- Imputation of missing numeric values with median
- Imputation of missing categorical values with mode
- Removal of obvious outliers using IQR filtering
"""

import pandas as pd
import numpy as np

def coerce_types(df: pd.DataFrame, schema: dict) -> pd.DataFrame:
    """Cast columns to the types specified in *schema*.

    *schema* maps column name -> pandas dtype (e.g., "float", "int", "category").
    Columns missing from *schema* are left untouched.
    """
    for col, dtype in schema.items():
        if col in df.columns:
            try:
                df[col] = df[col].astype(dtype)
            except Exception as e:
                raise ValueError(f"Failed to cast column {col} to {dtype}: {e}")
    return df

def impute_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Simple imputation:
    - numeric columns → median
    - object / category columns → mode (most frequent)
    """
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            median = df[col].median()
            df[col].fillna(median, inplace=True)
        else:
            mode = df[col].mode()
            if not mode.empty:
                df[col].fillna(mode.iloc[0], inplace=True)
    return df

def remove_outliers_iqr(df: pd.DataFrame, columns: list | None = None) -> pd.DataFrame:
    """Remove rows that contain outliers based on the IQR method.

    For each numeric column, compute Q1, Q3 and filter rows outside
    ``[Q1 - 1.5*IQR, Q3 + 1.5*IQR]``.
    If *columns* is ``None`` all numeric columns are considered.
    """
    if columns is None:
        columns = [c for c in df.select_dtypes(include=[np.number]).columns]
    mask = pd.Series(True, index=df.index)
    for col in columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        mask &= df[col].between(lower, upper, inclusive="both")
    return df[mask]

def clean_dataframe(df: pd.DataFrame, schema: dict | None = None, outlier_cols: list | None = None) -> pd.DataFrame:
    """Run the full cleaning pipeline.

    Steps:
    1. Optional type coercion using *schema*.
    2. Impute missing values.
    3. Remove outliers.
    """
    if schema:
        df = coerce_types(df, schema)
    df = impute_missing(df)
    df = remove_outliers_iqr(df, outlier_cols)
    return df
