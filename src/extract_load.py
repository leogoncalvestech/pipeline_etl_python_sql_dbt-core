# import
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

# environment variable imports- imports de variaveis de ambiente
load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = F"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

# Função para buscar os dados de uma commodity
def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)  
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]  # 'Close' com C maiúsculo
    dados['simbolo'] = simbolo
    return dados

# Função para buscar os dados de todas as commodities
def buscar_todos_dados_commodities(lista_commodities):
    todos_dados = []
    for simbolo in lista_commodities:
        dados = buscar_dados_commodities(simbolo)  # chamada correta aqui
        todos_dados.append(dados)
    return pd.concat(todos_dados)

def salvar_no_postgres(df , schema='public'):
    df.to_sql('commodities',engine ,if_exists='replace', index=True , index_label='Date', schema=schema)

# Bloco principal
if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    salvar_no_postgres(dados_concatenados, schema='public')

print (dados_concatenados)

#get asset quotes  - pegar a cotação dos ativos

# concatenate assets (1..2..3) -> (1)  concatenar ativos

#salvar no banco de dados
