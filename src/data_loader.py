import pandas as pd

class DataLoader:
    @staticmethod
    def load_data(file_path='data/demanda2.xlsx'):
        """Carga y devuelve los datos relevantes del Excel"""
        columnas_meses = [
            'Año', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]
        
        df = pd.read_excel(file_path)
        return df[columnas_meses]