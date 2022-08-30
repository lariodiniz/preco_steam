from PySide6.QtWidgets import QCheckBox

from codigo.utilidades import PadraoDeCores

class CaixaDeMarcar(QCheckBox):
    """Componente Caixa de Marcar.
    Esta classe cria uma caixa de marcar padrão do sistema.

    ..Args::
        espacamento {int} -- espaçamento .
    """

    def __init__(self, espacamento: int = 8, *args, **kargs):

        super().__init__(*args, **kargs)

        estilo = f"""
        QCheckBox {{
            color:{PadraoDeCores.primaria};
            background-color: {PadraoDeCores.entrada_fundo};
            padding: {espacamento}px;
            border: 2px solid {PadraoDeCores.primaria};
            border-radius: 10px;
        }}
        """
        self.setStyleSheet(estilo)
