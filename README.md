# Proyecto de Tesis

## 🏥 Gemelo Digital Analítico para la Estimación Prospectiva de Pagos en Pacientes con Diabetes Mellitus Tipo 2

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Jupyter](https://img.shields.io/badge/JupyterLab-Lab-orange)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E)
![XGBoost](https://img.shields.io/badge/XGBoost-Regression-green)
![Plotly](https://img.shields.io/badge/Plotly-Dashboard-3F4F75)
![Arquitectura](https://img.shields.io/badge/Arquitectura-Analytical_Digital_Twin-blueviolet)
![Estado](https://img.shields.io/badge/Estado-En_Desarrollo-yellow)
![Licencia](https://img.shields.io/badge/Licencia-Académico-lightgrey)
---

# Objetivo General

Desarrollar un Gemelo Digital Analítico basado en segmentación de pacientes, Machine Learning y simulación de escenarios que permita estimar prospectivamente los pagos asociados a pacientes con Diabetes Mellitus Tipo 2 utilizando información histórica de EPS colombianas.

El proyecto NO busca construir un gemelo digital fisiológico.

El proyecto corresponde a un Gemelo Digital Analítico Poblacional.

---
# Fases Proyecto

		
Fase 1	- Investigación y diseño metodológico

Fase 2	- Preparación del dataset

Fase 3	- Clustering y Machine Learning

Fase 4	- Gemelo Digital

Fase 5	- Simulación

Fase 6	- Dashboard

Fase 7	- Validación


## Estado actual

Actualmente el proyecto se encuentra entre la Fase 2 y Fase 3 de la metodología.

## Fase 1

✔ Terminada

- Revisión bibliográfica
- Estado del arte
- Objetivos
- Justificación
- Marco metodológico

---

## Fase 2

En desarrollo.

Objetivos:

- Integración de datos
- Calidad de datos
- Limpieza
- Ingeniería de variables
- Construcción de dataset analítico

---

## Fase 3

En desarrollo.

Objetivos:

- Segmentación mediante clustering
- Entrenamiento de modelos predictivos
- Validación temporal
- Selección del mejor modelo

---

# Arquitectura General

```
Datos Históricos
        │
        ▼
Preparación de Datos
        │
        ▼
Feature Engineering
        │
        ▼
Clustering
        │
        ▼
Machine Learning
        │
        ▼
Gemelo Digital Analítico
        │
        ▼
Simulación de Escenarios
        │
        ▼
Dashboard
```

---
# Arquitectura del código

```
diabetes-digital-twin/

│

├── data/

│   ├── raw/

│   ├── interim/

│   ├── processed/

│   ├── features/

│   └── simulation/

│

├── notebooks/

│   ├── 01_EDA.ipynb

│   ├── 02_DataQuality.ipynb

│   ├── 03_FeatureEngineering.ipynb

│   ├── 04_Clustering.ipynb

│   ├── 05_ModelTraining.ipynb

│   ├── 06_ModelEvaluation.ipynb

│   ├── 07_DigitalTwin.ipynb

│   ├── 08_Simulation.ipynb

│   └── 09_Dashboard.ipynb

│

├── src/

│

│   ├── preprocessing/

│

│   ├── feature_engineering/

│

│   ├── clustering/

│

│   ├── prediction/

│

│   ├── simulation/

│

│   ├── visualization/

│

│   └── utils/

│

├── models/

│

├── reports/

│

├── mlruns/

│

├── tests/

│

├── dashboard/

│

├── docs/

│

└── docker/
```

---

# Datos disponibles

Actualmente existen los siguientes archivos.

```
COSTOS_PAGOS_DIABETES_2022.parquet

COSTOS_PAGOS_DIABETES_2023.parquet

COSTOS_PAGOS_DIABETES_2024.parquet

COSTOS_PAGOS_DIABETES_2025.parquet

COSTOS_PAGOS_DIABETES_2026.parquet

Pacientes_Con_Diabetes.parquet

Pacientes_Con_Diabetes_Limpia.parquet

Pacientes_Con_Diabetes_en_Ecosistema_Bienestar.parquet

Diccionario_base_Pagos.xlsx
```

### Peso aproximado:

650 MB

Formato:

Apache Parquet

---

## 🚀 Stack Tecnológico

### Ciencia de Datos

- Python 3.11
- Pandas
- NumPy
- SciPy

### Machine Learning

- Scikit-Learn
- XGBoost
- LightGBM
- SHAP

### Visualización

- Plotly
- Matplotlib
- Power BI

### Persistencia

- Apache Parquet
- PostgreSQL

### Experimentación

- JupyterLab
- MLflow

### Infraestructura

- Docker
- Docker Compose
- GitHub

# Librerías principales

pandas
numpy
pyarrow
scikit-learn
xgboost
lightgbm
matplotlib
plotly
shap
mlflow
joblib
scipy
duckdb
pyyaml
jupyterlab

---


# Git

Todo el código será versionado en GitHub.

Excluyendo:

```
*.parquet

*.csv

mlruns/

data/

outputs/

```

# Machine Learning

Problema: Regresión.

Variable objetivo: Pago observado.

Modelos candidatos:

- Linear Regression

- Random Forest

- Gradient Boosting

- XGBoost

- HistGradientBoosting

Se Evalua con:

- MAE

- RMSE

- SMAPE

Registro de experimentos mediante MLFlow.

---

# Clustering

Se Evalua con:

- KMeans

- Hierarchical Clustering

Se Evalua con:

- Silhouette

- Davies-Bouldin

- Calinski-Harabasz

- Generar perfil de clusters.

---

# Validación

## Entrenamiento

2022

2023

## Validación

2024

2025

2026


---

# Restricciones de Gemelo Digital

NO se construyen simulaciones fisiológicas.

NO utiliza modelos mecanísticos.

El Gemelo Digital será Analítico.

# Alcance de Gemelo Digital

Debe integrar:

Perfil del paciente

↓

Cluster

↓

Modelo Predictivo

↓

Escenario

↓

Pago esperado

---

# Escenarios

- Base

- Mayor seguimiento ambulatorio

- Mayor participación en programas preventivos

- Mayor continuidad farmacológica

- Escenario combinado

- Los escenarios modifican variables de entrada.

- Nunca modificar directamente la predicción.

---

# Dashboard

Inicialmente Plotly.

Posteriormente Power BI.

Debe mostrar:

- Clusters

- Distribución de pagos

- Predicción

- Comparación escenarios

- Indicadores

- KPIs

---

# Principios Tecnicos

Todo el código cumple con estandares de calidad de codificacion y lineamientos tecnicos como :

- Modular

- Tipado

- Documentado

- Reutilizable

- Con logging

- Con manejo de errores

- Sin duplicación

---

### 📦 Instalación
## Instalar Docker
### Windows
```bash
https://www.docker.com/products/docker-desktop/
```
### Linux
```bash
sudo apt update
sudo apt install docker.io docker-compose-plugin
```

### Clonar & Instalar
```bash
git clone https://github.com/usuario/diabetes-digital-twin.git

cd diabetes-digital-twin
```

### Variables de Entorno

.env :
```
PYTHON_ENV=development

POSTGRES_DB=diabetes

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

MLFLOW_TRACKING_URI=http://mlflow:5000

DATA_PATH=/workspace/data

```

### 🐳 Levantar Infraestructura

## Construir contenedores

```
docker-compose build
```

## Levantar contenedores

```
docker-compose up -d
```
## Levantar contenedores

Jupyter disponible en:
```
http://localhost:8888
```
MLflow disponible en:
```
http://localhost:5000
```
---

## 👨‍💻 Authors

**Julie Alejandra Barragan**
- GitHub:  [@juliebarragan-netizen]

**Edwin Yhovany Garzon**
- GitHub: [@edwinyhovany]

**Jeferson Torrado**
- GitHub: [@JefersonTB]
---

## 📧 Contact

For questions or collaboration: edwingarzon@usantoto.edu.co

---
