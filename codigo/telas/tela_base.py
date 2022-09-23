from PySide6.QtWidgets import QWidget

class TelaBase(QWidget):
    """TelaBase.
    Esta classe é a base de todas as telas da aplicação.

    ..Args::
        parent {Aplicacao} -- Classe base da aplicação.

    ..Attributes::
        aplicacao {Aplicacao} -- Classe base da aplicação.
    """
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.aplicacao = parent