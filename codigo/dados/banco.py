
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from codigo.dados.conexao import busca_conexao

engine = create_engine(busca_conexao())
Session = sessionmaker(bind=engine)
secao = Session()

Banco = declarative_base()