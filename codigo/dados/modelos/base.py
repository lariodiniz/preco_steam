
from codigo.dados.banco import secao



class Base:
    """Modelo Base.
    Esta classe cria a Base para os modelos.

    ..Methods::
        buscar_filtro -- faz uma busca no banco de dados respeitando um filtro e uma ordem.
        buscar_id -- faz uma busca no banco de dados respeitando um id.
        buscar_todos -- faz uma busca no banco de dados respeitando uma ordem.
        deletar -- apaga um registro do banco.
        salvar -- adiciona ou atualiza um registro do banco.
    """

    def buscar_filtro(self, filtro, ordem = None)->list:
        """faz uma busca no banco de dados respeitando um filtro e uma ordem.
        ..Arguments::
            filtro -- O filtro da busca
            ordem -- A Ordenação da busca
        ..Returns::
            [list] -- Uma lista de registros retornados do banco de dados.
        """
        if ordem:
            return secao.query(type(self)).filter(filtro).order_by(ordem).all()
        return secao.query(type(self)).filter(filtro).all()

    def buscar_id(self, id):
        """faz uma busca no banco de dados respeitando um id.

        ..Arguments::
            id{int} -- O id a ser buscado

        ..Returns::
            [Base] -- Uma objeto do tipo da busca.
        """
        return secao.query(type(self)).filter_by(id=id).first()

    def buscar_todos(self, ordem = None)->list:
        """faz uma busca no banco de dados respeitando uma ordem.
        ..Arguments::
            ordem -- A Ordenação da busca
        ..Returns::
            [list] -- Uma lista de registros retornados do banco de dados.
        """
        if ordem:
            return secao.query(type(self)).order_by(ordem).all()
        return secao.query(type(self)).all()

    def deletar(self) -> None:
        """apaga um registro do banco.
        """
        secao.delete(self)
        secao.commit()

    def salvar(self) -> None:
        """adiciona ou atualiza um registro do banco.
        """
        secao.add(self)
        secao.commit()

