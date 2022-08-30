from PySide6.QtWidgets import QWidget

class TelaBase(QWidget):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.aplicacao = parent