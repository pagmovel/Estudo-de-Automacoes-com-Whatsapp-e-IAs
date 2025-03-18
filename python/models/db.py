import os
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define o caminho absoluto para o config.json
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(BASE_DIR, 'config.json')

# Carrega as configurações do JSON
with open(config_path, 'r') as f:
    config = json.load(f)

# Obtém o ambiente atual do config.json (ex: 'dev' ou 'prod')
ambiente = config.get("ambiente", "dev")  # Default para 'dev' se não estiver definido

# Função para criar engine com base na configuração selecionada
def get_engine(db_key):
    db_params = config['database'][db_key]
    
    if db_params['database'].lower() == 'pgsql':
        connection_string = (
            f"postgresql://{db_params['user']}:{db_params['password']}"
            f"@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
        )
    else:
        connection_string = 'sqlite:///meu_banco.db'
    
    return create_engine(connection_string, echo=False)

# Usa a configuração correta baseada no ambiente
engine = get_engine(ambiente)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
