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
    """Tela Cadastro.
    Esta classe é responsavel pela tela de cadastro da aplicação.

    ..Args::
        parent {Aplicacao} -- Classe base da aplicação.
    """

    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        layout = cria_layout_caixa_vertical(self)

        self.__barra_topo = cria_layout_moldura(
            altura_minima=50, altura_maxima=50
        )
        self.__area_grid = cria_layout_moldura()

        self.__cria_botoes_superiores()
        self.__cria_formulario()

        layout.addWidget(self.__barra_topo)
        layout.addWidget(self.__area_grid)

    def __busca_jogo(self, url:str) -> None:
        """Busca o jogo na Steam para cadastrar.

        ..Arguments::
            url {str} -- url do jogo.

        ..Returns::
            None
        """
        steam_api = SteamApi()
        jogo_steam = steam_api.buscar_jogo_url(url)
        if jogo_steam.nome != 'Não Localizado':
            jogo_steam.cadastra_jogo()
        else:
            self.aplicacao.janela_aviso(titulo='Erro!', texto='O jogo não foi localizado.')

    def __cria_botoes_superiores(self) -> None:
        """Cria os botões na barra superior da janela.

        ..Returns::
            None
        """
        barra_topo_layout = cria_layout_caixa_horizontal(
            self.__barra_topo, 10, 0, 10, 0
        )

        barra_topo_espacador = QSpacerItem(
            50, 50, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        barra_topo_layout.addItem(barra_topo_espacador)

        botoes = [
            ['cadastro.png', self.__clique_botao_cadastro], 
            ['importar_csv.png', self.__clique_botao_importar_planilha]]

        for botao in botoes:
            botao_gerado = Botao(
                parent=self.aplicacao, 
                texto='', 
                largura_maxima=50, 
                icone=botao[0])
            botao_gerado.clique(botao[1])
            barra_topo_layout.addWidget(botao_gerado)

    def __cria_formulario(self) -> None:
        """Cria os botões na barra superior da janela.

        ..Returns::
            None
        """

        layout = cria_layout_caixa_vertical(self.__area_grid)
        formulario_espacador = QSpacerItem(
            50, 550, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        formulario_area_rotulo = cria_layout_moldura()
        formulario_layout_rotulo = cria_layout_caixa_horizontal(formulario_area_rotulo)
        link_jogo = Rotulo(text='Url do Jogo', largura_maxima=75, largura_minima=75)
        self.__link_entrada = Entrada(largura=900)

        formulario_layout_rotulo.addWidget(link_jogo)
        formulario_layout_rotulo.addWidget(self.__link_entrada)

        layout.addWidget(formulario_area_rotulo)
        layout.addItem(formulario_espacador)

    @Slot()
    def __clique_botao_cadastro(self) -> None:
        """Metodo de Clique no botão menu
        Cadastra um jogo a partir do link informado no rótulo "__link_entrada" 

        ..Returns::
            None
        """
        link = self.__link_entrada.text()
        if 'https://store.steampowered.com/app/' in link:
            retorno = Jogos().buscar_link(link)
            if retorno:
                self.aplicacao.janela_aviso(titulo='Erro!',
                    texto=f'Jogo já se encontra cadastrado com o nome "{retorno.nome}"')
            else:
                self.__busca_jogo(link)
                self.aplicacao.janela_aviso(titulo='Sucesso!',
                    texto='Jogo Cadastrado')
        else:
            self.aplicacao.janela_aviso(titulo='Erro!',
                    texto=f'Link inválido."')

    @Slot()
    def __clique_botao_importar_planilha(self) -> None:
        """Metodo de Clique no botão importar planilha
        importa as urls de uma planilha e insere no sistema.

        ..Returns::
            None
        """ 
        pergunta = self.aplicacao.janela_pergunta(titulo='Você tem certeza?',
            texto=f'Você gostaria de importar os jogos de um arquivo?')
        resp = pergunta.exec_()
        if pergunta.sucesso(resp):
            dialogo = QFileDialog.getOpenFileName(self.aplicacao, 
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
                                self.aplicacao.janela_aviso(titulo='Erro!',
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
                                self.__busca_jogo(link)
                                asinc.updateProgress.emit(index)

                    asincrono = Asincrono(self.aplicacao, len(linhas))
                    asincrono.define_run(executar(asincrono))
                    asincrono.start()

                    self.aplicacao.progress_bar.setValue(0)
                    self.aplicacao.janela_aviso(titulo='Sucesso!',
                        texto='Planilha exportada!')
