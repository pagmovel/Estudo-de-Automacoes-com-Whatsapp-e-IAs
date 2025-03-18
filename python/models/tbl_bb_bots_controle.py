from sqlalchemy import Column, BIGINT, BOOLEAN, TIMESTAMP, VARCHAR
from models.db import Base
from models.crud import CRUDMixin

class TblBbBotsControle(Base, CRUDMixin):
    __tablename__ = 'tbl_bb_bots_controle'
    __table_args__ = {'schema': 'bancos'}

    id = Column(BIGINT, primary_key=True, nullable=False)
    nome_bot = Column(VARCHAR, nullable=False)
    robo_ativo = Column(BOOLEAN, nullable=False)
    iniciado_em = Column(TIMESTAMP)
    encerrado_em = Column(TIMESTAMP)
    apresentou_erro = Column(BOOLEAN, nullable=False)
    iniciar = Column(BOOLEAN)
    user_login = Column(VARCHAR)
    ordem_servico = Column(BIGINT, nullable=False)
