import csv
from datetime import datetime
from PySide6.QtWidgets import (
    QSpacerItem,
    QSizePolicy,
    QFileDialog
)
from PySide6.QtCore import Slot

from codigo.servicos.steam_api import SteamApi
from codigo.componentes import (Botao, Entrada, Rotulo)

from codigo.dados.modelos.jogos import Jogos
from codigo.utilidades import Asincrono

from codigo.utilidades.cria_layouts.caixa_horizontal import (
    cria_layout_caixa_horizontal,
)
from codigo.utilidades.cria_layouts.caixa_vertical import (
    cria_layout_caixa_vertical,
)
from codigo.utilidades.cria_layouts.moldura import cria_layout_moldura
from codigo.telas.tela_base import TelaBase


class TelaCadastro(TelaBase):


    def __init__(self, parent, *args, **kwargs):
        """Função de Inicialização da janela."""
        # inicializa a classe pai.
        super().__init__(parent, *args, **kwargs)
        self.__aplicacao = parent
        layout = cria_layout_caixa_vertical(self)
        barra_topo = cria_layout_moldura(
            altura_minima=50, altura_maxima=50
        )

        barra_topo_layout = cria_layout_caixa_horizontal(
            barra_topo, 10, 0, 10, 0
        )
        barra_topo_espacador = QSpacerItem(
            50, 50, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        icone= 'cadastro.png'
        self.botao_cadastro = Botao(parent=self.__aplicacao, texto='', largura_maxima=50, icone=icone)
        self.botao_cadastro.clique(self.__clique_botao_cadastro)

        icone_importar_csv='importar_csv.png'
        self.botao_importar_planilha = Botao(parent=self.__aplicacao, texto='', largura_maxima=50, icone=icone_importar_csv)
        self.botao_importar_planilha.clique(self.__clique_botao_importar_planilha)
        
        barra_topo_layout.addItem(barra_topo_espacador)
        barra_topo_layout.addWidget(self.botao_importar_planilha)
        barra_topo_layout.addWidget(self.botao_cadastro)

        self.area_grid = cria_layout_moldura()
        self.__cria_formulario()

        layout.addWidget(barra_topo)
        layout.addWidget(self.area_grid)

    def __cria_formulario(self):
        layout = cria_layout_caixa_horizontal(self.area_grid)

        self.link_entrada = Entrada(largura=600)
        link_jogo = Rotulo(text='Url do Jogo')
        layout.addWidget(link_jogo)
        layout.addWidget(self.link_entrada)

    @Slot()
    def __clique_botao_importar_planilha(self) -> None:
        """Metodo de Clique no botão menu
        Mostra ou esconde o menu a esquerda.

        ..Returns::
            None
        """ 
        pergunta = self.__aplicacao.janela_pergunta(titulo='Você tem certeza?',
            texto=f'Você gostaria de importar os jogos de um arquivo?')            
        resp = pergunta.exec_()
        if pergunta.sucesso(resp):
            dialogo = QFileDialog.getOpenFileName(self.__aplicacao, 
                'Selecionar arquivo',
                selectedFilter="CSV (*csv)",
                filter="CSV (*csv)")
            nome_arquivo= dialogo[0]
            if nome_arquivo:
                linhas =[]
                with open(f'{nome_arquivo}', 'r', encoding='utf-8') as csvfile:  
                    linhas_csv = csv.reader(csvfile, delimiter=';')  
                    for index, linha in enumerate(linhas_csv):
                        if index == 0:
                            if linha[2] != 'Link':
                                self.__aplicacao.janela_aviso(titulo='Erro!',
                                    texto='Planilha Selecionada Invalida!')
                                break
                        else:
                            linhas.append(linha)
                
                if len(linhas)>0:
                    def executar(asinc):
                        for index, linha in enumerate(linhas):
                            link = linha[2]
                            retorno = Jogos().buscar_link(link)
                            if retorno:
                                print(f'Jogo já se encontra cadastrado com o nome "{retorno.nome}"')
                            else:
                                self.busca_jogo(link)
                                asinc.updateProgress.emit(index)

                    asincrono = Asincrono(self.__aplicacao, len(linhas))
                    asincrono.define_run(executar(asincrono))
                    asincrono.start()

                    self.__aplicacao.progress_bar.setValue(0)
                    self.__aplicacao.janela_aviso(titulo='Sucesso!',
                        texto='Planilha exportada!')

    @Slot()
    def __clique_botao_cadastro(self) -> None:
        """Metodo de Clique no botão menu
        Mostra ou esconde o menu a esquerda.

        ..Returns::
            None
        """
        link = self.link_entrada.text()
        if 'https://store.steampowered.com/app/' in link:
            retorno = Jogos().buscar_link(link)
            if retorno:
                self.__aplicacao.janela_aviso(titulo='Erro!',
                    texto=f'Jogo já se encontra cadastrado com o nome "{retorno.nome}"')
            else:
                self.busca_jogo(link)
                self.__aplicacao.janela_aviso(titulo='Sucesso!',
                    texto='Jogo Cadastrado')
        else:
            self.__aplicacao.janela_aviso(titulo='Erro!',
                    texto=f'Link inválido."')


    def busca_jogo(self, url):
        steam_api = SteamApi()
        jogo_steam = steam_api.buscar_jogo_url(url)
        if jogo_steam.nome != 'Não Localizado':
            jogo_steam.cadastra_jogo()
        else:
            self.__aplicacao.janela_aviso(titulo='Erro!', texto='O jogo não foi cadastrado.')
