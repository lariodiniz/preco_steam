from PySide6.QtCore import QThread, Signal

class Asincrono(QThread):
    updateProgress = Signal(int)

    def __init__(self, aplicacao, maximo):
        QThread.__init__(self)
        
        self.updateProgress.connect(aplicacao.define_progresso)
        aplicacao.progress_bar.setRange(1, maximo-1)
        aplicacao.progress_bar.setValue(0)

    def define_run(self, executar):
        self.executar = executar

    def run(self):
        if self.executar:
            self.executar()
