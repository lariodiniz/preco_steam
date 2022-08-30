from codigo.telas.tela_base import TelaBase

class GestorDeTelas:
    """Gestor de Telas.
    Esta classe é responsavel pela gestão das telas da aplicação.

    ..Args::
        index {int} -- é o index utilizado para mostrar a tela
        tela {QFrame} -- tela da aplicação
    ..Attributes::
        index {int} -- é o index utilizado para mostrar a tela
        tela {QFrame} -- tela da aplicação
    """

    def __init__(self, index:int, tela)->None:
        self.index = index
        self.tela=tela
