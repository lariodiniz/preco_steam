import os

from pytestqt.qt_compat import qt_api

from codigo.aplicacao import Aplicacao


def mensagem_erro(mensagem):
    qt_api.qWarning(mensagem)


def test_titulo_da_aplicacao(qtbot):
    """Verifica o Titulo da Aplicação"""
    window = Aplicacao(show=False)
    # qtbot.addWidget(window)
    # qtbot.waitExposed(window)

    titulo_esperado = 'Preço Steam'
    titulo_da_aplicacao = window.windowTitle()

    mensagem_erro('O Título da aplicação esta errado!')
    assert titulo_da_aplicacao == titulo_esperado


def test_pastas_bases_da_aplicacao(qtbot):
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


def test_busca_imagem_da_aplicacao(qtbot):
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
