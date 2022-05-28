from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QPushButton


class Botao(QPushButton):
    """Componente Botão.
    Esta classe cria um botão padrão do sistema.

    ..Args::
        texto {str} -- texto que aparece no botão.
        altura {int} -- altura padrão do botão.
        largura_minima {int} -- largura padrão do botão.
        texto_espacamento {int} -- espaçamento padrão do botão.
        texto_cor {str} -- hexadecimal da cor do botão.
        icone {str} -- caminho para o icone do botão
        icone_cor {str} -- hexadecimal da cor do icone do botão.
        botao_cor {str} -- hexadecimal da cor do botão.
        botao_selecionado {str} -- hexadecimal da cor do botão quando selecionado.
        botao_pressionado {str} -- hexadecimal da cor do botão quando precionado.
        ativo {bool} -- estado do botão.

    ..Methods::
        configura_estilo -- Configura o estilo do botão.
        define_estilo -- Aplica o estilo configurado no botão.

    ..Attributes::
        largura_minima {int} -- largura padrão do botão.
        texto_espacamento {int} -- espaçamento padrão do botão.
        texto_cor {str} -- hexadecimal da cor do botão.
        icone {str} -- caminho para o icone do botão
        icone_cor {str} -- hexadecimal da cor do icone do botão.
        botao_cor {str} -- hexadecimal da cor do botão.
        botao_selecionado {str} -- hexadecimal da cor do botão quando selecionado.
        botao_pressionado {str} -- hexadecimal da cor do botão quando precionado.
        ativo {bool} -- estado do botão.
    """

    def __init__(
        self,
        texto: str = '',
        altura: int = 40,
        largura_minima: int = 50,
        texto_espacamento: int = 55,
        texto_cor: str = '#116530',
        icone: str = '',
        icone_cor: str = '#116530',
        botao_cor: str = '#f8f8f2',
        botao_selecionado: str = '#f8f8f2',
        botao_pressionado: str = '#FFFFFF',
        ativo: bool = False,
    ):

        super().__init__()

        self.setText(texto)
        self.setMinimumHeight(altura)
        self.setMaximumHeight(altura)
        self.setCursor(Qt.PointingHandCursor)

        self.largura_minima = largura_minima
        self.icone = icone
        self.icone_cor = icone_cor
        self._ativo = ativo

        self.configura_estilo(
            texto_espacamento=texto_espacamento,
            texto_cor=texto_cor,
            botao_cor=botao_cor,
            botao_selecionado=botao_selecionado,
            botao_pressionado=botao_pressionado,
        )
        self.__define_estilo()

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
        self.texto_espacamento = texto_espacamento
        self.texto_cor = texto_cor
        self.botao_cor = botao_cor
        self.botao_selecionado = botao_selecionado
        self.botao_pressionado = botao_pressionado

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
        self._ativo = acao
        self.__define_estilo()

    def __define_estilo(self) -> None:
        """Configura o estilo do botão.

        ..Returns::
            [None]
        """

        estilo = f"""
        QPushButton {{
            color:{self.texto_cor};
            background-color: {self.botao_cor};
            padding-left: {self.texto_espacamento}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {self.botao_selecionado};
        }}
        QPushButton:pressed {{
            background-color: {self.botao_pressionado};
        }}
        """

        estilo_ativo = f"""
        QPushButton {{
            background-color: {self.botao_selecionado};
            border-right: 5px solid {self.botao_pressionado};

        }}
        """
        if not self._ativo:
            self.setStyleSheet(estilo)
        else:
            self.setStyleSheet(estilo + estilo_ativo)

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

        rect = QRect(0, 0, self.largura_minima, self.height())

        self.__desenha_icone(painter_pai, rect)

    def __desenha_icone(self, painter_pai: QPainter, retangulo: QRect) -> None:
        """Desenha o Icone no Botão
        ..Arguments::
            painter_pai {QPainter} -- Area do botão.
            retangulo {QRect} -- retangulo onde o icone será desenhado

        ..Returns::
            [None]
        """
        icone = QPixmap(self.icone)
        painter = QPainter(icone)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icone.rect(), self.icone_cor)

        painter_pai.drawPixmap(
            int((retangulo.width() - icone.width()) / 2),
            int((retangulo.height() - icone.height()) / 2),
            icone,
        )

        painter.end()
