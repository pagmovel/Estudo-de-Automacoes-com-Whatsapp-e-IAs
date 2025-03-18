from sqlalchemy import Column, BigInteger, BOOLEAN, TIMESTAMP, VARCHAR, TEXT, text, ForeignKey
from models.db import Base
from models.crud import CRUDMixin

class TblBbBotRegistros1Sentenca(Base, CRUDMixin):
    __tablename__ = 'tbl_bb_bot_registros_primeira_sentenca'
    __table_args__ = {'schema': 'bancos'}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    bot_controle_id = Column(BigInteger, ForeignKey("bancos.tbl_bb_bots_controle.id", ondelete="CASCADE"), nullable=False)
    npj = Column(VARCHAR, nullable=False)
    cadastro = Column(VARCHAR, nullable=True)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'))
    updated_at = Column(TIMESTAMP)
    tags_analise_riscos = Column(TEXT, nullable=True)
    cod_tarefa = Column(BigInteger, nullable=True)
    nome_evento = Column(VARCHAR, nullable=True)
    tag_tarefa = Column(TEXT, nullable=True)
    tag_pasta = Column(TEXT, nullable=True)
    pasta_id = Column(BigInteger, nullable=True)
