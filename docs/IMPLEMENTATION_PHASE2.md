# IMPLEMENTATION_PHASE2.md

# Implementación Técnica – Fase 2
## Gemelo Digital Analítico para la Estimación Prospectiva de Pagos en Pacientes con Diabetes Mellitus Tipo 2

---

# Objetivo

Implementar la Fase 2 de la investigación correspondiente a:

- Integración de datos
- Perfilamiento de datos
- Calidad de datos
- Limpieza
- Validación
- Ingeniería de variables
- Construcción del Dataset Analítico

Esta implementación constituye la base para la Fase 3 (Clustering y Machine Learning), por lo tanto deberá diseñarse siguiendo principios de modularidad, reutilización, reproducibilidad y escalabilidad.

---

# Principios Arquitectónicos

El proyecto debe seguir una arquitectura por capas.

NO colocar lógica de negocio dentro de notebooks.

Los notebooks únicamente deberán:

- importar módulos
- ejecutar procesos
- visualizar resultados
- documentar experimentos

Toda la lógica deberá implementarse dentro de src/.

---

# Flujo General

                Datos Parquet
                       │
                       ▼
              Data Loader
                       │
                       ▼
             Data Profiling
                       │
                       ▼
             Data Quality
                       │
                       ▼
             Data Cleaning
                       │
                       ▼
            Data Validation
                       │
                       ▼
         Feature Engineering
                       │
                       ▼
        Dataset Analítico
                       │
                       ▼
              Persistencia

---

# Arquitectura propuesta

```
project/

│

├── data/

│   ├── raw/

│   ├── interim/

│   ├── processed/

│   ├── features/

│   └── simulation/

│

├── notebooks/

│

├── src/

│

│   ├── config/

│

│   ├── data_loader/

│

│   ├── profiling/

│

│   ├── quality/

│

│   ├── cleaning/

│

│   ├── validation/

│

│   ├── feature_engineering/

│

│   ├── dataset/

│

│   ├── clustering/

│

│   ├── prediction/

│

│   ├── digital_twin/

│

│   ├── simulation/

│

│   ├── dashboard/

│

│   ├── utils/

│

│   └── visualization/

│

├── models/

├── reports/

├── tests/

├── docs/

└── docker/

```

---

# 1 Data Loader

Crear

```
src/data_loader/
```

Responsabilidad:

Leer automáticamente todos los archivos Parquet.

NO utilizar únicamente COSTOS_PAGOS_DIABETES_2022.

Debe detectar automáticamente:

```
COSTOS_PAGOS_DIABETES_20XX.parquet
```

Agregar una columna

```
ANIO
```

Concatenar todos los datasets.

Funciones esperadas

```
load_parquet()

load_all_years()

load_patients()

load_ecosystem()

merge_sources()
```

---

# 2 Muestreo

NO utilizar:

```
head(1000)
```

Utilizar:

```
sample(random_state=42)
```

Preferiblemente:

Muestreo estratificado por año.

Ejemplo

```
300 registros por año
```

Esto evita sesgos temporales.

---

# 3 Configuración

Crear

```
src/config/settings.py
```

Debe centralizar:

```
RANDOM_STATE

TRAIN_YEARS

VALID_YEARS

DATA_RAW

DATA_INTERIM

DATA_PROCESSED

MODEL_PATH

MLFLOW_URI

LOG_LEVEL
```

Ninguna ruta deberá estar escrita directamente en notebooks.

---

# 4 Data Profiling

Crear

```
src/profiling/
```

Responsabilidad

Generar automáticamente:

- cantidad de registros

- cantidad de columnas

- tipos

- cardinalidad

- nulos

- estadísticas

- distribución

- valores únicos

- memoria utilizada

Guardar reporte HTML y JSON.

Notebook

```
02_DataProfiling.ipynb
```

---

# 5 Calidad

Crear

```
src/quality/
```

Evaluar

Duplicados

Nulos

Consistencia

Tipos

Llaves

Integridad

Valores fuera de rango

Generar

```
quality_report.json
```

---

# 6 Limpieza

Crear

```
src/cleaning/
```

Responsabilidades

Conversión de tipos

Imputación

Tratamiento de fechas

Tratamiento de texto

Tratamiento de outliers

Normalización de categorías

No eliminar registros sin registrar la razón.

---

# 7 Validación

Nuevo módulo

```
src/validation/
```

Validar

Integridad

Consistencia

Tipos

Reglas de negocio

Ejemplo

Pago >= 0

Edad > 0

Edad < 120

---

# 8 Ingeniería de Variables

Crear

```
src/feature_engineering/
```

Construir variables derivadas.

Ejemplos

Edad

Grupo de edad

Pago anual

Pago promedio

Número consultas

Número urgencias

Número hospitalizaciones

Continuidad farmacológica

Participación Ecosistema Bienestar

Variables temporales

Variables por segmento

Todas las variables deberán documentarse.

---

# 9 Dataset Analítico

Crear

```
src/dataset/
```

Debe producir

```
dataset_clean.parquet

dataset_features.parquet

dataset_analytic.parquet
```

No producir un único dataset.

---

# 10 Persistencia

Guardar

```
data/interim/

data/features/

data/processed/
```

Nunca sobrescribir datasets originales.

---

# 11 Logging

Crear

```
src/utils/logger.py
```

Todo módulo deberá registrar

Inicio

Fin

Tiempo

Errores

Advertencias

Cantidad registros

---

# 12 Utilidades

Crear

```
src/utils/
```

Ejemplos

paths.py

dates.py

constants.py

helpers.py

---

# 13 MLFlow

Aunque aún no existan modelos.

Registrar

Versiones dataset

Fecha

Experimento

Autor

Parámetros

---

# 14 Notebooks

Los notebooks únicamente deberán consumir funciones.

Nunca implementar lógica compleja.

Orden esperado

01_DataIntegration

02_DataProfiling

03_DataQuality

04_DataCleaning

05_DataValidation

06_FeatureEngineering

07_BuildDataset

---

# 15 Testing

Crear

```
tests/
```

Mínimo

test_loader.py

test_quality.py

test_cleaning.py

test_validation.py

test_features.py

test_dataset.py

---

# 16 Git

Nunca subir

```
data/

mlruns/

outputs/

*.parquet

*.csv

```

Agregar

.gitignore

---

# 17 Docker

Todo debe ejecutarse dentro del contenedor.

No asumir instalaciones locales.

Servicios

JupyterLab

MLFlow

Python 3.11

---

# 18 Entregables

La Fase 2 se considera finalizada cuando existan:

✔ Data Loader funcional

✔ Perfilamiento automático

✔ Reporte de calidad

✔ Limpieza

✔ Validación

✔ Ingeniería de variables

✔ Dataset Analítico

✔ Dataset documentado

✔ Tests

✔ Logging

✔ Docker funcional

✔ MLFlow configurado

✔ Notebooks ejecutables

---

# No implementar todavía

NO desarrollar aún:

Clustering

Machine Learning

Gemelo Digital

Dashboard

Power BI

Simulación

Estos pertenecen a fases posteriores.

---

# Objetivo para la siguiente fase

El resultado final de esta implementación debe ser un único Dataset Analítico completamente limpio y documentado que sirva como entrada para la Fase 3 correspondiente a:

- Segmentación mediante Clustering.
- Entrenamiento y evaluación de modelos predictivos.
- Validación temporal.
- Selección del modelo que será integrado posteriormente al Gemelo Digital Analítico.
