# Análisis de Demanda de Potencia Máxima ANDE

Este proyecto analiza y visualiza datos de demanda eléctrica de ANDE (Administración Nacional de Electricidad), permitiendo identificar patrones en el consumo de energía a lo largo del tiempo.

## Descripción

El sistema procesa datos históricos de demanda eléctrica en Paraguay, organizados por mes y año, para generar visualizaciones que facilitan el análisis de tendencias y comportamientos estacionales. La herramienta está especialmente diseñada para analizar los patrones de consumo eléctrico, destacando los períodos de mayor y menor demanda.

## Características

- Carga de datos desde archivos Excel con estructura predefinida
- Procesamiento y transformación de datos para su análisis
- Generación de visualizaciones por año con:
  - Líneas de tendencia mensual
  - Marcadores para equinoccios (marzo y septiembre)
  - Promedio anual de consumo
  - Comparativa con años anteriores

## Requisitos

- Python 3.8+
- Pandas
- Matplotlib
- Seaborn
- Pytest (para ejecutar pruebas)
- uv (gestor de dependencias)

## Instalación

1. Clone el repositorio:
```bash
git clone https://github.com/gillopy/demanda_de_potencia_max_ande_deployment_uv.git
cd gillopy-demanda_de_potencia_max_ande_deployment_uv
```

2. Instale las dependencias usando uv:
```bash
uv pip install -e .
```

## Uso

### Ejecución del programa principal

```bash
python src/main.py
```

Esto cargará los datos desde `data/demanda2.xlsx`, los procesará y generará una visualización que se guardará como `grafico_demandaactual.png`.

### Ejecución de pruebas

```bash
pytest
```

## Estructura del proyecto

```
gillopy-demanda_de_potencia_max_ande_deployment_uv/
├── README.md
├── main.py                # Punto de entrada alternativo
├── pyproject.toml         # Configuración del proyecto
├── uv.lock                # Archivo de bloqueo de dependencias
├── .python-version        # Versión de Python requerida
├── data/                  # Datos de entrada
│   └── demanda2.xlsx      # Datos de demanda eléctrica
├── src/                   # Código fuente
│   ├── data_analyzer.py   # Clase para análisis de datos
│   ├── data_loader.py     # Clase para carga de datos
│   ├── data_visualizer.py # Clase para visualización
│   └── main.py            # Punto de entrada principal
└── tests/                 # Pruebas unitarias
    ├── test_data_analyzer.py
    ├── test_data_loader.py
    └── test_data_visualizer.py
```

## Componentes principales

### DataLoader

Responsable de cargar los datos desde un archivo Excel, asegurándose de que contenga las columnas necesarias (año y meses).

### DataAnalyzer

Procesa los datos cargados, realizando transformaciones y cálculos estadísticos para facilitar su visualización y análisis.

### DataVisualizer

Genera visualizaciones a partir de los datos procesados, con múltiples características para resaltar patrones y comportamientos en la demanda eléctrica.

## Formato de datos

El archivo Excel de entrada debe contener las siguientes columnas:
- Año
- Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviembre, Diciembre

Cada fila representa un año, y cada celda contiene el valor de demanda en Megavatios (MW).

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

## Autor

Gillopy

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue o pull request para sugerencias o mejoras.
