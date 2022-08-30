
import os

from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Slot, QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QProgressBar

)
from shiboken6 import Object

from codigo.utilidades.versao_do_aplicativo import versao_do_aplicativo
from codigo.utilidades.cria_layouts.caixa_horizontal import (
    cria_layout_caixa_horizontal,
)
from codigo.utilidades.cria_layouts.caixa_vertical import (
    cria_layout_caixa_vertical,
)

from codigo.utilidades import PadraoDeCores, GestorDeTelas
from codigo.utilidades.cria_layouts.moldura import cria_layout_moldura

from codigo.telas.inicial.tela_inicial import TelaInicial
from codigo.telas.cadastro.tela_cadastro import TelaCadastro
from codigo.dados.atualiza_banco import AtualizaBanco
from codigo.componentes import (
    BotaoMenu, JanelaDeMensagemAviso, JanelaDeMensagemPergunta
)

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
        define_progresso --  Atualiza a barra de progresso do sistema.

    ..Attributes::
        cores {PadraoDeCores} -- Classe com as cores padrão do sistema.
        progress_bar {QProgressBar} -- Barra de progresso na parte inferior da aplicação.
        pasta_icones {str} -- string contento o caminho dos icones.
        pasta_imgs {str} -- string contento o caminho da pasta de imagens.
        pasta_raiz {str} -- string contento o caminho da pasta da aplicação.
        versao {str} -- string contento a versão do sistema.
    """

    def __init__(self, show: bool = True) -> None:
        """Função de Inicialização da aplicação."""
        # inicializa a classe pai.
        super().__init__()

        #Usa o Alambic para atualizar o banco de dados.
        self.__atualiza_banco()

        #Define as cores padrões do sistema.
        self.__define_cores_padroes()
        
        # Adiciona as telas na aplicação
        self.__telas = {
            'inicial': GestorDeTelas(0,TelaInicial),
            'cadastro': GestorDeTelas(1,TelaCadastro),
        }

        # define pastas do sistema.
        self.__define_pastas()

        # define a versão
        self.__define_versao()

        # define o título da aplicação.
        title = self.__define_titulo()
        self.setWindowTitle(title)

        # define o icone da aplicação.
        self.__appIcon = QIcon(self.busca_imagem(self.pasta_icones, 'logo.png'))
        self.setWindowIcon(self.__appIcon)

        # define tamanho inicial de tela
        self.__define_layout()

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

    def define_progresso(self, valor: int) -> None:
        """define o valor da barra de progresso

        ..Arguments::
            valor {str} -- o diretório onde a imagem esta
            imagem {str} -- o nome da imagem

        ..Returns::
            None
        """
        self.progress_bar.setValue(valor)

    def janela_aviso(self, titulo:str, texto:str) -> None:
        """Mostra a Janela de aviso.

        ..Arguments::
            titulo {str} -- titulo da janela.
            texto {str} -- texto da janela
        ..Returns::
            None
        """
        janela = JanelaDeMensagemAviso(titulo=titulo, texto=texto)
        janela.setWindowIcon(self.__appIcon)
        janela.exec_()

    def janela_pergunta(self, titulo:str, texto:str) -> JanelaDeMensagemPergunta:
        """Mostra a Janela de aviso.

        ..Arguments::
            titulo {str} -- titulo da janela.
            texto {str} -- texto da janela
        ..Returns::
            None
        """
        janela = JanelaDeMensagemPergunta(titulo=titulo, texto=texto)
        janela.setWindowIcon(self.__appIcon)
        return janela

    def __ativa_botao_menu(self, nome_botao:str) -> None:
        """Define o botão do menu clicado como ativo e remove o ativo
        dos outros botões.

        ..Arguments::
            nome_botao {str} -- o diretório onde a imagem esta

        ..Returns::
            None
        """
        for botao in self.__botoes_do_menu.keys():
            self.__botoes_do_menu[botao].define_ativar(nome_botao==botao)

    def __atualiza_banco(self) -> None:
        """Atualiza o Banco de dados.

        ..Returns::
            None
        """
        atualizacao = AtualizaBanco()
        QThreadPool().start(atualizacao)

    @Slot()
    def __clique_botao_menu(self) -> None:
        """Metodo de Clique no botão menu
        Mostra ou esconde o menu a esquerda.

        ..Returns::
            None
        """
        menu_largura = self.__menu_esquerdo.width()
        width = 50

        if menu_largura == width:
            width = 240

        self.__animation = QPropertyAnimation(self.__menu_esquerdo, b'minimumWidth')
        self.__animation.setStartValue(menu_largura)
        self.__animation.setEndValue(width)
        self.__animation.setDuration(500)
        self.__animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.__animation.start()

    @Slot()
    def __clique_botao_tela_cadastro(self) -> None:
        """Metodo de Clique no botão tela cadastro
        Mostra a tela de cadastro.

        ..Returns::
            None
        """
        self.__mostra_tela('cadastro')
        self.__barra_topo_label_direito.setText('Cadastro')

    @Slot()
    def __clique_botao_tela_inicial(self) -> None:
        """Metodo de Clique no botão tela inicial
        Mostra a tela inicial.

        ..Returns::
            None
        """
        self.__mostra_tela('inicial')
        self.__barra_topo_label_direito.setText('Pagina Inicial')

    def __define_area_principal(self) -> None:
        """Define o Layout da Area Principal.

        ..Returns::
                None
        """

        #Cria o Frame principal.
        area_principal = cria_layout_moldura()
        area_principal.setStyleSheet(f'background-color: {self.cores.fundo}')

        #Cria a box vertical principal.
        area_principal_layout = cria_layout_caixa_vertical(area_principal)

        #Cria o Frame da barra do topo.
        barra_topo = cria_layout_moldura(altura_minima=30, altura_maxima=30)
        barra_topo.setStyleSheet(
            f'background-color:  {self.cores.secundaria}; color:  {self.cores.rotulo.primario.texto}'
        )

        #Cria a box horizontal da barra do topo.
        layout_barra_topo = cria_layout_caixa_horizontal(barra_topo, 10, 0, 10, 0)

        #Cria o texto a esquerda da barra do topo.
        barra_topo_label_esquerdo = QLabel(
            'Gerencie os preços dos jogos que você mais deseja!'
        )

        #Cria um espaçador para a barra do topo.
        espacador_barra_topo = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        #Cria o texto a direita da barra do topo.
        self.__barra_topo_label_direito = QLabel('Pagina Inicial')
        self.__barra_topo_label_direito.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #Adiciona os textos e o espaçador na barra do topo.
        layout_barra_topo.addWidget(barra_topo_label_esquerdo)
        layout_barra_topo.addItem(espacador_barra_topo)
        layout_barra_topo.addWidget(self.__barra_topo_label_direito)

        #Cria a pilha onde as janelas vão ficar.
        self.__janelas = QStackedWidget()
        self.__janelas.setStyleSheet(f'font-size:12pt; color: {self.cores.rotulo.primario.texto}')

        #Adiciona as janelas na pilha.
        for tela in self.__telas.keys():
            self.__janelas.addWidget(self.__telas[tela].tela(self))

        #Cria o Frame da barra do inferior.
        barra_inferior = cria_layout_moldura(altura_minima=30, altura_maxima=30)
        barra_inferior.setStyleSheet(
            f'background-color: {self.cores.secundaria};color: {self.cores.rotulo.primario.texto}'
        )

        #Cria a box horizontal da barra inferior.
        layout_barra_inferior = cria_layout_caixa_horizontal(
            barra_inferior, 10, 0, 10, 0
        )

        #Cria o texto a esquerda da barra inferior.
        barra_inferior_label_esquerda = QLabel(
            '<a href="https://lariodiniz.github.io/preco_steam/">Ajuda!</a>'
        )
        barra_inferior_label_esquerda.setOpenExternalLinks(True)

        #Cria dois espaçadores para a barra inferior.
        espacador_barra_inferior1 = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        espacador_barra_inferior2 = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        #Cria a barra de progresso da barra inferior.
        self.progress_bar = QProgressBar()

        #Cria o texto a direita da barra inferior.
        barra_inferior_label_direita = QLabel('Criado por: Lário Diniz')

        #Adiciona os textos, os espaçadores e a barra de progresso na barra do topo.
        layout_barra_inferior.addWidget(barra_inferior_label_esquerda)
        layout_barra_inferior.addItem(espacador_barra_inferior1)
        layout_barra_inferior.addWidget(self.progress_bar)
        layout_barra_inferior.addItem(espacador_barra_inferior2)
        layout_barra_inferior.addWidget(barra_inferior_label_direita)

        #Adiciona as barras e as janelas na area principal.
        area_principal_layout.addWidget(barra_topo)
        area_principal_layout.addWidget(self.__janelas)
        area_principal_layout.addWidget(barra_inferior)

        #Adiciona a area principal na janela.
        self.__layout_principal.addWidget(area_principal)

    def __define_cores_padroes(self) -> None:
        """Define as cores padrões da aplicação.

        ..Returns::
            None
        """
        self.cores = PadraoDeCores()

    def __define_layout(self) -> None:
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
        self.__layout_principal = cria_layout_caixa_horizontal(area_total)

        # Cria o layout do menu da area esquerda.
        self.__define_menu_esquerdo()

        # Cria o layout da area principal.
        self.__define_area_principal()

        # Adiciona a area principal na aplicação.
        self.setCentralWidget(area_total)

    def __define_menu_esquerdo(self) -> None:
        """Define o Layout do menu esquerdo.

        ..Returns::
            None
        """

        cor_menu_esquerdo = self.cores.primaria
        
        self.__menu_esquerdo = cria_layout_moldura(largura_minima=50, largura_maxima=50)
        self.__menu_esquerdo.setStyleSheet(f'background-color: {cor_menu_esquerdo}')
        layout_menu_esquerdo = cria_layout_caixa_vertical(self.__menu_esquerdo)
        area_topo_menu_esquerdo = cria_layout_moldura(altura_minima=40)
        layout_topo_menu_esquerdo = cria_layout_caixa_vertical(
            area_topo_menu_esquerdo
        )

        icone_menu = self.busca_imagem(self.pasta_botoes, 'menu.png')
        icone_inicial = self.busca_imagem(self.pasta_botoes, 'promocao.png')
        icone_cadastro = self.busca_imagem(self.pasta_botoes, 'cadastro.png')

        self.__botoes_do_menu ={
            'menu': BotaoMenu(texto='Ocultar Barra', icone=icone_menu),
            'inicial': BotaoMenu(texto='Inicial', icone=icone_inicial, ativo=True),
            'cadastro': BotaoMenu(texto='Cadastro', icone=icone_cadastro),
        }

        self.__botoes_do_menu['menu'].clique(self.__clique_botao_menu)
        self.__botoes_do_menu['inicial'].clique(self.__clique_botao_tela_inicial)
        self.__botoes_do_menu['cadastro'].clique(self.__clique_botao_tela_cadastro)

        for botao in self.__botoes_do_menu.keys():
            layout_topo_menu_esquerdo.addWidget(self.__botoes_do_menu[botao])
        
        espacador_menu_esquerdo = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        area_baixo_menu_esquerdo = cria_layout_moldura(altura_minima=40)

        self.__menu_esquerdo_label_versao = QLabel(self.versao)
        self.__menu_esquerdo_label_versao.setAlignment(Qt.AlignCenter)
        self.__menu_esquerdo_label_versao.setMinimumHeight(30)
        self.__menu_esquerdo_label_versao.setMaximumHeight(30)
        self.__menu_esquerdo_label_versao.setStyleSheet(f'color: {self.cores.rotulo.primario.texto}')

        layout_menu_esquerdo.addWidget(area_topo_menu_esquerdo)
        layout_menu_esquerdo.addItem(espacador_menu_esquerdo)
        layout_menu_esquerdo.addWidget(area_baixo_menu_esquerdo)
        layout_menu_esquerdo.addWidget(self.__menu_esquerdo_label_versao)

        self.__layout_principal.addWidget(self.__menu_esquerdo)

    def __define_pastas(self) -> None:
        """Cria os atributos `pasta_raiz`, `pasta_imgs`, `pasta_botoes` e `pasta_icones` na classe.

        ..Returns::
            None
        """
        pasta_raiz = os.path.abspath(os.getcwd())
        self.pasta_raiz = os.path.join(pasta_raiz, 'codigo')
        self.pasta_imgs = os.path.join(self.pasta_raiz, 'imgs')
        self.pasta_icones = os.path.join(self.pasta_imgs, 'icons')
        self.pasta_botoes = os.path.join(self.pasta_imgs, 'botoes')

    def __define_titulo(self) -> str:
        """Retorna o título da aplicação.

        ..Returns::
            string - O Título da aplicação
        """
        return 'Jogos Desejados'

    def __define_versao(self) -> None:
        """Retorna a versão do sistema.

        ..Returns::
            None
        """
        self.versao = f'v{versao_do_aplicativo()}'

    def __mostra_tela(self, nome: str) -> None:
        """Mostra a tela informada.

        ..Arguments::
            nome {str} -- nome da tela

        ..Returns::
            None
        """
        self.__ativa_botao_menu(nome)
        self.__janelas.setCurrentIndex(self.__telas[nome].index)
