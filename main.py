'''Imports'''
from dotenv import load_dotenv
import os
from app import config
from app import extract
from app import transform
from app import load

load_dotenv()


def main():
    '''function principal'''
    # df = extract.load_data(config.INPUT_DIR / "2026.xlsx")
    # print(df.columns)
    
    # df_agrupado = transform.agrupar(df, "Bandeira")
    
    # print(df_agrupado.head(10))
    
    df_idade = extract.load_data(config.INPUT_DIR / "idade.xlsx")
    df_sexo = extract.load_data(config.INPUT_DIR / "sexo.xlsx")
    
    print(df_idade.columns)
    print(df_sexo.columns)

    
    df_merge = transform.mergiar(
        df_idade,
        df_sexo,
        "nome",
        "nome"
    )
    
    print(df_merge)

if __name__ == "__main__":
    main()
