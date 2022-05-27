from PySide6.QtWidgets import QVBoxLayout


def cria_layout_caixa_vertical(
    frame,
    distancia_esquerda: int = 0,
    distancia_topo: int = 0,
    distancia_direita: int = 0,
    distancia_baixo: int = 0,
) -> QVBoxLayout:
    """Cria um QVBoxLayout padronizado.

    ..Arguments::
        frame {QFrame} -- O QFrame que será o pai do QVBoxLayout.
        distancia_esquerda: {int} -- o espaçamento da margem esquerda.
        distancia_topo: {int} -- o espaçamento da margem do topo.
        distancia_direita: {int} -- o espaçamento da margem direita.
        distancia_baixo: {int} -- o espaçamento da margem de baixo.
    """
    layout_horizontal = QVBoxLayout(frame)
    layout_horizontal.setContentsMargins(
        distancia_esquerda, distancia_topo, distancia_direita, distancia_baixo
    )
    layout_horizontal.setSpacing(0)
    return layout_horizontal
