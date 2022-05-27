from PySide6.QtWidgets import QHBoxLayout


def cria_layout_caixa_horizontal(
    frame,
    distancia_esquerda: int = 0,
    distancia_topo: int = 0,
    distancia_direita: int = 0,
    distancia_baixo: int = 0,
):
    """Cria um QHBoxLayout padronizado.

    ..Arguments::
        frame {QFrame} -- O QFrame que será o pai do QHBoxLayout.
        distancia_esquerda: {int} -- o espaçamento da margem esquerda.
        distancia_topo: {int} -- o espaçamento da margem do topo.
        distancia_direita: {int} -- o espaçamento da margem direita.
        distancia_baixo: {int} -- o espaçamento da margem de baixo.
    """
    layout_horizontal = QHBoxLayout(frame)
    layout_horizontal.setContentsMargins(
        distancia_esquerda, distancia_topo, distancia_direita, distancia_baixo
    )
    layout_horizontal.setSpacing(0)
    return layout_horizontal
