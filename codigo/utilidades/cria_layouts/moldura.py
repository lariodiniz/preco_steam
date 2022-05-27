from PySide6.QtWidgets import QFrame

altura_minima: int
largura_minima: int
altura_maxima: int
largura_maxima: int


def cria_layout_moldura(
    altura_minima: int = -1,
    largura_minima: int = -1,
    altura_maxima: int = -1,
    largura_maxima: int = -1,
):
    """Cria um QFrame padronizado.

    ..Arguments::
        altura_minima: {int} -- altura minima que essa moldura poderá ter.
        largura_minima: {int} -- largura minima que essa moldura poderá ter.
        altura_maxima: {int} -- altura maxima que essa moldura poderá ter.
        largura_maxima: {int} -- largura maxima que essa moldura poderá ter.
    """
    moldura = QFrame()
    if altura_minima > -1:
        moldura.setMinimumHeight(altura_minima)

    if largura_minima > -1:
        moldura.setMinimumWidth(largura_minima)

    if altura_maxima > -1:
        moldura.setMaximumHeight(altura_maxima)

    if largura_maxima > -1:
        moldura.setMaximumWidth(largura_maxima)

    return moldura
