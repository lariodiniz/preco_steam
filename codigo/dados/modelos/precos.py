from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from codigo.dados.banco import secao
from codigo.dados.banco import Banco
from codigo.dados.modelos.base import Base

class Precos(Banco, Base):
    """Modelo Precos.
    Esta classe cria o modelo Precos.

    ..Attributes::
        data {DateTime} -- Data que o registro foi salvo.
        id {int} -- Inteiro unico que identifica o registro.
        jogo {Jogos} -- objeto Jogos que é relacionado a esse preço.
        jogo_id {int} -- Inteiro que identifica o jogo que esse preço pertence.
        valor {int} -- Inteiro que identifica o preço atual do jogo.

    ..Methods::
        buscar_link -- faz uma busca no banco de dados respeitando um link.
        menor_preco -- faz uma busca do menor preço do jogo.
        preco_atual -- faz uma busca do preço atual do jogo.
        deletar -- apaga o registro do jogo e os preços vinculados a ele do banco.
    """

    __tablename__ = 'precos'

    data = Column(DateTime, nullable=False)
    id = Column(Integer, primary_key=True)
    jogo = relationship("Jogos", back_populates="precos")
    jogo_id = Column(Integer, ForeignKey('jogos.id'), nullable=False)
    valor = Column(Integer)

    def buscar_menor_preco(self, jogo):
        """faz uma busca do menor preço de um jogo.

        ..Arguments::
            jogo{Jogos} -- Objeto do tipo Jogos

        ..Returns::
            [Precos] -- Uma objeto do tipo da Precos.
        """
        model = type(self)
        return secao.query(model).filter(model.jogo==jogo)\
        .order_by(model.valor).first()

    def buscar_preco_atual(self, jogo):
        """faz uma busca do preço atual de um jogo.

        ..Arguments::
            jogo{Jogos} -- Objeto do tipo Jogos

        ..Returns::
            [Precos] -- Uma objeto do tipo da Precos.
        """
        model = type(self)
        return secao.query(model).filter(model.jogo==jogo)\
        .order_by(model.data.desc()).first()

    def buscar_precos_do_jogo(self, jogo, ordem):
        """faz uma busca de todos os preços de um jogo.

        ..Arguments::
            jogo{Jogos} -- Objeto do tipo Jogos

        ..Returns::
            [list[Precos]] -- Uma lista de objetos do tipo Precos.
        """
        model = type(self)
        return secao.query(model).filter(model.jogo==jogo)\
        .order_by(ordem).all()

    def __repr__(self):
        return f'<Preco(jogo={self.jogo.nome}, valor={self.valor})>'