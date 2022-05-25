import sys

from PySide6.QtWidgets import QApplication

from codigo.aplicacao import Aplicacao

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacao()
    sys.exit(app.exec())
