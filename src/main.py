from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from data_visualizer import DataVisualizer

if __name__ == "__main__":
    # Carga de datos
    df = DataLoader.load_data()
    
    # Procesamiento y análisis
    analyzer = DataAnalyzer(df)
    
    # Visualización
    visualizer = DataVisualizer(analyzer)
    visualizer.plot()
    visualizer.save_plot()