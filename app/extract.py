'''imports'''
import pandas as pd


def load_data(path: Path) -> pd.DataFrame:
    '''Carrega um arquivo .xlsx no path especificado'''
    return pd.read_excel(path)
