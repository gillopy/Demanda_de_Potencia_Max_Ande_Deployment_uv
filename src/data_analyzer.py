import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        if data.empty:
            raise ValueError("El DataFrame no puede estar vacío.")
        self.data = data
        self.df_melted = None
        self.annual_stats = None
        self._process_data()
    
    def _process_data(self):
        """Transforma los datos y calcula estadísticas"""
        orden_meses = [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]
        
        # Reorganizar datos
        self.df_melted = pd.melt(
            self.data,
            id_vars='Año',
            var_name='Mes',
            value_name='KWh'
        )
        
        # Ordenar meses correctamente
        self.df_melted['Mes'] = pd.Categorical(
            self.df_melted['Mes'],
            categories=orden_meses,
            ordered=True
        )
        
        # Calcular estadísticas anuales
        self.annual_stats = self.df_melted.groupby('Año')['KWh'].mean().to_dict()