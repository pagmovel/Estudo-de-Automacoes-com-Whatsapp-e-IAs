# db.py

import os
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(BASE_DIR, 'config.json')

with open(config_path, 'r') as f:
    config = json.load(f)

def get_engine():
    """
    Lê config["ambiente"] (ex.: 'dev', 'prod') e monta a conexão com base nisso.
    """
    ambiente = config.get("ambiente", "dev")  # Pega "ambiente" ou usa 'dev' como padrão
    db_params = config['database'].get(ambiente)
    
    if not db_params:
        raise ValueError(f"Ambiente '{ambiente}' não encontrado em config['database'].")
    
    if db_params['database'].lower() == 'pgsql':
        connection_string = (
            f"postgresql://{db_params['user']}:{db_params['password']}"
            f"@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
        )
    else:
        # Fallback se não for pgsql
        connection_string = 'sqlite:///meu_banco.db'
    
    return create_engine(connection_string, echo=False)

def get_schema():
    """
    Retorna o schema definido no config.json para o ambiente atual.
    """
    ambiente = config.get("ambiente", "dev")
    db_params = config['database'].get(ambiente)
    if not db_params:
        raise ValueError(f"Ambiente '{ambiente}' não encontrado em config['database'].")
    return db_params.get('schema', None)

# Inicializa engine e SessionLocal para uso geral
engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
