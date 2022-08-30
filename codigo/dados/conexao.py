from os.path import join
from codigo.utilidades.pasta_do_aplicativo import caminho_do_aplicativo

def busca_conexao():
    """retorna a conexão com o banco de dados do sistema.
    """
    pasta = caminho_do_aplicativo()
    banco = join(pasta, 'sqlite.db')
    return f'sqlite:///{banco}'

def busca_conexao_async():
    """retorna a conexão com o banco de dados do sistema de forma assincrona.
    TODO: NÃO FINALIZADO.
    """
    pasta = caminho_do_aplicativo()
    banco = join(pasta, 'sqlite.db')
    return f'sqlite+aiosqlite:///{banco}'
