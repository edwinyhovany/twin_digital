# src/sampling/sample.py
"""Sampling utilities.

Provides a simple function to obtain a random sample from a DataFrame.
"""

import pandas as pd

def random_sample(df: pd.DataFrame, n: int = 1000, seed: int = 42) -> pd.DataFrame:
    """Return a random sample of *n* rows from *df*.

    Args:
        df: Input pandas DataFrame.
        n: Number of rows to sample (default 1000).
        seed: Random seed for reproducibility.

    Returns:
        Sampled pandas DataFrame.
    """
    if n <= 0:
        raise ValueError("Sample size 'n' must be positive")
    return df.sample(n=min(n, len(df)), random_state=seed)
