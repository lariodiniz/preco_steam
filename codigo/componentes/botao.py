from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QPushButton

from codigo.utilidades import PadraoDeCores


class TipoBotao:
    """Constante que define os tipos de botões.
    Esta classe é a constante dos tipos de botões aceitos pelosistema.

    Constants::
        PRIMARIO --  {int} -- com o valor 0.
        SECUNDARIO --  {int} -- com o valor 1.
        SUCESSO --  {int} -- com o valor 2.
        PERIGO --  {int} -- com o valor 3.
        CUIDADO --  {int} -- com o valor 4.
        INFORMACAO  --  {int} -- com o valor 5.
    """

    PRIMARIO = 0
    SECUNDARIO = 1
    SUCESSO = 2
    PERIGO = 3
    CUIDADO = 4
    INFORMACAO = 5

class Botao(QPushButton):
    """Componente Botão.
    Esta classe cria um botão padrão do sistema.

    ..Args::
        texto {str} -- texto que aparece no botão.
        altura {int} -- altura padrão do botão.
        largura_minima {int} -- largura minima padrão do botão.
        largura_maxima {int} -- largura maxima padrão do botão.
        texto_cor {str} -- texto do hexadecimal da cor do botão.
        tipo {int} -- inteiro que defineo tipo de botão possivel.
        icone {str} -- caminho para o icone do botão

    Constants::
        TIPO {TipoBotao} -- Constantes com os tipos de botões possiveis.

    ..Methods::
        clique -- conecta um evento ao botão.
    """

    TIPO = TipoBotao

    def __init__(
        self,
        parent,
        texto: str = '',
        altura: int = 40,
        largura_minima: int = 50,
        largura_maxima: int = 240,
        tipo:int = TipoBotao.PRIMARIO,
        icone: str = ''
    ) -> None:

        super().__init__()

        #Define as cores do botão
        self.__configura_cores(tipo)

        #Define Texto do botão
        self.setText(texto)

        #Define o cursor que aparecerá quando o mouse estiver sobre o botão
        self.setCursor(Qt.PointingHandCursor)

        #define altura do botão.
        self.setMinimumHeight(altura)
        self.setMaximumHeight(altura)

        #Define a largura do botão.
        self.__largura_minima = largura_minima
        self.setMinimumWidth(largura_minima)
        self.setMaximumWidth(largura_maxima)

        #Define o Icone do botão.
        if icone != '':
            self.__icone = parent.busca_imagem(parent.pasta_botoes, icone)
        else:
             self.__icone = None

        #Define o Estilo do botão.
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

    def paintEvent(self, event) -> None:
        """Método herdado do QPushButton.

        ..Returns::
            [None]
        """
        QPushButton.paintEvent(self, event)
        if self.__icone:
            painter_pai = QPainter()
            painter_pai.begin(self)
            painter_pai.setRenderHint(QPainter.Antialiasing)
            painter_pai.setPen(Qt.NoPen)

            rect = QRect(0, 0, self.__largura_minima, self.height())

            self.__desenha_icone(painter_pai, rect)

    def __configura_cores(self, tipo) -> None:
        """Configura as cores do botão.
    
        ..Args::
        tipo {int} -- inteiro que defineo tipo de botão possivel.
        
        ..Returns::
            [None]
        """
        if tipo == TipoBotao.SECUNDARIO:
            cores = PadraoDeCores.botao.secundario
        elif tipo == TipoBotao.SUCESSO:
            cores = PadraoDeCores.botao.sucesso
        elif tipo == TipoBotao.PERIGO:
            cores = PadraoDeCores.botao.perigo
        elif tipo == TipoBotao.CUIDADO:
            cores = PadraoDeCores.botao.cuidado
        elif tipo == TipoBotao.INFORMACAO:
            cores = PadraoDeCores.botao.informacao
        else:
            cores = PadraoDeCores.botao.primario

        self.__texto_cor = cores.texto
        self.__botao_cor = cores.botao
        self.__botao_selecionado = cores.botao_selecionado
        self.__botao_pressionado = cores.botao_pressionado
        self.__texto_cor_pressionado = PadraoDeCores.primaria
        self.__icone_cor = cores.icone

    def __define_estilo(self) -> None:
        """Define o estilo do botão.

        ..Returns::
            [None]
        """

        estilo = f"""
        QPushButton {{
            color:{self.__texto_cor};
            background-color: {self.__botao_cor};
            text-align: center;
            border: none;
            border: 2px solid {self.__botao_cor};
            border-radius: 5px;
        }}
        QPushButton:hover {{
            color:{self.__botao_pressionado};
            background-color: {self.__botao_selecionado};
            border: 2px solid {self.__botao_selecionado};
            
        }}
        QPushButton:pressed {{
            color:{self.__texto_cor_pressionado};
            background-color: {self.__botao_pressionado};
            border: 2px solid {self.__botao_pressionado};
        }}
        """
        self.setStyleSheet(estilo)

    def __desenha_icone(self, painter_pai: QPainter, retangulo: QRect) -> None:
        """Desenha o Icone no Botão
        ..Arguments::
            painter_pai {QPainter} -- Area do botão.
            retangulo {QRect} -- retangulo onde o icone será desenhado

        ..Returns::
            [None]
        """
        if self.__icone:
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
