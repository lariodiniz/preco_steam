import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

os.environ[
    'QT_FONT_DPI'
] = '96'   # FIX Problem for High DPI and Scale above 100%


class Aplicacao(QMainWindow):
    def __init__(self, show: bool = True):
        """Função de Inicialização da aplicação"""

        # inicializa a classe pai
        super().__init__()

        # define pastas do sistema
        self.__definePastas()

        # define o título da aplicação
        title = self.__defineTitulo()
        self.setWindowTitle(title)

        # define o icone da aplicação
        appIcon = QIcon(self.busca_imagem(self.pasta_icones, 'logo.png'))
        self.setWindowIcon(appIcon)

        # mostra a aplicação na tela
        if show:
            self.show()

    def busca_imagem(self, pasta: str, imagem: str) -> str:
        """retorna o caminho correto da imagem informada que esta no diretorio."""
        return os.path.normpath(os.path.join(pasta, imagem))

    def __definePastas(self):
        """cria os atributos `pasta_raiz`, `pasta_imgs` e `pasta_icones` na classe."""
        pasta_main = os.path.abspath(os.getcwd())
        self.pasta_raiz = os.path.join(pasta_main, 'codigo')
        self.pasta_imgs = os.path.join(self.pasta_raiz, 'imgs')
        self.pasta_icones = os.path.join(self.pasta_imgs, 'icons')

    def __defineTitulo(self):
        return 'Preço Steam'
