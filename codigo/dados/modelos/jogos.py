from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from codigo.dados.banco import secao
from codigo.dados.banco import Banco
from codigo.dados.modelos.base import Base
from codigo.dados.modelos.precos import Precos


class Jogos(Banco, Base):
    """Modelo Jogos.
    Esta classe cria o modelo Jogos.

    ..Attributes::
        descricao {str} -- String que aceita nulo com tamanho máximo 250.
        id {int} -- Inteiro unico que identifica o registro.
        link {str} -- String que não aceita nulo com tamanho máximo 50.
        nome {str} -- String que não aceita nulo com tamanho máximo 50.
        preco {int} -- Inteiro que identifica o preço atual do jogo.
        precos {list[Precos]} -- Uma lista de preços.

    ..Methods::
        buscar_link -- faz uma busca no banco de dados respeitando um link.
        menor_preco -- faz uma busca do menor preço do jogo.
        preco_atual -- faz uma busca do preço atual do jogo.
        deletar -- apaga o registro do jogo e os preços vinculados a ele do banco.
    """
    __tablename__ = 'jogos'

    descricao = Column(String(250))
    id = Column(Integer, primary_key=True)
    link = Column(String(50), nullable=False)
    nome = Column(String(50), nullable=False)
    preco = Column(Integer)

    precos = relationship("Precos", back_populates="jogo")

    def buscar_link(self, link):
        """faz uma busca no banco de dados respeitando um link.

        ..Arguments::
            link{str} -- O link a ser buscado

        ..Returns::
            [Jogos] -- Uma objeto do tipo da Jogos.
        """
        return secao.query(type(self)).filter_by(link=link).first()

    def menor_preco(self) -> Precos:
        """faz uma busca do menor preço do jogo.

        ..Returns::
            [Precos] -- Uma objeto do tipo da Precos.
        """
        return Precos().buscar_menor_preco(self)

    def preco_atual(self) -> Precos:
        """faz uma busca do preço atual do jogo.

        ..Returns::
            [Precos] -- Uma objeto do tipo da Precos.
        """
        return Precos().buscar_preco_atual(self)

    def deletar(self) -> None:
        """apaga o registro do jogo e os preços vinculados a ele do banco.
        """
        for preco in self.precos:
            secao.delete(preco)
            secao.commit()

        secao.delete(self)
        secao.commit()

    def __repr__(self):
        return f'<Jogo(id={self.id}, nome={self.nome})>'
