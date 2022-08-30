import os

from pytestqt.qt_compat import qt_api

from codigo.componentes.botao import Botao


def test_component_botao_padrao(qtbot):
    """Verifica se o componente botão esta funcionando corretamente."""
    botao = Botao('Teste')

    esperado_texto = 'Teste'
    esperado_altura = 40
    esperado_largura_minima = 50
    esperado_texto_espacamento = 55
    esperado_texto_cor = '#116530'
    esperado_icone = ''
    esperado_icone_cor = '#116530'
    esperado_botao_cor = '#f8f8f2'
    esperado_botao_selecionado = '#FFFFFF'
    esperado_botao_pressionado = '#f8f8f2'

    assert esperado_texto == botao.text(), 'Texto do Botão incorreto'
    assert esperado_altura == botao.height(), 'Altura do Botão incorreta'
    assert (
        esperado_largura_minima == botao.largura_minima
    ), 'Largura do Botão incorreta'
    assert (
        esperado_texto_espacamento == botao.texto_espacamento
    ), 'Espaçamento do texto do Botão incorreta'
    assert (
        esperado_texto_cor == botao.texto_cor
    ), 'Cor do texto do Botão incorreta'
    assert esperado_icone == botao.icone, 'Cor do texto do Botão incorreta'
    assert (
        esperado_icone_cor == botao.icone_cor
    ), 'Cor do texto do Botão incorreta'
    assert esperado_botao_cor == botao.botao_cor, 'Cor do Botão incorreta'
    assert (
        esperado_botao_selecionado == botao.botao_selecionado
    ), 'Cor do Botão selecionado incorreta'
    assert (
        esperado_botao_pressionado == botao.botao_pressionado
    ), 'Cor do Botão pessionado incorreta'


def test_component_botao_estilo(qtbot):
    """Verifica se o componente botão esta funcionando corretamente."""
    botao = Botao('Teste')
    estilo_esperado = """
        QPushButton {
            color:#116530;
            background-color: #f8f8f2;
            padding-left: 55px;
            text-align: left;
            border: none;
        }
        QPushButton:hover {
            background-color: #FFFFFF;
        }
        QPushButton:pressed {
            background-color: #f8f8f2;
        }
        """
    estilo_aplicacao = botao.styleSheet()
    assert (
        estilo_esperado == estilo_aplicacao
    ), 'O estilo da barra_inferior esta errado!'


def test_component_botao_estilo_ativo(qtbot):
    """Verifica se o componente botão esta funcionando corretamente."""
    botao = Botao('Teste')
    botao.define_ativar(True)
    estilo_esperado = """
        QPushButton {
            color:#116530;
            background-color: #f8f8f2;
            padding-left: 55px;
            text-align: left;
            border: none;
        }
        QPushButton:hover {
            background-color: #FFFFFF;
        }
        QPushButton:pressed {
            background-color: #f8f8f2;
        }
        
        QPushButton {
            background-color: #FFFFFF;
            border-right: 5px solid #f8f8f2;

        }
        """
    estilo_aplicacao = botao.styleSheet()
    assert (
        estilo_esperado == estilo_aplicacao
    ), 'O estilo da barra_inferior esta errado!'
