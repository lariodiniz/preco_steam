from PySide6.QtWidgets import QFrame

from codigo.utilidades.cria_layouts.moldura import cria_layout_moldura


def test_cria_layout_caixa_vertical(qtbot):
    """Verifica se a função cria_layout_moldura esta criando corretamente"""
    layout = cria_layout_moldura(10, 20, 30, 40)

    tipo_do_layou = type(layout)
    tipo_do_h_box_layout = type(QFrame())
    assert (
        tipo_do_layou == tipo_do_h_box_layout
    ), 'Layout retornado não corresponde ao esperado.'
