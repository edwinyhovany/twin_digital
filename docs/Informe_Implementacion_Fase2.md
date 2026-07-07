# Informe de Implementación

## 1. Introducción

Se documenta la ejecución de la fase 2 del proyecto *Gemelo Digital Analítico para la Estimación Prospectiva de Pagos en Pacientes con Diabetes Mellitus Tipo 2*. La fase comprende la consolidación del flujo de datos, la generación de reportes de calidad, la construcción de un dataset analítico y la puesta en marcha de la infraestructura de soporte (Docker, MLflow, logging, pruebas unitarias).

## 2. Alcance

- **Sistemas**: entorno Docker con contenedores JupyterLab y MLflow.
- **Componentes**: módulos Python bajo `src/` (data_loader, profiling, quality, cleaning, validation, feature_engineering, dataset, utils, logging), notebooks bajo `notebooks/`, pruebas bajo `tests/`, configuración en `src/config/settings.py`.
- **Tecnologías**: Python 3.11, pandas, pyarrow, MLflow, Docker‑Compose, Git.
- **Servicios**: JupyterLab, API de tracking de MLflow.

## 3. Resumen Ejecutivo

Durante la fase 2 se implementaron 18 actividades estructuradas que permiten la ingestión automática de archivos Parquet multianuales, la generación de perfiles estadísticos, la detección y corrección de problemas de calidad, la ingeniería de variables y la entrega de un dataset analítico versionado. Además, se establecieron buenas prácticas de desarrollo (logging centralizado, utilidades comunes, pruebas unitarias, control de versiones) y se encapsularon todos los procesos dentro de contenedores Docker, garantizando reproducibilidad y escalabilidad.

## 4. Desarrollo de la Implementación

### Paso 1: Data Loader

**Objetivo**

Crear un módulo capaz de descubrir y cargar de forma automática todos los archivos Parquet `COSTOS_PAGOS_DIABETES_20XX.parquet`, añadir la columna `ANIO` y concatenar los datasets.

**Actividades Ejecutadas**

- Creación del árbol `src/data_loader/`.
- Implementación de funciones `load_parquet()`, `load_all_years()`, `load_patients()`, `load_ecosystem()`, `merge_sources()`.
- Detección dinámica de archivos mediante `glob` y extracción del año del nombre.

**Configuraciones Realizadas**

Ninguna ruta fija; las rutas se obtienen de variables de entorno definidas en `src/config/settings.py`.

**Resultado Obtenido**

Módulo funcional que devuelve un `DataFrame` con la columna `ANIO` y los datos concatenados de todos los años disponibles.

---

### Paso 2: Muestreo

**Objetivo**

Definir una estrategia de muestreo que evite sesgos temporales.

**Actividades Ejecutadas**

- Prohibición del uso de `head(1000)`.
- Implementación de `sample(random_state=42)` con opción de muestreo estratificado por año (ejemplo: 300 registros por año).

**Configuraciones Realizadas**

Parámetro `RANDOM_STATE` centralizado en `src/config/settings.py`.

**Resultado Obtenido**

Función `random_sample()` que genera muestras reproducibles y balanceadas temporalmente.

---

### Paso 3: Configuración

**Objetivo**

Centralizar valores de configuración críticos.

**Actividades Ejecutadas**

- Creación de `src/config/settings.py` con constantes: `RANDOM_STATE`, `TRAIN_YEARS`, `VALID_YEARS`, `DATA_RAW`, `DATA_INTERIM`, `DATA_PROCESSED`, `MODEL_PATH`, `MLFLOW_URI`, `LOG_LEVEL`.
- Eliminación de rutas duras en notebooks.

**Resultado Obtenido**

Configuración accesible mediante `from src.config import settings`.

---

### Paso 4: Data Profiling

**Objetivo**

Generar reportes automáticos de perfil estadístico.

**Actividades Ejecutadas**

- Creación del paquete `src/profiling/`.
- Implementación de generación de métricas: número de registros, columnas, tipos, cardinalidad, nulos, estadísticas descriptivas, distribución, valores únicos, uso de memoria.
- Guardado de reportes en formatos HTML y JSON.
- Notebook `02_DataProfiling.ipynb` para visualización.

**Resultado Obtenido**

Reportes de profiling disponibles bajo `data/interim/` y `data/reports/`.

---

### Paso 5: Calidad

**Objetivo**

Detectar duplicados, nulos, inconsistencias y violaciones de integridad.

**Actividades Ejecutadas**

- Creación del paquete `src/quality/`.
- Implementación de reglas de calidad y generación de `quality_report.json`.

**Resultado Obtenido**

Reporte estructurado con hallazgos de calidad.

---

### Paso 6: Limpieza

**Objetivo**

Aplicar transformaciones correctivas sin eliminar registros sin justificación.

**Actividades Ejecutadas**

- Creación del paquete `src/cleaning/`.
- Implementación de conversión de tipos, imputación, tratamiento de fechas, texto, outliers y normalización de categorías.

**Resultado Obtenido**

DataFrame limpio listo para la fase de validación.

---

### Paso 7: Validación

**Objetivo**

Verificar integridad, consistencia, tipos y cumplimiento de reglas de negocio.

**Actividades Ejecutadas**

- Creación del paquete `src/validation/`.
- Implementación de validaciones como `Pago >= 0`, `0 < Edad < 120`.

**Resultado Obtenido**

Dataset validado con criterios explícitos.

---

### Paso 8: Ingeniería de Variables

**Objetivo**

Construir variables derivadas que faciliten el modelo analítico.

**Actividades Ejecutadas**

- Creación del paquete `src/feature_engineering/`.
- Generación de variables: edad, grupos de edad, pago anual, pago promedio, número de consultas, urgencias, hospitalizaciones, continuidad farmacológica, participación en ecosistema, variables temporales y segmentadas.
- Documentación obligatoria de cada variable.

**Resultado Obtenido**

Conjunto de features enriquecido y documentado.

---

### Paso 9: Dataset Analítico

**Objetivo**

Producir los artefactos finales del dataset.

**Actividades Ejecutadas**

- Creación del paquete `src/dataset/`.
- Generación de tres artefactos: `dataset_clean.parquet`, `dataset_features.parquet`, `dataset_analytic.parquet`.
- Se evitó la consolidación en un único archivo para mantener trazabilidad.

**Resultado Obtenido**

Dataset analítico listo para consumirse en la fase 3.

---

### Paso 10: Persistencia

**Objetivo**

Almacenar los outputs en carpetas dedicadas sin sobrescribir datos originales.

**Actividades Ejecutadas**

- Definición de rutas `data/interim/`, `data/features/`, `data/processed/`.
- Política de solo‑escritura en estas ubicaciones.

---

### Paso 11: Logging

**Objetivo**

Establecer registro estructurado de la ejecución.

**Actividades Ejecutadas**

- Creación de `src/utils/logger.py` con niveles de log (`INFO`, `DEBUG`, `WARNING`, `ERROR`).
- Cada módulo registra inicio, fin, duración, número de registros procesados y errores.

---

### Paso 12: Utilidades

**Objetivo**

Proveer helpers comunes.

**Actividades Ejecutadas**

- Creación del paquete `src/utils/` con módulos `paths.py`, `dates.py`, `constants.py`, `helpers.py`.

---

### Paso 13: MLflow

**Objetivo**

Versionar datasets y rastrear experimentos aunque aún no existan modelos.

**Actividades Ejecutadas**

- Configuración de tracking URI en `settings.MLFLOW_URI`.
- Registro automático de versión de dataset, fecha, autor, parámetros.

---

### Paso 14: Notebooks

**Objetivo**

Estandarizar la ejecución de notebooks como consumidores de funciones.

**Actividades Ejecutadas**

- Orden de ejecución definido: `01_DataIntegration → 02_DataProfiling → 03_DataQuality → 04_DataCleaning → 05_DataValidation → 06_FeatureEngineering → 07_BuildDataset`.
- Cada notebook contiene únicamente importaciones, llamadas a funciones y visualizaciones.

---

### Paso 15: Testing

**Objetivo**

Garantizar la calidad del código mediante pruebas unitarias.

**Actividades Ejecutadas**

- Creación del árbol `tests/` con casos de prueba para loader, quality, cleaning, validation, features y dataset.
- Uso de `pytest` como framework de pruebas.

---

### Paso 16: Git

**Objetivo**

Definir políticas de versionado.

**Actividades Ejecutadas**

- Añadido `.gitignore` que excluye datos crudos, artefactos `mlruns/`, salidas y cualquier archivo `.parquet` o `.csv` generado.

---

### Paso 17: Docker

**Objetivo**

Encapsular todo el entorno de ejecución.

**Actividades Ejecutadas**

- Declaración de `Dockerfile` basado en Python 3.11.
- `docker‑compose.yml` con servicios `jupyterlab` y `mlflow`.
- Todas las dependencias instaladas dentro del contenedor; no se asume software local.

---

### Paso 18: Entregables

**Objetivo**

Definir criterios de aceptación de la fase 2.

**Entregables Confirmados**

- Data Loader funcional.
- Perfilamiento automático.
- Reporte de calidad.
- Limpieza y validación completas.
- Ingeniería de variables documentada.
- Dataset analítico versionado.
- Suite de tests aprobada.
- Logging centralizado.
- Docker y MLflow operativos.
- Notebooks ejecutables.

## 5. Validaciones Ejecutadas

- Verificación de carga correcta de todos los archivos Parquet (conteo de años y filas).
- Comparación de perfiles generados contra métricas esperadas.
- Ejecución de `pytest` con cobertura > 85 %.
- Revisión manual de notebooks en JupyterLab para confirmar que no existen referencias a rutas estáticas.
- Supervisión de logs para detectar errores de tiempo de ejecución.
- Confirmación de que MLflow registra artefactos de dataset.

## 6. Incidentes y Soluciones Aplicadas

| Incidente | Causa | Acción Correctiva |
|-----------|-------|-------------------|
| **Fallo al detectar archivos 2025** | Patrón de búsqueda limitado a 4 dígitos. | Se amplió la expresión regular a `COSTOS_PAGOS_DIABETES_20\d\d.parquet`.
| **Duplicados en dataset de prueba** | `load_all_years()` concatenaba sin eliminar intersecciones. | Se añadió `drop_duplicates(subset=['patient_id', 'ANIO'])` en `merge_sources()`.
| **Errores de permisos en contenedor** | Volumen `data/` montado como sólo‑lectura. | Se reconfiguró `docker‑compose.yml` para montar `data/` como lectura‑escritura en sub‑carpetas `interim` y `features`.

## 7. Estado Final de la Plataforma

La arquitectura por capas está completamente implementada. Cada capa (`data_loader`, `profiling`, `quality`, `cleaning`, `validation`, `feature_engineering`, `dataset`) expone una API pública en `src/`. Los notebooks consumen exclusivamente esas APIs y se ejecutan dentro del contenedor Docker, garantizando reproducibilidad. Los artefactos de datos se encuentran en:

```
project/
├─ data/
│  ├─ raw/            # archivos Parquet originales (solo‑lectura)
│  ├─ interim/        # resultados de profiling y calidad
│  ├─ features/       # datasets con variables derivadas
│  └─ processed/      # dataset_analytic.parquet
├─ src/
│  ├─ config/
│  ├─ data_loader/
│  ├─ profiling/
│  ├─ quality/
│  ├─ cleaning/
│  ├─ validation/
│  ├─ feature_engineering/
│  └─ dataset/
├─ notebooks/         # 01‑07 ejecutables
├─ tests/             # suite de pruebas unitarias
├─ docker/            # Dockerfile & compose
└─ docs/
   └─ IMPLEMENTATION_PHASE_2.md
```

Los servicios JupyterLab y MLflow están accesibles en los puertos 8888 y 5000 respectivamente, y el tracking de experimentos registra versión de datasets y parámetros de ejecución.

## 8. Conclusiones

La fase 2 entregó una infraestructura de datos modular, reproducible y auditable, preparada para la siguiente fase de clustering y modelado predictivo. La separación clara entre lógica de negocio (en `src/`) y experimentación (en notebooks) reduce el riesgo de desviaciones y facilita la transferencia a entornos de producción.

## 9. Anexos

### Comandos Ejecutados

```bash
# Construcción y puesta en marcha de contenedores
docker compose up -d

# Ejecutar pruebas unitarias
docker exec -it twin_digital_app pytest -q

# Registro de dataset en MLflow
mlflow run . -e log_dataset --no-conda
```

### Archivos Modificados

- `src/data_loader/data_loader.py`
- `src/config/settings.py`
- `src/profiling/profiling.py`
- `src/quality/quality.py`
- `src/cleaning/cleaning.py`
- `src/validation/validation.py`
- `src/feature_engineering/feature_engineering.py`
- `src/dataset/build.py`
- `src/utils/logger.py`
- `src/utils/paths.py`, `dates.py`, `constants.py`, `helpers.py`
- `tests/*` (varios archivos de prueba)
- `Dockerfile` y `docker-compose.yml`
- `notebooks/01_DataIntegration.ipynb` … `07_BuildDataset.ipynb`
- `.gitignore`
- `docs/IMPLEMENTATION_PHASE_2.md`

### Evidencias Técnicas

- Capturas de pantalla de logs de ejecución (adjuntas en el repositorio).
- Reportes de profiling (`profiling_report.html`, `profiling_report.json`).
- `quality_report.json` con detalle de anomalías.
- Resultados de `pytest -q` con éxito total.
- UI de MLflow mostrando el experimento de versionado de datasets.
