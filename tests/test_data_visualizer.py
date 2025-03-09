import pytest
import pandas as pd
import matplotlib.pyplot as plt
from src.data_visualizer import DataVisualizer
from src.data_analyzer import DataAnalyzer
from src.data_loader import DataLoader

@pytest.fixture
def sample_analyzer():
    """Proporciona un analizador con datos de ejemplo."""
    df = DataLoader.load_data('data/demanda2.xlsx')
    return DataAnalyzer(df)

def test_data_visualizer_initialization(sample_analyzer):
    """Verifica que el visualizador se inicialice correctamente."""
    visualizer = DataVisualizer(sample_analyzer)
    assert visualizer.analyzer == sample_analyzer

def test_data_visualizer_plot(sample_analyzer):
    """Verifica que el gráfico se genere sin errores."""
    visualizer = DataVisualizer(sample_analyzer)
    visualizer.plot()
    plt.close('all')  # Cierra todas las figuras para liberar memoria

def test_data_visualizer_save_plot(sample_analyzer, tmpdir):
    """Verifica que el gráfico se guarde correctamente."""
    visualizer = DataVisualizer(sample_analyzer)
    output_path = tmpdir.join("test_plot.png")
    visualizer.save_plot(filename=output_path)
    assert output_path.exists()

def test_data_visualizer_invalid_data():
    """Verifica que el visualizador maneje datos inválidos."""
    df_invalido = pd.DataFrame()
    with pytest.raises(ValueError):
        analyzer = DataAnalyzer(df_invalido)
        visualizer = DataVisualizer(analyzer)
        visualizer.plot()