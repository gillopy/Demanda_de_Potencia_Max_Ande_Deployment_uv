import pytest
import pandas as pd
from src.data_analyzer import DataAnalyzer
from src.data_loader import DataLoader

@pytest.fixture
def sample_data():
    """Proporciona datos de ejemplo para las pruebas."""
    return DataLoader.load_data('data/demanda2.xlsx')

def test_data_analyzer_initialization(sample_data):
    """Verifica que el analizador se inicialice correctamente."""
    analyzer = DataAnalyzer(sample_data)
    assert analyzer.df_melted is not None
    assert analyzer.annual_stats is not None

def test_data_analyzer_melted_format(sample_data):
    """Verifica el formato correcto de los datos derretidos."""
    analyzer = DataAnalyzer(sample_data)
    assert 'Año' in analyzer.df_melted.columns
    assert 'Mes' in analyzer.df_melted.columns
    assert 'KWh' in analyzer.df_melted.columns

def test_data_analyzer_annual_stats(sample_data):
    """Verifica que las estadísticas anuales se calculen correctamente."""
    analyzer = DataAnalyzer(sample_data)
    assert isinstance(analyzer.annual_stats, dict)
    assert all(isinstance(k, int) for k in analyzer.annual_stats.keys())
    assert all(isinstance(v, float) for v in analyzer.annual_stats.values())

def test_data_analyzer_empty_data():
    """Verifica el manejo de un DataFrame vacío."""
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError) as exc_info:
        DataAnalyzer(empty_df)
    assert str(exc_info.value) == "El DataFrame no puede estar vacío."