import os
from time import sleep
from pytestqt.qt_compat import qt_api
from PySide6.QtCore import Qt
from PySide6 import QtTest
from codigo.aplicacao import Aplicacao


def mensagem_erro(mensagem):
    qt_api.qWarning(mensagem)


def test_aplicacao_versao(qtbot):
    """Verifica o Titulo da Aplicação"""
    window = Aplicacao(show=False)
    # qtbot.addWidget(window)
    # qtbot.waitExposed(window)

    versao_esperado = 'v0.1.0'
    versao_aplicacao = window.versao

    assert (
        versao_aplicacao == versao_esperado
    ), 'A versão da aplicação esta errada.'


def test_aplicacao_dimensoes(qtbot):
    """Verifica o Titulo da Aplicação"""
    window = Aplicacao(show=False)
    # qtbot.addWidget(window)
    # qtbot.waitExposed(window)

    largura_esperado = 1200
    largura_aplicacao = window.width()

    altura_esperado = 720
    altura_aplicacao = window.height()

    assert (
        largura_aplicacao == largura_esperado
    ), 'Largura inicial da aplicação incorreto'
    assert (
        altura_aplicacao == altura_esperado
    ), 'Altura inicial da aplicação incorreto'


def test_aplicacao_titulo(qtbot):
    """Verifica o Titulo da Aplicação"""
    window = Aplicacao(show=False)
    # qtbot.addWidget(window)
    # qtbot.waitExposed(window)

    titulo_esperado = 'Preço Steam'
    titulo_da_aplicacao = window.windowTitle()

    mensagem_erro('O Título da aplicação esta errado!')
    assert titulo_da_aplicacao == titulo_esperado


def test_aplicacao_pastas_bases(qtbot):
    """Verifica as pastas bases da Aplicação"""
    window = Aplicacao(show=False)

    pasta_base = os.path.abspath(os.getcwd())

    pasta_raiz_esperada = os.path.join(pasta_base, 'codigo')
    pasta_imgs_esperada = os.path.join(pasta_raiz_esperada, 'imgs')
    pasta_icons_esperada = os.path.join(pasta_imgs_esperada, 'icons')

    pasta_raiz_da_aplicacao = window.pasta_raiz
    pasta_imgs_da_aplicacao = window.pasta_imgs
    pasta_icons_da_aplicacao = window.pasta_icones

    assert (
        pasta_raiz_da_aplicacao == pasta_raiz_esperada
    ), 'A pasta raiz da aplicação esta errada!'
    assert (
        pasta_imgs_da_aplicacao == pasta_imgs_esperada
    ), 'A pasta de imagens da aplicação esta errada!'
    assert (
        pasta_icons_da_aplicacao == pasta_icons_esperada
    ), 'A pasta de icones da aplicação esta errada!'


def test_aplicacao_busca_imagem(qtbot):
    """Verifica a função busca imagem da Aplicação"""
    window = Aplicacao(show=False)

    pasta_base = os.path.abspath(os.getcwd())

    imagem = 'logo.png'
    pasta_raiz = os.path.join(pasta_base, 'codigo')
    pasta_imgs = os.path.join(pasta_raiz, 'imgs')
    pasta_icons = os.path.join(pasta_imgs, 'icons')
    caminho_da_imagem_esperada = os.path.normpath(
        os.path.join(pasta_icons, imagem)
    )

    caminho_da_imagem_da_aplicacao = window.busca_imagem(
        window.pasta_icones, imagem
    )

    assert (
        caminho_da_imagem_esperada == caminho_da_imagem_da_aplicacao
    ), 'O método busca_imagem da aplicação esta retornando um caminho errado!'


def test_aplicacao_barra_topo_label_esquerdo(qtbot):
    """Verifica o texto no label na barra do topo a esquerda"""
    window = Aplicacao(show=False)
    texto_esperado = 'Gerencie os preços dos jogos que você mais deseja!'
    texto_aplicacao = window.barra_topo_label_esquerdo.text()
    assert (
        texto_esperado == texto_aplicacao
    ), 'O texto no label na barra do topo a esquerda esta errado!'


def test_aplicacao_barra_topo_label_direito(qtbot):
    """Verifica o texto no label na barra do topo a direita"""
    window = Aplicacao(show=False)
    texto_esperado = 'PAGINA INICIAL'
    texto_aplicacao = window.barra_topo_label_direito.text()
    assert (
        texto_esperado == texto_aplicacao
    ), 'O texto no label na barra do topo a direita esta errado!'


def test_aplicacao_barra_inferior_label_esquerda(qtbot):
    """Verifica o texto no label na barra inferior esquerda"""
    window = Aplicacao(show=False)
    texto_esperado = (
        '<a href="https://lariodiniz.github.io/preco_steam/">Ajuda!</a>'
    )
    texto_aplicacao = window.barra_inferior_label_esquerda.text()
    assert (
        texto_esperado == texto_aplicacao
    ), 'O texto no label na barra inferior esquerda esta errado!'


def test_aplicacao_barra_inferior_label_direita(qtbot):
    """Verifica o texto no label na barra inferior direita"""
    window = Aplicacao(show=False)
    texto_esperado = 'Criado por: Lário Diniz'
    texto_aplicacao = window.barra_inferior_label_direita.text()
    assert (
        texto_esperado == texto_aplicacao
    ), 'O texto no label na barra inferior direita esta errado!'


def test_aplicacao_menu_esquerdo_label_versao(qtbot):
    """Verifica o texto no label na barra inferior direita"""
    window = Aplicacao(show=False)
    texto_esperado = 'v0.1.0'
    texto_aplicacao = window.menu_esquerdo_label_versao.text()
    assert (
        texto_esperado == texto_aplicacao
    ), 'O texto no label versão na barra da esquerda esta errado!'


def test_aplicacao_estilo_area_principal(qtbot):
    """Verifica o estilo da area_principal"""
    window = Aplicacao(show=False)
    estilo_esperado = 'background-color: #EEEDDE'
    estilo_aplicacao = window.area_principal.styleSheet()
    assert (
        estilo_esperado == estilo_aplicacao
    ), 'O estilo da area_principal esta errado!'


def test_aplicacao_estilo_barra_topo(qtbot):
    """Verifica o estilo da barra_topo"""
    window = Aplicacao(show=False)
    estilo_esperado = 'background-color: #116530;color: #FFFFFF'
    estilo_aplicacao = window.barra_topo.styleSheet()
    assert (
        estilo_esperado == estilo_aplicacao
    ), 'O estilo da barra_topo esta errado!'


def test_aplicacao_estilo_label_barra_topo_direito(qtbot):
    """Verifica o estilo da barra_topo"""
    window = Aplicacao(show=False)
    estilo_esperado = "font: 700 9pt 'Segoe UI'"
    estilo_aplicacao = window.barra_topo_label_direito.styleSheet()
    assert (
        estilo_esperado == estilo_aplicacao
    ), 'O estilo da label_barra_topo_direito esta errado!'


def test_aplicacao_estilo_janelas(qtbot):
    """Verifica o estilo da janelas"""
    window = Aplicacao(show=False)
    estilo_esperado = 'font-size:12pt; color: #f8f8f2'
    estilo_aplicacao = window.janelas.styleSheet()
    assert (
        estilo_esperado == estilo_aplicacao
    ), 'O estilo da janelas esta errado!'


def test_aplicacao_estilo_barra_inferior(qtbot):
    """Verifica o estilo da barra_inferior"""
    window = Aplicacao(show=False)
    estilo_esperado = 'background-color: #116530;color: #FFFFFF'
    estilo_aplicacao = window.barra_inferior.styleSheet()
    assert (
        estilo_esperado == estilo_aplicacao
    ), 'O estilo da barra_inferior esta errado!'


def test_aplicacao_largura_menu_esquerdo(qtbot):
    """Verifica o estilo da barra_inferior"""
    window = Aplicacao(show=False)
    largura_do_menu_esquerdo_esperada = 50
    largura_do_menu_esquerdo = window.menu_esquerdo.width()

    assert (
        largura_do_menu_esquerdo_esperada == largura_do_menu_esquerdo
    ), 'Largura do menu esquerdo incorreta incorreta'

def test_aplicacao_menu_esquerdo_botao_menu_texto(qtbot):
    """Verifica o texto do botão menu"""
    window = Aplicacao(show=False)
    botao_texto_esperada = 'Ocultar Barra'
    botao_texto = window.botao_menu.text()

    assert (
        botao_texto_esperada == botao_texto
    ), 'O texto do botão menu esta incorreto'

def test_aplicacao_menu_esquerdo_botao_menu_click(qtbot):
    """Verifica o click do botão menu"""
    window = Aplicacao(show=False)
    qtbot.addWidget(window)

    qtbot.wait_for_window_shown(window)
    qtbot.mouseClick(window.botao_menu, Qt.LeftButton)
    qtbot.wait(550)

    largura_do_menu_esquerdo_esperada = 240
    largura_do_menu_esquerdo = window.menu_esquerdo.width()
    assert (
        largura_do_menu_esquerdo_esperada == largura_do_menu_esquerdo
    ), 'A largura do menur esquerto esta incorreta'

