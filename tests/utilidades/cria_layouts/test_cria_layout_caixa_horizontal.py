from PySide6.QtWidgets import QHBoxLayout

from codigo.utilidades.cria_layouts.caixa_horizontal import (
    cria_layout_caixa_horizontal,
)


def test_cria_layout_caixa_horizontal(qtbot):
    """Verifica se a função cria_layout_caixa_horizontal esta criando corretamente"""
    layout = cria_layout_caixa_horizontal(None, 10, 20, 30, 40)

    tipo_do_layou = type(layout)
    tipo_do_h_box_layout = type(QHBoxLayout())
    largura_do_layout_esperada = 10

    assert (
        tipo_do_layou == tipo_do_h_box_layout
    ), 'Layout retornado não corresponde ao esperado.'
