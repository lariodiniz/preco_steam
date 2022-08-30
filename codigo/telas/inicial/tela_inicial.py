import os
import csv

from operator import itemgetter
import webbrowser
from PySide6.QtWidgets import (
    QSizePolicy,
    QSpacerItem,
    QFileDialog
)
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QColor

from codigo.utilidades.cria_layouts.caixa_horizontal import (
    cria_layout_caixa_horizontal,
)
from codigo.utilidades.cria_layouts.caixa_vertical import (
    cria_layout_caixa_vertical,
)

from codigo.servicos.steam_api import SteamApi
from codigo.utilidades.cria_layouts.moldura import cria_layout_moldura

from codigo.utilidades import formata_dinheiro, PadraoDeCores, Asincrono
from codigo.componentes import (Botao, Tabela, Celula, Entrada, Rotulo, 
CaixaDeMarcar)

from codigo.telas.detalhe.tela_detalhe import TelaDetalhe

from codigo.dados.modelos.jogos import Jogos
from codigo.telas.tela_base import TelaBase


class TelaInicial(TelaBase):

    @Slot()
    def __clique_botao_atualizar(self):
        self.__busca_jogos()
        self.__monta_tabela()

    def showEvent(self, event):
        self.__busca_jogos()
        self.__monta_tabela()

    def __init__(self, parent, *args, **kwargs):
        """Função de Inicialização da janela."""
        # inicializa a classe pai.
        super().__init__(parent, *args, **kwargs)

        self.__busca_jogos()
        self.detalhe = None
        self.__preco_de_hoje = {}
        
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
        barra_topo_espacador2 = QSpacerItem(
            50, 50, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        icone_atualizar='atualizar.png'
        icone_sincronia='sincronia.png'
        icone_apagar= 'apagar.png'
        icone_exporta_csv='exporta_csv.png'
        icone_apaga_tabela='apaga_tabela.png'

        self.botao_atualizar = Botao(parent=self.__aplicacao, texto='', largura_maxima=50, icone=icone_atualizar)
        self.botao_atualizar.clique(self.__clique_botao_atualizar)
        self.botao_sincronizar = Botao(parent=self.__aplicacao, texto='', largura_maxima=50, icone=icone_sincronia)
        self.botao_sincronizar.clique(self.__clique_botao_sincronia)
        self.botao_apagar = Botao(parent=self.__aplicacao, texto='', largura_maxima=50, icone=icone_apagar)
        self.botao_apagar.clique(self.__clique_botao_apagar)
        self.botao_apagar_todos = Botao(parent=self.__aplicacao, texto='', largura_maxima=50, icone=icone_apaga_tabela)
        self.botao_apagar_todos.clique(self.__clique_botao_apagar_todos)
        self.botao_gerar_planilha = Botao(parent=self.__aplicacao, texto='', largura_maxima=50, icone=icone_exporta_csv)
        self.botao_gerar_planilha.clique(self.__gerar_planilha)
        
        self.rotulo_numero_de_jogos = Rotulo(text='Jogos', tipo=Rotulo.TIPO.CUIDADO)
        self.rotulo_numero_de_jogos.setMaximumHeight(40)
        barra_topo_layout.addWidget(self.botao_atualizar)
        barra_topo_layout.addWidget(self.botao_gerar_planilha)
        barra_topo_layout.addItem(barra_topo_espacador)
        barra_topo_layout.addWidget(self.botao_apagar)
        barra_topo_layout.addWidget(self.botao_apagar_todos)
        barra_topo_layout.addItem(barra_topo_espacador2)
        barra_topo_layout.addWidget(self.rotulo_numero_de_jogos)
        barra_topo_layout.addWidget(self.botao_sincronizar)

        self.area_filtros = cria_layout_moldura()
        self.area_grid = cria_layout_moldura()
        self.__cria_filtros()
        self.__cria_tabela()
        self.__monta_tabela()

        layout.addWidget(barra_topo)
        layout.addWidget(self.area_filtros)
        layout.addWidget(self.area_grid)

    def __mostra_numero_jogos(self, numero):
        self.rotulo_numero_de_jogos.setText(f'Jogos: {numero}')

    def __cria_filtros(self):
        
        layout = cria_layout_caixa_horizontal(self.area_filtros)
        layout.setContentsMargins(10,0,10,0)
        
        rotulo_filtro_nome = Rotulo(text='Nome do Jogo')
        self.filtro_nome = Entrada(largura=600)
        self.filtro_desconto = CaixaDeMarcar(text='Descontos')

        layout.addWidget(rotulo_filtro_nome, alignment=Qt.AlignLeft)
        layout.addWidget(self.filtro_nome, alignment=Qt.AlignLeft, stretch=1)
        layout.addWidget(self.filtro_desconto)

    def __cria_tabela(self):
        layout = cria_layout_caixa_horizontal(self.area_grid)
        layout.setContentsMargins(10,10,10,10)
        
        titulos = ['id', 'Nome', 'Preço', 'Menor Preço', 
                    'Menor Desconto %', 'Preço de Hoje', 
                    'Desconto %', 'Steam']
        self.tabela = Tabela(titulos)
        self.tabela.clicked.connect(self.__clica_tabela)
        layout.addWidget(self.tabela)
    
    @Slot()
    def __clica_tabela(self, item):
        linha_selecionada  = self.tabela.currentRow()
        celula_selecionada = self.tabela.item(linha_selecionada,0)
        if celula_selecionada:
            id = self.tabela.item(linha_selecionada,0).text()
            self.detalhe = TelaDetalhe(self.__aplicacao, int(id))
            self.detalhe.exec_()

    

    def __busca_jogos(self):
        if 'filtro_nome' in dir(self):
            filtro_nome = self.filtro_nome.text()
            if filtro_nome:
                filtro_nome = f'%{filtro_nome}%'
                self.jogos = Jogos().buscar_filtro(Jogos.nome.like(filtro_nome))
            else:
                self.jogos = Jogos().buscar_todos()
        else:
            self.jogos = Jogos().buscar_todos()

    def __formata_jogos(self):
        jogos = []
        for jogo in self.jogos:
            id = jogo.id
            nome = jogo.nome
            preco = jogo.preco
            preco_menor = jogo.menor_preco()
            if preco_menor:
                menor_preco = preco_menor.valor
                if jogo.preco > 0:
                    menor_desconto = int(100 - ((preco_menor.valor * 100) / jogo.preco))
                else:
                    menor_desconto = 0
            else:
                menor_preco = -1
                menor_desconto = -1

            if len(self.__preco_de_hoje) > 0:
                preco_de_hoje = self.__preco_de_hoje[jogo.id]
                if jogo.preco > 0:
                    desconto_hoje = int(100 - ((preco_de_hoje * 100) / jogo.preco))
                else:
                    desconto_hoje = 0
            else:
                preco_de_hoje = -1
                desconto_hoje = -1
            link = jogo.link

            if not self.filtro_desconto.isChecked():
                jogos.append([id, nome, preco, menor_preco, menor_desconto, preco_de_hoje, desconto_hoje, link])
            elif desconto_hoje > 0:
                jogos.append([id, nome, preco, menor_preco, menor_desconto, preco_de_hoje, desconto_hoje, link])

        return jogos

    def __monta_tabela(self):
        
        jogos = self.__formata_jogos()
        numero_jogos = len(jogos)
        self.__mostra_numero_jogos(numero_jogos)

        dados = []
        for dado in jogos:
            celulas = []

            menor_preco = dado[3]
            preco_de_hoje = dado[5]
            preco = dado[2]

            for index, coluna in enumerate(dado):
                if index == 2:
                    celula = Celula(formata_dinheiro(coluna), tipo=Celula.TIPO.NUMERICO)
                elif index == 3:
                    celula = Celula(formata_dinheiro(coluna), tipo=Celula.TIPO.NUMERICO)
                    if preco_de_hoje == menor_preco and preco_de_hoje < preco:
                        celula.cor = PadraoDeCores.rotulo.cuidado.fundo
                elif index == 4:
                    celula = Celula(f'{coluna}%', tipo=Celula.TIPO.NUMERICO)
                elif index == 5:
                    informacao = 'INDEFINIDO' if coluna == -1 else formata_dinheiro(coluna)
                    celula = Celula(informacao, tipo=Celula.TIPO.NUMERICO)
                    if preco_de_hoje <= menor_preco and preco_de_hoje < preco:
                        celula.cor = PadraoDeCores.rotulo.cuidado.fundo
                elif index == 6:
                    informacao = 'INDEFINIDO' if coluna == -1 else f'{coluna}%'
                    celula = Celula(informacao, tipo=Celula.TIPO.NUMERICO)
                    if preco_de_hoje <= menor_preco and preco_de_hoje < preco:
                        celula.cor = PadraoDeCores.rotulo.cuidado.fundo
                elif index == 7:
                    celula = Celula('Abrir')
                    celula.tipo = Celula.TIPO.BOTAO
                    celula.define_clique(self.__clique_abrir)
                else:
                    celula = Celula(coluna)

                celulas.append(celula)
            dados.append(celulas)

        self.tabela.dados = dados
        self.tabela.desenha_tabela()
        self.tabela.setColumnWidth(1, 300)

    def __criaBotaoTabela(self):
        btn = Botao(parent=self.__aplicacao, texto='Abrir', tipo=Botao.TIPO.INFORMACAO)
        btn.clique(self.__clique_abrir)
        return btn

    @Slot()
    def __gerar_planilha(self) -> None:
        """Metodo de Clique no botão apagar
        verifica na Steam as promoções.

        ..Returns::
            None
        """
        pergunta = self.__aplicacao.janela_pergunta(titulo='Você tem certeza?',
            texto=f'Você gostaria de gerar um arquivo csv dos seus jogos?')
        resp = pergunta.exec_()
        if pergunta.sucesso(resp):
            dialogo = QFileDialog.getSaveFileName(self.__aplicacao, 
                'Salvar arquivo',
                selectedFilter="CSV (*csv)",
                filter="CSV (*csv)")
            nome_arquivo= dialogo[0]
            if nome_arquivo:
                nome_arquivo = os.path.splitext(nome_arquivo)[0]

                def executar(asinc):
                    titulo = ['Nome', 'Descricao', 'Link']

                    with open(f'{nome_arquivo}.csv', 'w', newline='', encoding='utf-8') as csvfile:  
                        csvwriter = csv.writer(csvfile, delimiter=';')  
                        csvwriter.writerow(titulo)  
                        for index, jogo in enumerate(self.jogos):
                            csvwriter.writerow([jogo.nome, jogo.descricao, jogo.link])  
                            asinc.updateProgress.emit(index)

                asincrono = Asincrono(self.__aplicacao, len(self.jogos))
                asincrono.define_run(executar(asincrono))
                asincrono.start()

                self.__aplicacao.progress_bar.setValue(0)
                self.__aplicacao.janela_aviso(titulo='Sucesso!', texto='Planilha criada!')

    @Slot()
    def __clique_botao_apagar_todos(self) -> None:
        """Metodo de Clique no botão apagar
        verifica na Steam as promoções.

        ..Returns::
            None
        """
        pergunta = self.__aplicacao.janela_pergunta(titulo='Você tem certeza?',
            texto=f'Você gostaria de apagar TODOS os jogos?')
        resp = pergunta.exec_()
        if pergunta.sucesso(resp):
            def executar(asinc):
                for index, jogo in enumerate(self.jogos):
                    jogo.deletar()
                    asinc.updateProgress.emit(index)

            asincrono = Asincrono(self.__aplicacao, len(self.jogos))
            asincrono.define_run(executar(asincrono))
            asincrono.start()

            self.__aplicacao.progress_bar.setValue(0)
            self.__aplicacao.janela_aviso(titulo='Sucesso!',texto='Jogos Deletados!')
            self.__monta_tabela()

    @Slot()
    def __clique_abrir(self) -> None:
        """Metodo de Clique no botão apagar
        verifica na Steam as promoções.

        ..Returns::
            None
        """
        linha_selecionada  = self.tabela.currentRow()
        celula_selecionada = self.tabela.item(linha_selecionada,0)
        if celula_selecionada:
            id = self.tabela.item(linha_selecionada,0).text()
            jogo = [jogo for jogo in self.jogos if jogo.id == int(id)][0]
            link = str(jogo.link)
            webbrowser.open(link)

    @Slot()
    def __clique_botao_apagar(self) -> None:
        """Metodo de Clique no botão apagar
        verifica na Steam as promoções.

        ..Returns::
            None
        """
        linha_selecionada  = self.tabela.currentRow()
        celula_selecionada = self.tabela.item(linha_selecionada,0)
        if celula_selecionada:
            id = self.tabela.item(linha_selecionada,0).text()
            jogo = [jogo for jogo in self.jogos if jogo.id == int(id)][0]
            nome_do_jogo = jogo.nome
            pergunta = self.__aplicacao.janela_pergunta(titulo='Você tem certeza?',
            texto=f'Você gostaria de apagar o jogo "{nome_do_jogo}"?')
            resp = pergunta.exec_()
            if pergunta.sucesso(resp):
                jogo.deletar()
                self.__monta_tabela()
                self.__aplicacao.janela_aviso(titulo='Sucesso!',
                    texto=f'Jogo "{nome_do_jogo}" deletado.')

    
    @Slot()
    def __clique_botao_sincronia(self) -> None:
        """Metodo de Clique no botão sincronia
        verifica na Steam as promoções.

        ..Returns::
            None
        """
        def executar(asinc):
            steam_api = SteamApi()
            for index, jogo in enumerate(self.jogos):
                url = jogo.link
                jogo_steam = steam_api.buscar_jogo_url(url)
                if jogo_steam.nome != 'Não Localizado':
                    jogo_steam.atualiza_jogo(jogo)
                    self.__preco_de_hoje[jogo.id] = jogo_steam.preco_atual_int

                asinc.updateProgress.emit(index)

        asincrono = Asincrono(self.__aplicacao, len(self.jogos))
        asincrono.define_run(executar(asincrono))
        asincrono.start()

        self.__monta_tabela()
        self.__aplicacao.progress_bar.setValue(0)
        self.__aplicacao.janela_aviso(titulo='Sucesso!',
            texto='Atualização Finalizada')

