'''imports'''
import pandas as pd
from pathlib import Path

def save_data(df: pd.DataFrame, 
              destino: Path
) -> None:
    '''Salva o df no caminho especificado no formato Excel'''
    destino.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(destino, index=False)
