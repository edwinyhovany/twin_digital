# src/dataset/build.py
"""Dataset construction utilities.

The `build_analytic_dataset` function orchestrates the full pipeline:
1️⃣ Load raw parquet
2️⃣ Sample (optional)
3️⃣ Clean data
4️⃣ Validate data
5️⃣ Engineer features
6️⃣ Persist the final analytic dataset

It returns the processed pandas DataFrame.
"""

import pathlib
from typing import Optional, Dict, Tuple
import pandas as pd

from src.data_loader.data_loader import load_parquet
from src.sampling.sample import random_sample
from src.cleaning.clean_data import clean_dataframe
from src.validation.validation import (
    validate_numeric_ranges,
    validate_categorical_consistency,
)
from src.feature_engineering.engineer import engineer_features
from src.persistence.persist import save_dataset

DATA_ROOT = pathlib.Path(__file__).resolve().parents[2] / "data"

def build_analytic_dataset(
    parquet_file: str,
    sample_n: Optional[int] = 1000,
    schema: Optional[dict] = None,
    numeric_ranges: Optional[dict] = None,
    categorical_allowed: Optional[dict] = None,
    outlier_columns: Optional[list] = None,
) -> pd.DataFrame:
    """Execute the full analytic‑dataset pipeline.

    Parameters
    ----------
    parquet_file: str
        Name of the source parquet file located in ``data/``.
    sample_n: int | None, default 1000
        Number of rows to sample; ``None`` uses the full file.
    schema: dict | None
        Optional column‑type mapping for ``clean_dataframe``.
    numeric_ranges: dict | None
        Mapping ``column -> (min, max)`` for numeric validation.
    categorical_allowed: dict | None
        Mapping ``column -> set([...])`` for categorical validation.
    outlier_columns: list | None
        Columns on which to apply IQR outlier removal.

    Returns
    -------
    pandas.DataFrame
        The processed analytic dataset.
    """
    # 1️⃣ Load raw data
    df = load_parquet(parquet_file)

    # 2️⃣ Sample (if requested)
    if sample_n is not None:
        df = random_sample(df, n=sample_n)

    # 3️⃣ Clean data
    df = clean_dataframe(df, schema=schema, outlier_cols=outlier_columns)

    # 4️⃣ Validate data (optional)
    if numeric_ranges:
        numeric_report = validate_numeric_ranges(df, numeric_ranges)
        print("Numeric validation report:", numeric_report)
    if categorical_allowed:
        cat_report = validate_categorical_consistency(df, categorical_allowed)
        print("Categorical validation report:", cat_report)

    # 5️⃣ Engineer features
    df = engineer_features(df)

    # 6️⃣ Persist the analytic dataset
    output_path = DATA_ROOT / "processed" / "analytic_dataset.parquet"
    save_dataset(df, output_path)

    return df
