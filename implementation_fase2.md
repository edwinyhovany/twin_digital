# Phase 2 – Data Preparation

The goal is to implement the **Integración de datos**, **Calidad de datos**, **Limpieza**, **Ingeniería de variables**, and **Construcción del dataset analítico** steps described in *context.md*.  We will create supporting modules under `src/` and corresponding notebooks under `notebooks/` that operate on a **sample** of the Parquet files (e.g., first 1 000 rows) so the pipeline can be iterated quickly before running on the full dataset.

## User Review Required
> [!IMPORTANT]  
> Please confirm the proposed folder layout and module names. If you prefer different names or additional steps, let me know before I start.

## Open Questions
> [!WARNING]  
> * **Sample size** – Should we always use the first 1 000 rows, or would you like a random sample?  
> * **Target parquet files** – The plan uses `COSTOS_PAGOS_DIABETES_2022.parquet` as a representative file.  Do you want to include additional years in the sample?  
> * **Feature engineering** – Any specific transformations (e.g., log‑scaling, binning) you already have in mind?

## Proposed Changes
---
### src/
- **[NEW] src/quality/__init__.py** – package init. 
- **[NEW] src/quality/data_quality.py** – functions `check_missing_and_duplicates(df)` returning a dict of issues.
- **[NEW] src/cleaning/__init__.py**
- **[NEW] src/cleaning/clean_data.py** – functions for type casting, outlier removal, and basic imputation.
- **[NEW] src/feature_engineering/__init__.py**
- **[NEW] src/feature_engineering/engineer.py** – functions to create derived columns (e.g., `age_group`, `payment_per_day`).
- **[NEW] src/dataset/__init__.py**
- **[NEW] src/dataset/build.py** – `build_analytic_dataset(sample_df)` that chains the above steps and returns a ready‑to‑train dataframe.
---
### notebooks/
- **[NEW] notebooks/01_DataIntegration.ipynb** – loads a sample parquet, shows schema, and saves a temporary merged parquet in `data/interim/`.
- **[MODIFY] notebooks/02_DataQuality.ipynb** – already created (uses `src.quality`).
- **[NEW] notebooks/03_DataCleaning.ipynb** – demonstrates `src.cleaning.clean_data` on the sample.
- **[NEW] notebooks/04_FeatureEngineering.ipynb** – demonstrates `src.feature_engineering.engineer`.
- **[NEW] notebooks/05_BuildDataset.ipynb** – uses `src.dataset.build` to produce the analytic dataset and stores it in `data/processed/`.
---
### data/
- Add placeholder `.gitkeep` files in `data/interim/` and `data/processed/` (already present via `.gitkeep` files if needed).
---
### tests/
- **[NEW] tests/test_quality.py** – unit test for missing/duplicate detection.
- **[NEW] tests/test_cleaning.py** – basic test for cleaning functions.
- **[NEW] tests/test_feature_engineering.py** – test engineered columns.
- **[NEW] tests/test_build.py** – integration test of the full pipeline on a tiny dataframe.
---
## Verification Plan
### Automated Tests
- Run `pytest -q` inside the `app` container to ensure all new modules work on the sample data.
### Manual Verification
- Open each notebook in JupyterLab (port 8888) and execute all cells.  Verify that a small parquet file (≈ 1 KB) appears in `data/processed/`.
- Confirm that the resulting dataframe contains the engineered features and has no missing values.

Once these steps pass, we will be ready to move to **Phase 3** (clustering & predictive modeling).
