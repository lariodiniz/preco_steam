from PySide6.QtWidgets import QMessageBox

class JanelaDeMensagem(QMessageBox):
    """Componente Janela de Mensagem.
    Esta classe cria a Janela de Mensagens padrão do sistema.

    ..Args::
        titulo {str} -- hexadecimal da cor do botão.
        texto {str} -- caminho para o icone do botão
        texto_informativo {str} -- hexadecimal da cor do icone do botão.
    """

    def __init__( self, titulo: str, texto: str, texto_informativo: str='', *args, **kargs) -> None:

        super().__init__(*args, **kargs)
        self.setWindowTitle(titulo)
        self.setText(texto)
        if texto_informativo != '':
            self.setInformativeText(texto_informativo)


class JanelaDeMensagemAviso(JanelaDeMensagem):
    """Componente Janela de Mensagem Aviso.
    Esta classe cria a Janela de Mensagens para avisos padrão do sistema.
    """
    def __init__(self,*args, **kargs):

        super().__init__(*args, **kargs)
        self.setIcon(QMessageBox.Information)

class JanelaDeMensagemPergunta(JanelaDeMensagem):
    """Componente Janela de Mensagem Aviso.
    Esta classe cria a Janela de Mensagens para avisos padrão do sistema.

    ..Methods::
        sucesso -- retorna se o usuario apertou em OK ou não.
    """

    def __init__(self,*args, **kargs):

        super().__init__(*args, **kargs)
        self.setIcon(QMessageBox.Question)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def sucesso(self, resposta):
        return resposta == QMessageBox.Ok
