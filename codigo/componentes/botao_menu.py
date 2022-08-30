from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QPushButton

from codigo.utilidades import PadraoDeCores

class BotaoMenu(QPushButton):
    """Componente Botão do Meno.
    Esta classe cria um botão para o menu do sistema.

    ..Args::
        texto {str} -- texto que aparece no botão.
        altura {int} -- altura padrão do botão.
        largura_minima {int} -- largura minima padrão do botão.
        largura_maxima {int} -- largura maxima padrão do botão.
        texto_espacamento {int} -- espaçamento padrão do botão.
        texto_cor {str} -- texto do hexadecimal da cor do botão.
        icone {str} -- caminho para o icone do botão
        icone_cor {str} -- texto do hexadecimal da cor do icone do botão.
        botao_cor {str} -- texto do hexadecimal da cor do botão.
        botao_selecionado {str} -- texto do hexadecimal da cor do botão quando selecionado.
        botao_pressionado {str} -- texto do hexadecimal da cor do botão quando precionado.
        ativo {bool} -- estado do botão.

    ..Methods::
        configura_estilo -- Configura o estilo do botão.
        define_estilo -- Aplica o estilo configurado no botão.
    """

    def __init__(
        self,
        texto: str = '',
        altura: int = 40,
        largura_minima: int = 50,
        largura_maxima: int = 240,
        texto_espacamento: int = 55,
        texto_cor: str = PadraoDeCores.botao.menu.texto,
        icone: str = '',
        icone_cor: str = PadraoDeCores.botao.menu.icone,
        botao_cor: str = PadraoDeCores.botao.menu.botao,
        botao_selecionado: str = PadraoDeCores.botao.menu.botao_selecionado,
        botao_pressionado: str = PadraoDeCores.botao.menu.botao_pressionado,
        ativo: bool = False,
    ):

        super().__init__()

        self.setText(texto)
        self.setMinimumHeight(altura)
        self.setMaximumHeight(altura)
        self.setCursor(Qt.PointingHandCursor)

        self.setMinimumWidth(largura_minima)
        self.setMaximumWidth(largura_maxima)
        self.__largura_minima = largura_minima
        self.__icone = icone
        self.__icone_cor = icone_cor
        self.__ativo = ativo

        self.configura_estilo(
            texto_espacamento=texto_espacamento,
            texto_cor=texto_cor,
            botao_cor=botao_cor,
            botao_selecionado=botao_selecionado,
            botao_pressionado=botao_pressionado,
        )
        self.__define_estilo()

    def clique(self, clique) -> None:
        """conecta um evento de clique no botão
        ..Arguments::
            clique {def} -- o Evento de clique que será chamado quando 
            esse botão for clicado.
        ..Returns::
            [None]
        """
        self.clicked.connect(clique)

    def configura_estilo(
        self,
        texto_espacamento: int,
        texto_cor: str,
        botao_cor: str,
        botao_selecionado: str,
        botao_pressionado: str,
    ) -> None:
        """Configura o estilo do botão.

        ..Arguments::
            texto_espacamento {int} -- espaçamento padrão do botão.
            texto_cor {str} -- hexadecimal da cor do botão.
            botao_cor {str} -- hexadecimal da cor do botão.
            botao_selecionado {str} -- hexadecimal da cor do botão quando selecionado.
            botao_pressionado {str} -- hexadecimal da cor do botão quando precionado.

        ..Returns::
            [None]
        """
        self.__texto_espacamento = texto_espacamento
        self.__texto_cor = texto_cor
        self.__botao_cor = botao_cor
        self.__botao_selecionado = botao_selecionado
        self.__botao_pressionado = botao_pressionado

    def define_ativar(self, acao: bool) -> None:
        """Ativa ou desativa o botão.

        ..Arguments::
            texto_espacamento {int} -- espaçamento padrão do botão.
            texto_cor {str} -- hexadecimal da cor do botão.
            botao_cor {str} -- hexadecimal da cor do botão.
            botao_selecionado {str} -- hexadecimal da cor do botão quando selecionado.
            botao_pressionado {str} -- hexadecimal da cor do botão quando precionado.

        ..Returns::
            [None]
        """
        self.__ativo = acao
        self.__define_estilo()

    def __define_estilo(self) -> None:
        """Configura o estilo do botão.

        ..Returns::
            [None]
        """

        estilo = f"""
        QPushButton {{
            color:{self.__texto_cor};
            background-color: {self.__botao_cor};
            padding-left: {self.__texto_espacamento}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {self.__botao_pressionado};
        }}
        QPushButton:pressed {{
            background-color: {self.__botao_selecionado};
        }}
        """

        estilo_ativo = f"""
        QPushButton {{
            background-color: {self.__botao_pressionado};
            border-right: 5px solid {self.__botao_pressionado};

        }}
        """
        if not self.__ativo:
            self.setStyleSheet(estilo)
        else:
            self.setStyleSheet(estilo + estilo_ativo)

    def __desenha_icone(self, painter_pai: QPainter, retangulo: QRect) -> None:
        """Desenha o Icone no Botão
        ..Arguments::
            painter_pai {QPainter} -- Area do botão.
            retangulo {QRect} -- retangulo onde o icone será desenhado

        ..Returns::
            [None]
        """
        icone = QPixmap(self.__icone)
        painter = QPainter(icone)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icone.rect(), self.__icone_cor)

        painter_pai.drawPixmap(
            int((retangulo.width() - icone.width()) / 2),
            int((retangulo.height() - icone.height()) / 2),
            icone,
        )

        painter.end()

    def paintEvent(self, event):
        """Método herdado do QPushButton.

        ..Returns::
            [None]
        """
        QPushButton.paintEvent(self, event)

        painter_pai = QPainter()
        painter_pai.begin(self)
        painter_pai.setRenderHint(QPainter.Antialiasing)
        painter_pai.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.__largura_minima, self.height())

        self.__desenha_icone(painter_pai, rect)

