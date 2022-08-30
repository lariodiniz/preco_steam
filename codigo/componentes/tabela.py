from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from codigo.utilidades import PadraoDeCores
from codigo.componentes.botao import Botao
from operator import itemgetter

class TipoCelula:
    """Constante que define os tipos de Celulas.
    Esta classe é a constante dos tipos de celulas aceitos pelo sistema.

    Constants::
        TEXTO --  {int} -- com o valor 0.
        BOTAO --  {int} -- com o valor 1.
        NUMERICO --  {int} -- com o valor 2.
    """
    TEXTO = 0
    BOTAO = 1
    NUMERICO = 2

class Celula:
    """Componente Celula.
    Esta classe cria uma celula padrão do sistema.

    ..Args::
        informacao {str} -- texto que aparece na célula.
        cor {str} -- texto do hexadecimal da cor do botão.
        editavel {bool} -- boleano que define se a célula é editavel ou não.
        tipo {int} -- inteiro que defineo tipo de célula possivel.

    Constants::
        TIPO {TipoCelula} -- constantes com os tipos de células possiveis.
        COR_INDEFINIDA {str} -- constantes que define cor indefinida.

    ..Methods::
        define_clique -- conecta um evento ao botão das células do tipo botão.
    """
    COR_INDEFINIDA = ''
    TIPO = TipoCelula()

    def __init__(self, informacao:str, cor:str='', editavel:bool=False, tipo:int = 0):
        self.informacao = informacao
        self.cor = cor
        self.editavel = editavel
        self.tipo = tipo
        self.clique = None

    def define_clique(self, clique) -> None:
        """conecta um evento de clique do botão da célula;
        ..Arguments::
            clique {def} -- o Evento de clique que será chamado quando 
            esse botão for clicado.
        ..Returns::
            [None]
        """
        self.clique = clique

class Tabela(QTableWidget):
    """Componente Tabela.
    Esta classe cria uma tabela padrão do sistema.

    ..Args::
        titulos: {list} -- lista com os titulos da Tabela.

    ..Attributes::
        titulos {list} -- lisca com o titulo da aplicação.
        dados {list} -- lisca com os dados da tabela.

    ..Methods::
        desenha_tabela -- desenha a tabela na tela.
    """

    def __init__(self, titulos:list, *args, **kargs) -> None:

        super().__init__(*args, **kargs)
        self.__titulos = titulos
        self.__dados = [[]]
        self.__define_estilo()
        self.__ordem = {'campo':self.__titulos[0],'ordem': 'crescente'}
        self.horizontalHeader().sectionClicked.connect(self.__ordenar)

    @property
    def dados(self) -> list:
        """Retorna os dados da tabela.

        ..Returns::
            [list] -- Lista de dados
        """
        return list()+self.__dados

    @dados.setter
    def dados(self, dados: list[Celula]) -> None:
        """define os dados da tabela.

        ..Args::
        dados {list} -- lista de dados.

        ..Returns::
            [None]
        """
        if isinstance(dados, list):
            self.__dados = dados

    def desenha_tabela(self) -> None:
        """desenha a tabela na tela.

        ..Returns::
            [None]
        """
        self.clearContents()
        self.setRowCount(len(self.__dados))

        for linha_numero, linha in enumerate(self.__dados):
            for coluna_numero, coluna in enumerate(linha):
                if coluna.tipo == Celula.TIPO.BOTAO:
                    celula = self.__cria_celula_botao(coluna)
                    self.setCellWidget(linha_numero, coluna_numero, celula)
                else:
                    celula = self.__cria_celula(coluna.informacao)
                    if coluna.cor == Celula.COR_INDEFINIDA:
                        if linha_numero % 2 == 0:
                            celula.setBackground(self.__cor_par())
                        else:
                            celula.setBackground(self.__cor_impar())
                    else:
                        cor = QColor(coluna.cor)
                        celula.setBackground(cor)

                    if not coluna.editavel:
                        celula.setFlags(Qt.ItemIsEnabled)
                    self.setItem(linha_numero, coluna_numero, celula)

        self.resizeColumnsToContents()
        self.resizeRowsToContents()

        self.__configura_titulos()

    @property
    def titulos(self) -> list:
        """Retorna os titulos da tabela.

        ..Returns::
            [list] -- Lista de titulos
        """
        return list()+self.__titulos

    @titulos.setter
    def titulos(self, titulos: list) -> None:
        """define os titulos da tabela.

        ..Args::
        titulos {list} -- lista de titulos.

        ..Returns::
            [None]
        """
        if isinstance(titulos, list):
            self.__titulos = titulos

    def __configura_titulos(self) -> None:
        """configura e mostra na tela os titulos da tabela.

        ..Returns::
            [None]
        """
        vertical_header = self.verticalHeader()
        vertical_header.setVisible(False)

        header = self.horizontalHeader()
        header.setStretchLastSection(True)

        if self.__ordem['ordem'] == 'crescente':
            sentido = '⬇️'
        else:
            sentido = '⬆️'

        titulos = []
        for titulo in self.__titulos:
            if self.__ordem['campo'] == titulo:
                titulos.append(f'{sentido} {titulo}')
            else:
                titulos.append(f'{titulo}')

        self.setColumnCount(len(titulos))
        self.setHorizontalHeaderLabels(titulos)

    def __define_estilo(self) -> None:
        """Define o estilo do botão.

        ..Returns::
            [None]
        """
        estilo = f"""
        QTableWidget {{
            color:{PadraoDeCores.primaria};
            background-color: {PadraoDeCores.entrada_fundo};
            padding: 5px;
            border: 2px solid {PadraoDeCores.primaria};
            border-radius: 10px;
        }}
        QHeaderView::section {{
            background-color: {PadraoDeCores.primaria};
            padding: 5px;
            color: {PadraoDeCores.rotulo.primario.texto};
            border-radius:2px;}}
        QScrollBar {{
            border: 5px solid {PadraoDeCores.primaria};
            background: {PadraoDeCores.entrada_fundo};
            width: 20px;
            margin: 0px 20px 0 20px;

        }}
        QScrollBar::handle {{
            background: {PadraoDeCores.entrada_fundo};
            width: 18px;
            height: 18px;

        }}
        QScrollBar::sub-line {{
        border: 2px solid {PadraoDeCores.entrada_fundo};
        background: {PadraoDeCores.entrada_fundo};
        width: 18px;
        height: 15px;
        }}
        QScrollBar::add-line {{
        border: 2px solid {PadraoDeCores.entrada_fundo};
        background: {PadraoDeCores.entrada_fundo};
        width: 18px;
        height: 15px;

        }}
        """

        self.setStyleSheet(estilo)

    def __cor_impar(self) -> QColor:
        """Retorna a cor para as linhas impares.

        ..Returns::
            [QColor] -- objeto do tipo QColor
        """
        return QColor(PadraoDeCores.tapela_linha_impar)

    def __cor_par(self) -> QColor:
        """Retorna a cor para as linhas pares.

        ..Returns::
            [QColor] -- objeto do tipo QColor
        """
        return QColor(PadraoDeCores.tapela_linha_par)

    def __cria_celula(self, texto:str) -> QTableWidgetItem:
        """Retorna uma célula da tabela.

        ..Args::
        texto {str} -- texto que estara dentro da célula.

        ..Returns::
            [QTableWidgetItem] -- objeto do tipo QTableWidgetItem
        """
        return QTableWidgetItem(str(texto))

    def __cria_celula_botao(self, celula: Celula) -> Botao:
        """Retorna uma célula da tabela.

        ..Args::
        celula {Celula} -- Célula com as informações das botões.

        ..Returns::
            [Botao] -- objeto do tipo Botao
        """
        botao = Botao(parent=self, texto=celula.informacao, tipo=Botao.TIPO.INFORMACAO)
        botao.clique(celula.clique)
        return botao

    @Slot()
    def __ordenar(self, index: int) -> None:
        """Ordena a lista de acordo com o clique do titulo da coluna.

        ..Args::
        index {int} -- index da coluna.

        ..Returns::
            None
        """
        campo = self.__titulos[index]

        if campo == self.__ordem['campo'] and self.__ordem['ordem'] == 'crescente':
            ordem = 'decrescente'
        else:
            ordem = 'crescente'

        self.__ordem = {'campo':campo,'ordem': ordem}

        def ordenar(coluna:list):
            if coluna[index].tipo == Celula.TIPO.NUMERICO:
                return float(coluna[index].informacao.replace('R','').replace('$','').replace('%','').replace(' ','').replace('.','').replace(',','.'))
            else:
                return coluna[index].informacao

        self.__dados =  sorted(self.__dados, key=ordenar, reverse=self.__ordem['ordem'] == 'decrescente')
        self.desenha_tabela()
