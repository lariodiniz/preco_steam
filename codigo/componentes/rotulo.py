from PySide6.QtWidgets import QLabel

from codigo.utilidades import PadraoDeCores


class TipoRotulo:
    """Constante que define os tipos de botões.
    Esta classe é a constante dos tipos de botões aceitos pelosistema.

    Constants::
        PRIMARIO --  {int} -- com o valor 0.
        SECUNDARIO --  {int} -- com o valor 1.
        SUCESSO --  {int} -- com o valor 2.
        PERIGO --  {int} -- com o valor 3.
        CUIDADO --  {int} -- com o valor 4.
        INFORMACAO  --  {int} -- com o valor 5.
    """

    PRIMARIO = 0
    SECUNDARIO = 1
    SUCESSO = 2
    PERIGO = 3
    CUIDADO = 4
    INFORMACAO = 5


class Rotulo(QLabel):
    """Componente Rotulo.
    Esta classe cria um rotulo padrão do sistema.

    ..Args::
        largura_minima {int} -- largura minima do rotulo.
        largura_maxima {int} -- largura maxima do rotulo.
        espacamento {int} -- espaçãmento interno das margens.
        tipo {str} -- hexadecimal da cor da fonte rotulo.

    Constants::
        TIPO {TipRotulo} -- Constantes com os tipos de rotulos possiveis.

    """

    TIPO = TipoRotulo

    def __init__(
        self,
        largura_minima: int = 100,
        largura_maxima: int = 200,
        espacamento: int = 5,
        tipo:int = TipoRotulo.PRIMARIO,
        *args, **kargs
    ):

        super().__init__(*args, **kargs)

        self.__configura_cores(tipo, espacamento)
        self.setMinimumWidth(largura_minima)
        self.setMaximumWidth(largura_maxima)

    def __configura_cores(self, tipo: int, espacamento: int) -> None:
        """Configura as cores do rotulo.

        ..Args::
        tipo {int} -- inteiro que defineo tipo de rotulo possivel.
        espacamento {int} -- espaçãmento interno das margens.

        ..Returns::
            [None]
        """
        if tipo == TipoRotulo.SECUNDARIO:
            cores = PadraoDeCores.rotulo.secundario
        elif tipo == TipoRotulo.SUCESSO:
            cores = PadraoDeCores.rotulo.sucesso
        elif tipo == TipoRotulo.PERIGO:
            cores = PadraoDeCores.rotulo.perigo
        elif tipo == TipoRotulo.CUIDADO:
            cores = PadraoDeCores.rotulo.cuidado
        elif tipo == TipoRotulo.INFORMACAO:
            cores = PadraoDeCores.rotulo.informacao
        else:
            cores = PadraoDeCores.rotulo.primario

        estilo = f"""
        QLabel {{
            font: 700 9pt 'Segoe UI'; 
            color:{cores.texto};
            background-color: {cores.fundo};
            padding: {espacamento}px;
        }}
        """
        self.setStyleSheet(estilo)

