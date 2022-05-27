import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
)

from codigo.utilidades.cria_layouts.caixa_horizontal import (
    cria_layout_caixa_horizontal,
)
from codigo.utilidades.cria_layouts.caixa_vertical import (
    cria_layout_caixa_vertical,
)
from codigo.utilidades.cria_layouts.moldura import cria_layout_moldura

os.environ[
    'QT_FONT_DPI'
] = '96'   # FIX Problem for High DPI and Scale above 100%


class Aplicacao(QMainWindow):
    """Janela Principal.
    Esta classe é responsavel pela janela principal da aplicação.

    ..Args::
        show {bool} -- serve para mostrar a janela na inicialização da classe.

    ..Methods::
        busca_imagem -- Retorna o caminho correto da imagem informada que esta no diretorio.

    ..Attributes::
        area_principal {QFrame} -- Frame da area principal.
        barra_inferior {QFrame} -- Frame da barra do inferior da area principal.
        barra_inferior_label_direita {QLabel} -- Label direito da barra_inferior.
        barra_inferior_label_esquerda {QLabel} -- Label esquerdo da barra_inferior.
        barra_topo {QFrame} -- Frame da barra do topo da area principal.
        barra_topo_label_esquerdo {QLabel} -- Label esquedo da barra_topo.
        barra_topo_label_direito {QLabel} -- Label direito da barra_topo.
        janelas {QStackedWidget} -- Area das janelas da aplicação.
        layout_principal {QFrame} -- Frame da janela inteira.
        menu_esquerdo {QFrame} -- Frame do menu da esquerda.
        pasta_icones {str} -- string contento o caminho dos icones.
        pasta_imgs {str} -- string contento o caminho da pasta de imagens.
        pasta_raiz {str} -- string contento o caminho da pasta da aplicação.
        versao {str} -- string contento a versão do sistema.
    """

    def __init__(self, show: bool = True):
        """Função de Inicialização da aplicação."""
        # inicializa a classe pai.
        super().__init__()

        # define pastas do sistema.
        self.__definePastas()

        # define a versão
        self.__defineVersao()

        # define o título da aplicação.
        title = self.__defineTitulo()
        self.setWindowTitle(title)

        # define o icone da aplicação.
        appIcon = QIcon(self.busca_imagem(self.pasta_icones, 'logo.png'))
        self.setWindowIcon(appIcon)

        # define tamanho inicial de tela
        self.__defineLayout()

        # mostra a aplicação na tela.
        if show:
            self.show()

    def busca_imagem(self, pasta: str, imagem: str) -> str:
        """Retorna o caminho correto da imagem informada que esta no diretorio.

        ..Arguments::
            pasta {str} -- o diretório onde a imagem esta
            imagem {str} -- o nome da imagem

        ..Returns::
            [str] -- o diretório da imagem
        """
        return os.path.normpath(os.path.join(pasta, imagem))

    def __defineAreaPrincipal(self) -> None:
        """Define o Layout da Area Principal.

        ..Returns::
                None
        """
        self.area_principal = cria_layout_moldura()
        self.area_principal.setStyleSheet('background-color: #EEEDDE')

        area_principal_layout = cria_layout_caixa_vertical(self.area_principal)

        self.barra_topo = cria_layout_moldura(
            altura_minima=30, altura_maxima=30
        )
        self.barra_topo.setStyleSheet(
            'background-color: #116530;color: #FFFFFF'
        )

        layout_barra_topo = cria_layout_caixa_horizontal(
            self.barra_topo, 10, 0, 10, 0
        )

        self.barra_topo_label_esquerdo = QLabel(
            'Gerencie os preços dos jogos que você mais deseja!'
        )

        espacador_barra_topo = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.barra_topo_label_direito = QLabel('PAGINA INICIAL')
        self.barra_topo_label_direito.setStyleSheet("font: 700 9pt 'Segoe UI'")

        layout_barra_topo.addWidget(self.barra_topo_label_esquerdo)
        layout_barra_topo.addItem(espacador_barra_topo)
        layout_barra_topo.addWidget(self.barra_topo_label_direito)

        self.janelas = QStackedWidget()
        self.janelas.setStyleSheet('font-size:12pt; color: #f8f8f2')
        # self.ui_pages = Ui_application_pages()
        # self.ui_pages.setupUi(self.pages)

        # self.pages.setCurrentWidget(self.ui_pages.page_1)

        self.barra_inferior = cria_layout_moldura(
            altura_minima=30, altura_maxima=30
        )
        self.barra_inferior.setStyleSheet(
            'background-color: #116530;color: #FFFFFF'
        )

        layout_barra_inferior = cria_layout_caixa_horizontal(
            self.barra_inferior, 10, 0, 10, 0
        )

        self.barra_inferior_label_esquerda = QLabel(
            '<a href="https://lariodiniz.github.io/preco_steam/">Ajuda!</a>'
        )
        self.barra_inferior_label_esquerda.setOpenExternalLinks(True)
        espacador_barra_inferior = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.barra_inferior_label_direita = QLabel('Criado por: Lário Diniz')

        layout_barra_inferior.addWidget(self.barra_inferior_label_esquerda)
        layout_barra_inferior.addItem(espacador_barra_inferior)
        layout_barra_inferior.addWidget(self.barra_inferior_label_direita)

        area_principal_layout.addWidget(self.barra_topo)
        area_principal_layout.addWidget(self.janelas)
        area_principal_layout.addWidget(self.barra_inferior)

        self.layout_principal.addWidget(self.area_principal)

    def __defineLayout(self) -> None:
        """Configura o layout inicial da aplicação.

        ..Returns::
            None
        """
        # Configura o tamanho inicial da aplicação.
        self.resize(1200, 720)

        # Configura o tamanho minimo da aplicação.
        self.setMinimumSize(960, 540)

        # Cria a area principal onde os componentes serão renderizados.
        area_total = cria_layout_moldura()

        # Cria o Layout da area total.
        self.layout_principal = cria_layout_caixa_horizontal(area_total)

        # Cria o layout do menu da area esquerda.
        self.__defineMenuEsquerdo()

        # Cria o layout da area principal.
        self.__defineAreaPrincipal()

        # Adiciona a area principal na aplicação.
        self.setCentralWidget(area_total)

    def __defineMenuEsquerdo(self) -> None:
        """Define o Layout do menu esquerdo.

        ..Returns::
            None
        """

        self.menu_esquerdo = cria_layout_moldura(
            largura_minima=50, largura_maxima=50
        )
        self.menu_esquerdo.setStyleSheet('background-color: #4CAE4F')

        layout_menu_esquerdo = cria_layout_caixa_vertical(self.menu_esquerdo)

        area_topo_menu_esquerdo = cria_layout_moldura(altura_minima=40)

        # layout_topo_menu_esquerdo = cria_layout_caixa_vertical(
        #    area_topo_menu_esquerdo
        # )

        # self.toggle_button = PyPushButton(text='Ocultar Barra', icon_path='icon_menu.svg')
        # self.btn_1 = PyPushButton(text='Página Inicial', is_active=True, icon_path='icon_home.svg')
        # self.btn_2 = PyPushButton('Página 2', icon_path='icon_widgets.svg')

        # self.layout_topo_menu_esquerdo.addWidget(self.toggle_button)
        # self.layout_topo_menu_esquerdo.addWidget(self.btn_1)
        # self.layout_topo_menu_esquerdo.addWidget(self.btn_2)

        espacador_menu_esquerdo = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        area_baixo_menu_esquerdo = cria_layout_moldura(altura_minima=40)

        # layout_baixo_menu_esquerdo = cria_layout_caixa_vertical(
        #    area_baixo_menu_esquerdo
        # )

        # self.settings_btn = PyPushButton(text='Configurações', icon_path='icon_settings.svg')

        # self.layout_baixo_menu_esquerdo.addWidget(self.settings_btn)

        self.menu_esquerdo_label_versao = QLabel(self.versao)
        self.menu_esquerdo_label_versao.setAlignment(Qt.AlignCenter)
        self.menu_esquerdo_label_versao.setMinimumHeight(30)
        self.menu_esquerdo_label_versao.setMaximumHeight(30)
        self.menu_esquerdo_label_versao.setStyleSheet('color: #FFFFFF')

        layout_menu_esquerdo.addWidget(area_topo_menu_esquerdo)
        layout_menu_esquerdo.addItem(espacador_menu_esquerdo)
        layout_menu_esquerdo.addWidget(area_baixo_menu_esquerdo)
        layout_menu_esquerdo.addWidget(self.menu_esquerdo_label_versao)

        self.layout_principal.addWidget(self.menu_esquerdo)

    def __definePastas(self) -> None:
        """Cria os atributos `pasta_raiz`, `pasta_imgs` e `pasta_icones` na classe.

        ..Returns::
            None
        """
        pasta_raiz = os.path.abspath(os.getcwd())
        self.pasta_raiz = os.path.join(pasta_raiz, 'codigo')
        self.pasta_imgs = os.path.join(self.pasta_raiz, 'imgs')
        self.pasta_icones = os.path.join(self.pasta_imgs, 'icons')

    def __defineTitulo(self) -> str:
        """Retorna o título da aplicação.

        ..Returns::
            string - O Título da aplicação
        """
        return 'Preço Steam'

    def __defineVersao(self) -> None:
        """Retorna a versão do sistema.

        ..Returns::
            None
        """
        pasta_raiz = os.path.abspath(os.getcwd())
        poetry_tom = os.path.normpath(
            os.path.join(pasta_raiz, 'pyproject.toml')
        )
        version = '0.0.0'
        with open(poetry_tom, 'r', encoding='UTF8') as arquivo:
            read_data = arquivo.readlines()
            for line in read_data:
                if 'version' in line:
                    version = line.split('=')[1]
                    version = (
                        version.replace(' ', '')
                        .replace('\n', '')
                        .replace('"', '')
                    )
                    break

        self.versao = f'v{version}'
