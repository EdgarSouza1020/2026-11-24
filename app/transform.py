'''imports'''
import pandas as pd

def agrupar(df: pd.DataFrame,
            coluna_agrupar: str
) -> pd.DataFrame:
    '''Agrupa o Dataframe'''
    colunas_metricas = [
        "Venda R$",
        "Qtde. Venda"
    ]
    return (
        df.groupby(coluna_agrupar)[colunas_metricas]
        .sum()
        .reset_index()
        .sort_values(by="Venda R$", ascending=False)
    )



def fazer_merge(
    df_left: pd.DataFrame,
    df_right: pd.DataFrame,
    chave_left: str,
    chave_right: str
) -> pd.DataFrame:
    '''Faz o merge entre as tabelas'''
    df_left = df_left.copy()
    df_right = df_right.copy()
    
    df_left[chave_left] = df_left[chave_left].astype(str).str.strip()
    df_right[chave_right] = df_right[chave_right].astype(str).str.strip()
    
    return pd.merge(
        left= df_left,
        right= df_right,
        how="left",
        left_on= chave_left,
        right_on= chave_right
    )
