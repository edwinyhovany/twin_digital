# IMPLEMENTATION_PHASE3.md

# Implementación Técnica – Fase 3
## Segmentación de Pacientes y Modelado Predictivo

Proyecto:
Gemelo Digital Analítico para la Estimación Prospectiva de Pagos en Pacientes con Diabetes Mellitus Tipo 2

---

# Objetivo

Implementar la Fase 3 de la investigación correspondiente a:

- Preparación del dataset para Machine Learning.
- Selección de variables.
- Segmentación de pacientes mediante Clustering.
- Perfilamiento de segmentos.
- Entrenamiento de modelos predictivos.
- Validación temporal.
- Interpretabilidad del modelo.
- Registro de experimentos.
- Persistencia de modelos.

Esta fase NO implementa todavía el Gemelo Digital ni la Simulación de Escenarios.

Su producto final será:

- Dataset segmentado.
- Modelo predictivo validado.
- Métricas de desempeño.
- Modelo serializado.
- Artefactos para ser consumidos por la Fase 4.

---

# Dependencias

Esta fase depende completamente de la salida de la Fase 2.

Se debe utilizar exclusivamente:

data/processed/dataset_analytic.parquet

No reconstruir el dataset durante esta fase.

---

# Arquitectura

                  Dataset Analítico
                          │
                          ▼
                Selección Variables
                          │
                          ▼
                  Escalamiento
                          │
                          ▼
                    Clustering
                          │
                          ▼
              Perfil de Segmentos
                          │
                          ▼
             Dataset Segmentado
                          │
                          ▼
               Entrenamiento ML
                          │
                          ▼
                Validación Temporal
                          │
                          ▼
               Evaluación Modelos
                          │
                          ▼
              Modelo Seleccionado
                          │
                          ▼
                 Persistencia

---

# Arquitectura de carpetas

src/

    clustering/

        __init__.py

        scaler.py

        selector.py

        kmeans.py

        hierarchical.py

        evaluation.py

        profiling.py

    prediction/

        __init__.py

        train.py

        evaluate.py

        metrics.py

        models.py

        validation.py

        explainability.py

        persistence.py

    mlflow/

        tracking.py

        registry.py

models/

reports/

artifacts/

tests/

---

# Dataset de entrada

Utilizar únicamente

dataset_analytic.parquet

Generado en la Fase 2.

No modificarlo.

Crear nuevos datasets derivados.

---

# Variables

Separar explícitamente:

Variables objetivo

Variables predictoras

Variables identificadoras

Variables temporales

Variables categóricas

Variables numéricas

Nunca utilizar identificadores como variables predictoras.

---

# Variable objetivo

Pago observado.

Corresponde al pago asociado al paciente durante el período definido.

Debe documentarse explícitamente el período utilizado (mensual, anual, etc.).

---

# División temporal

Debe respetar exactamente la metodología de la tesis.

Entrenamiento

2022

2023

Validación

2024

2025

No utilizar validación aleatoria.

No utilizar train_test_split.

La validación es exclusivamente temporal.

---

# Selección de Variables

Crear

src/clustering/selector.py

Debe:

Eliminar columnas no utilizadas.

Eliminar identificadores.

Eliminar variables constantes.

Eliminar variables duplicadas.

Documentar las variables utilizadas.

Guardar:

reports/features_used.json

---

# Escalamiento

Crear

src/clustering/scaler.py

Debe utilizar

StandardScaler

Persistir el scaler entrenado.

models/scaler.joblib

No recalcular durante inferencia.

---

# Clustering

Crear

src/clustering/

Implementar inicialmente:

KMeans

Agglomerative Clustering

No implementar DBSCAN salvo que se solicite posteriormente.

---

# Número de clusters

No fijar manualmente.

Evaluar automáticamente

k = 2 ... 10

Calcular

Silhouette Score

Davies-Bouldin

Calinski-Harabasz

Seleccionar el mejor valor.

Guardar:

reports/clustering_metrics.csv

---

# Perfilamiento de clusters

Crear

src/clustering/profiling.py

Generar automáticamente

Cantidad pacientes

Edad promedio

Pago promedio

Consultas

Urgencias

Hospitalizaciones

Medicamentos

Variables relevantes

Exportar

reports/cluster_profile.xlsx

reports/cluster_profile.csv

---

# Dataset Segmentado

Persistir

data/features/dataset_clustered.parquet

Debe contener

dataset original

+

cluster_id

---

# Modelos Predictivos

Crear

src/prediction/models.py

Implementar

Linear Regression

Random Forest

Gradient Boosting

HistGradientBoosting

XGBoost

Todos deben tener la misma interfaz.

---

# Entrenamiento

Crear

src/prediction/train.py

Debe

Entrenar todos los modelos.

Registrar tiempos.

Registrar parámetros.

Guardar modelos temporalmente.

No seleccionar todavía el mejor.

---

# Evaluación

Crear

src/prediction/evaluate.py

Calcular

MAE

RMSE

SMAPE

R²

Generar

comparison_models.csv

---

# Selección del modelo

Seleccionar automáticamente

Menor RMSE

En caso de empate

Menor MAE

Documentar decisión.

Guardar

best_model.json

---

# Interpretabilidad

Crear

src/prediction/explainability.py

Implementar

SHAP

Generar

Feature Importance

SHAP Summary Plot

Dependence Plot

Guardar en

reports/shap/

---

# Persistencia

Guardar

models/

best_model.joblib

scaler.joblib

cluster_model.joblib

features_used.json

Nunca sobrescribir sin versionado.

---

# MLflow

Registrar automáticamente

Dataset

Modelo

Parámetros

Métricas

Tiempo entrenamiento

Versión

Artefactos

No registrar datasets completos.

---

# Logging

Registrar

Inicio entrenamiento

Fin entrenamiento

Modelo

Tiempo

Errores

Métricas

---

# Notebooks

Los notebooks únicamente deben consumir funciones.

Orden esperado

08_FeatureSelection.ipynb

09_Clustering.ipynb

10_ClusterProfiling.ipynb

11_ModelTraining.ipynb

12_ModelEvaluation.ipynb

13_ModelExplainability.ipynb

No escribir lógica de negocio.

---

# Testing

Crear

tests/

test_selector.py

test_scaler.py

test_kmeans.py

test_hierarchical.py

test_metrics.py

test_training.py

test_explainability.py

---

# Docker

Todo debe ejecutarse dentro del contenedor.

No utilizar dependencias instaladas localmente.

Verificar

docker compose up

pytest

JupyterLab

MLflow

---

# Entregables

La Fase 3 se considera terminada cuando existan:

✔ Dataset segmentado

✔ Clusters perfilados

✔ Métricas de clustering

✔ Modelo predictivo seleccionado

✔ Métricas MAE

✔ Métricas RMSE

✔ Métricas SMAPE

✔ SHAP

✔ MLflow actualizado

✔ Modelos serializados

✔ Tests exitosos

✔ Notebooks ejecutables

✔ Reportes exportados

---

# Restricciones

NO implementar todavía

Gemelo Digital

Simulación

Dashboard

Power BI

API REST

Frontend

Estas funcionalidades pertenecen a la Fase 4 y Fase 5.

---

# Objetivo de salida

El resultado final de esta fase deberá ser un conjunto de artefactos reutilizables para la construcción del Gemelo Digital Analítico.

Los únicos componentes que podrán ser consumidos por la Fase 4 serán:

- dataset_clustered.parquet
- best_model.joblib
- scaler.joblib
- cluster_model.joblib
- features_used.json
- cluster_profile.csv
- comparison_models.csv

No generar dependencias adicionales.

Toda la lógica deberá mantenerse desacoplada, modular y reutilizable.