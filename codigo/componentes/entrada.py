from PySide6.QtCore import QSize
from PySide6.QtWidgets import QLineEdit

from codigo.utilidades import PadraoDeCores

class Entrada(QLineEdit):
    """Componente Entrada.
    Esta classe cria uma area de entrada padrão do sistema.

    ..Args::
        altura {int} -- altura padrão do botão.
        largura {int} -- largura padrão do botão.
        espacamento {int} -- espacamento padrão do botão.
    """

    def __init__(self, altura: int = 40, largura: int = 100, espacamento: int = 8, *args, **kargs):

        super().__init__(*args, **kargs)

        self.setMinimumSize(QSize(largura,altura))
        self.setMaximumSize(QSize(largura,altura))

        estilo = f"""
        QLineEdit {{
            color:{PadraoDeCores.entrada_texto};
            background-color: {PadraoDeCores.entrada_fundo};
            padding: {espacamento}px;
            border: 2px solid {PadraoDeCores.primaria};
            border-radius: 10px;
        }}
        """

        self.setStyleSheet(estilo)

