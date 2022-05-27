from PySide6.QtWidgets import QVBoxLayout

from codigo.utilidades.cria_layouts.caixa_vertical import (
    cria_layout_caixa_vertical,
)


def test_cria_layout_caixa_vertical(qtbot):
    """Verifica se a função test_cria_layout_caixa_vertical esta criando corretamente"""
    layout = cria_layout_caixa_vertical(None, 10, 20, 30, 40)

    tipo_do_layou = type(layout)
    tipo_do_h_box_layout = type(QVBoxLayout())
    assert (
        tipo_do_layou == tipo_do_h_box_layout
    ), 'Layout retornado não corresponde ao esperado.'
