# CONTEXT.md

# Proyecto de Tesis
## Gemelo Digital Analítico para la Estimación Prospectiva de Pagos en Pacientes con Diabetes Mellitus Tipo 2 en EPS Colombianas

---

# Objetivo General

Desarrollar un Gemelo Digital Analítico basado en segmentación de pacientes, Machine Learning y simulación de escenarios que permita estimar prospectivamente los pagos asociados a pacientes con Diabetes Mellitus Tipo 2 utilizando información histórica de EPS colombianas.

El proyecto NO busca construir un gemelo digital fisiológico.

El proyecto corresponde a un Gemelo Digital Analítico Poblacional.

---

# Estado actual

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

Peso aproximado:

650 MB

Formato:

Apache Parquet

---

# Tecnología

Todo el proyecto será desarrollado en Python 3.11.

Nunca utilizar R.

---

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

# Git

Todo el código será versionado en GitHub.

NO subir:

```
*.parquet

*.csv

mlruns/

data/

outputs/

.ipynb_checkpoints/
```

Utilizar .gitignore.

---

# Docker

Todo debe ejecutarse dentro de Docker.

No asumir instalaciones locales.

Se utilizará Docker Compose.

Servicios:

JupyterLab

MLFlow

MinIO (opcional)

PostgreSQL (si posteriormente se requiere)

---

# Docker Compose esperado

Servicios:

- notebook

- mlflow

- postgres (opcional)

Red interna:

digital-twin-network

Persistencia mediante volumes.

---

# Entorno

Ubuntu 24.04

Python 3.11

Docker

Docker Compose

Git

GitHub

---

# Flujo de trabajo

Siempre seguir el flujo:

```
git pull

crear rama feature

desarrollar

commit

push

pull request
```

Nunca trabajar sobre main.

---

# Machine Learning

Problema:

Regresión.

Variable objetivo:

Pago observado.

Modelos candidatos:

Linear Regression

Random Forest

Gradient Boosting

XGBoost

HistGradientBoosting

Evaluar:

MAE

RMSE

SMAPE

Seleccionar mejor modelo.

Registrar experimentos mediante MLFlow.

---

# Clustering

Evaluar:

KMeans

Hierarchical Clustering

DBSCAN (opcional)

Evaluar con:

Silhouette

Davies-Bouldin

Calinski-Harabasz

Generar perfil de clusters.

---

# Validación

Entrenamiento

2022

2023

Validación

2024

2025

2026 podrá utilizarse para pruebas futuras o escenarios adicionales.

No mezclar entrenamiento con validación.

---

# Gemelo Digital

NO construir simulaciones fisiológicas.

NO utilizar modelos mecanísticos.

El Gemelo Digital será Analítico.

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

Base

Mayor seguimiento ambulatorio

Mayor participación en programas preventivos

Mayor continuidad farmacológica

Escenario combinado

Los escenarios modifican variables de entrada.

Nunca modificar directamente la predicción.

---

# Dashboard

Inicialmente Plotly.

Posteriormente Power BI.

Debe mostrar:

Clusters

Distribución de pagos

Predicción

Comparación escenarios

Indicadores

KPIs

---

# Principios

Todo el código debe ser:

Modular

Tipado

Documentado

Reutilizable

PEP8

Con logging

Con manejo de errores

Sin duplicación

---

# Convención

Todos los notebooks deberán posteriormente convertirse en scripts dentro de src.

Los notebooks solo sirven para experimentación.

La lógica de negocio siempre debe vivir en src/.

---

# Objetivo del agente

Cada vez que se solicite desarrollar una funcionalidad:

1.

Revisar primero la arquitectura.

2.

Mantener separación entre notebooks y src.

3.

No generar código duplicado.

4.

Crear funciones reutilizables.

5.

Documentar con docstrings.

6.

Agregar typing.

7.

Agregar comentarios únicamente cuando aporten valor.

8.

Mantener compatibilidad con Docker.

9.

No asumir rutas absolutas.

10.

Todas las rutas deben obtenerse mediante pathlib.

---

# Prioridad inmediata

Actualmente desarrollar:

✔ Preparación de datos

✔ Calidad

✔ Ingeniería de variables

✔ Clustering

✔ Modelado Predictivo

No comenzar todavía Dashboard ni Simulación avanzada hasta terminar la validación del modelo.

---

Fin del contexto.