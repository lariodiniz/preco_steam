import webbrowser

from PySide6.QtWidgets import (QDialog)

from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, Slot
from codigo.utilidades import formata_dinheiro
from codigo.dados.modelos.jogos import Jogos, Precos
from codigo.utilidades.cria_layouts.caixa_horizontal import (
    cria_layout_caixa_horizontal,
)
from codigo.utilidades.cria_layouts.caixa_vertical import (
    cria_layout_caixa_vertical,
)
from codigo.utilidades.cria_layouts.moldura import cria_layout_moldura


from codigo.componentes import (Botao, Celula, Rotulo, Tabela)
class TelaDetalhe(QDialog):

    def __formata_descricao(self):
        descricao = self.jogo.descricao.rstrip('\n')
        #print(descricao)

    def __init__(self, parent, id_jogo:int, *args, **kwargs):
        """Função de Inicialização da janela."""
        # inicializa a classe pai.
        super().__init__(parent, *args, **kwargs)
        self.aplicacao = parent
        self.jogo = Jogos().buscar_id(id_jogo)
        self.preco = Precos().buscar_precos_do_jogo(self.jogo, ordem=Precos.data.desc())
        self.__formata_descricao()
        appIcon = QIcon(self.aplicacao.busca_imagem(self.aplicacao.pasta_icones, 'logo.png'))
        self.setWindowIcon(appIcon)
        self.resize(500, 400)
        self.setStyleSheet(f'background-color: {self.aplicacao.cores.fundo}')
        # Configura o tamanho minimo da aplicação.
        self.setMinimumSize(500, 400)
        self.setMaximumSize(500, 400)


        title = f'Detalhe do jogo {self.jogo.nome}'

        self.setWindowTitle(title)

        layout = cria_layout_caixa_vertical(self)

        self.area_informacoes = cria_layout_moldura()
        self.area_informacoes.setMaximumHeight(180)

        self.area_tabela = cria_layout_moldura()
        self.area_botoes = cria_layout_moldura()

        self.mostra_informacoes()

        self.cria_tabela()
        self.mostra_tabela()

        self.mostra_botoes()
        layout.addWidget(self.area_informacoes)
        layout.addWidget(self.area_tabela)
        layout.addWidget(self.area_botoes)

    def cria_linha_informacoes(self, itens):
        area = cria_layout_moldura()
        linha = cria_layout_caixa_horizontal(
            area, 10, 0, 10, 0
        )
        for index, item in enumerate(itens):
            if index == 1:
                linha.addWidget(item, alignment=Qt.AlignLeft, stretch=1)
            else:
                linha.addWidget(item, alignment=Qt.AlignLeft)

        return area

    def mostra_informacoes(self):
        layout = cria_layout_caixa_vertical(self.area_informacoes)

        self.linha01 = self.cria_linha_informacoes([
            Rotulo(text='Nome do Jogo:', largura_maxima=50),
            Rotulo(text=self.jogo.nome, largura_minima=300, largura_maxima=300)
        ])
        self.linha02 = self.cria_linha_informacoes([
            Rotulo(text='Preço:', largura_maxima=50),
            Rotulo(text=formata_dinheiro(self.jogo.preco))
        ])
        self.linha03 = self.cria_linha_informacoes([
            Rotulo(text='Menor Preço:', largura_maxima=50),
            Rotulo(text=formata_dinheiro(self.jogo.menor_preco().valor))
        ])

        self.linha04 = cria_layout_moldura(altura_minima=200)
        linha04 = cria_layout_caixa_vertical(
            self.linha04, 10, 0, 10, 10
        )
        linha04.addWidget(Rotulo(text='Descrição:'), alignment=Qt.AlignTop)
        descricao = Rotulo(text=self.jogo.descricao, largura_minima=470,  largura_maxima=470, tipo=Rotulo.TIPO.INFORMACAO)
        descricao.setWordWrap(True);
        descricao.setMaximumHeight(100)
        linha04.addWidget(descricao, alignment=Qt.AlignTop, stretch=1)


        layout.addWidget(self.linha01)
        layout.addWidget(self.linha02)
        layout.addWidget(self.linha03)
        layout.addWidget(self.linha04)

    def cria_tabela(self):
        layout = cria_layout_caixa_horizontal(self.area_tabela)
        layout.setContentsMargins(10,0,10,0)
        titulos = ['Data', 'Valor']
        self.tabela = Tabela(titulos)
        self.tabela.setRowCount(len(self.preco))
        self.tabela.desenha_tabela()
        
        layout.addWidget(self.tabela, alignment=Qt.AlignTop, stretch=1)

    def mostra_tabela(self):
        dados = []

        for preco in self.preco:
            dados.append([
                Celula(preco.data.strftime("%d/%m/%Y")),
                Celula(formata_dinheiro(preco.valor))
            ])

        self.tabela.dados = dados
        self.tabela.desenha_tabela()
        
    def mostra_botoes(self):
        layout = cria_layout_caixa_horizontal(self.area_botoes)
        icone='sincronia.png'
        botao_steam = Botao(parent=self.aplicacao, 
        texto='', 
        tipo=Botao.TIPO.INFORMACAO, 
        icone=icone, 
        largura_maxima=150, 
        largura_minima=150)
        botao_steam.clique(self.__clique_notao_steam)

        layout.addWidget(botao_steam)

    @Slot()
    def __clique_notao_steam(self) -> None:
        """Metodo de Clique no botão apagar
        verifica na Steam as promoções.

        ..Returns::
            None
        """
        link = str(self.jogo.link)
        webbrowser.open(link)