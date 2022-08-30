import alembic.config
from PySide6.QtCore import QRunnable, Slot

class AtualizaBanco(QRunnable):
    """Classe de Atualização do Banco.
    Esta classe faz a atualização do banco de dados

    ..Methods::
        run -- faz a atualização do banco de dados.
    """
    @Slot() 
    def run(self):
        """faz a atualização do banco de dados.
        """
        alembicArgs = [
            '--raiseerr',   
            'upgrade', 'head',
        ]
        alembic.config.main(argv=alembicArgs)