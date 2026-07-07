# src/data_loader/data_loader.py
"""Data loading utilities for the Twin Digital project.

Provides functions to load individual Parquet files, automatically discover and
concatenate all yearly cost files, and load auxiliary patient datasets.
"""

import pathlib
import re
from typing import List
import pandas as pd

# Root path for the ``data`` directory (two levels up from this file)
DATA_ROOT = pathlib.Path(__file__).resolve().parents[2] / "data"

def _list_parquet_files(pattern: str) -> List[pathlib.Path]:
    """Return a list of parquet files in ``DATA_ROOT`` matching *pattern*.
    The pattern is a simple glob (e.g. ``COSTOS_PAGOS_DIABETES_*.parquet``).
    """
    return sorted(DATA_ROOT.glob(pattern))

def load_parquet(filename: str, columns: List[str] | None = None) -> pd.DataFrame:
    """Load a single Parquet file located in the project's ``data`` folder.

    Parameters
    ----------
    filename: str
        Name of the parquet file (e.g. ``"COSTOS_PAGOS_DIABETES_2022.parquet"``).
    columns: list | None
        Optional list of columns to read.
    """
    file_path = DATA_ROOT / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Parquet file not found: {file_path}")
    return pd.read_parquet(file_path, columns=columns, engine="pyarrow")

def load_all_years(columns: List[str] | None = None) -> pd.DataFrame:
    """Automatically discover all ``COSTOS_PAGOS_DIABETES_*.parquet`` files,
    load them and concatenate into a single DataFrame.

    A ``year`` column is added (extracted from the filename) so the origin of
    each row is retained.
    """
    pattern = "COSTOS_PAGOS_DIABETES_*.parquet"
    files = _list_parquet_files(pattern)
    if not files:
        raise FileNotFoundError("No cost parquet files found in the data folder.")

    dfs = []
    for f in files:
        # Extract the year from the filename using a regex
        match = re.search(r"_(\d{4})\.parquet$", f.name)
        year = int(match.group(1)) if match else None
        df = pd.read_parquet(f, columns=columns, engine="pyarrow")
        if year is not None:
            df = df.copy()
            df["year"] = year
        dfs.append(df)
    # Concatenate vertically, keeping all columns (outer join semantics)
    return pd.concat(dfs, ignore_index=True, sort=False)

def load_patients(version: str = "raw") -> pd.DataFrame:
    """Load the patients dataset.

    ``version`` can be ``"raw"`` (default) which loads ``Pacientes_Con_Diabetes.parquet``
    or ``"clean"`` which loads ``Pacientes_Con_Diabetes_Limpia.parquet``.
    """
    filename = (
        "Pacientes_Con_Diabetes.parquet"
        if version == "raw"
        else "Pacientes_Con_Diabetes_Limpia.parquet"
    )
    return load_parquet(filename)

def load_ecosystem() -> pd.DataFrame:
    """Load the ecosystem patient dataset.
    """
    return load_parquet("Pacientes_Con_Diabetes_en_Ecosistema_Bienestar.parquet")

def merge_sources(
    on: str | List[str] = "patient_id",
    how: str = "left",
) -> pd.DataFrame:
    """Merge the yearly cost data with patient and ecosystem information.

    The function loads all cost years, the patient table (raw version) and the
    ecosystem table, then merges them using ``pd.merge`` on the columns provided
    in *on*. If the column does not exist in one of the dataframes the merge will
    fall back to a concatenation on the index.
    """
    costs = load_all_years()
    patients = load_patients()
    ecosystem = load_ecosystem()

    # Determine common columns for merging
    common_cols = set(costs.columns) & set(patients.columns) & set(ecosystem.columns)
    if isinstance(on, list):
        merge_keys = [k for k in on if k in common_cols]
    else:
        merge_keys = [on] if on in common_cols else []

    if merge_keys:
        merged = pd.merge(costs, patients, on=merge_keys, how=how)
        merged = pd.merge(merged, ecosystem, on=merge_keys, how=how)
    else:
        # No common key – concatenate side‑by‑side (axis=1) preserving row order
        merged = pd.concat([costs.reset_index(drop=True),
                            patients.reset_index(drop=True),
                            ecosystem.reset_index(drop=True)],
                           axis=1)
    return merged
