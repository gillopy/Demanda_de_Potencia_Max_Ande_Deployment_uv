import pytest
import pandas as pd
from src.data_loader import DataLoader

def test_load_data_success():
    """Verifica que los datos se carguen correctamente."""
    df = DataLoader.load_data('data/demanda2.xlsx')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'Año' in df.columns
    assert 'Enero' in df.columns

def test_load_data_file_not_found():
    """Verifica que se lance una excepción si el archivo no existe."""
    with pytest.raises(FileNotFoundError):
        DataLoader.load_data('data/no_existe.xlsx')

import pytest
import pandas as pd
from src.data_loader import DataLoader

def test_load_data_invalid_columns(tmpdir):
    """Verifica que se lance una excepción si faltan columnas requeridas."""
    # Crear un archivo Excel inválido
    df_invalido = pd.DataFrame({
        'Año': [2021, 2022],
        'Enero': [100, 200]
    })
    invalid_file = tmpdir.join("demanda_invalida.xlsx")
    df_invalido.to_excel(invalid_file, index=False)

    with pytest.raises(KeyError):
        DataLoader.load_data(str(invalid_file))