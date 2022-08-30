from os import getcwd
from os.path import abspath, normpath, join

def versao_do_aplicativo()->str:
    """Retorna a versão do sistema.

        ..Returns::
            string -> Versão do sistema
        """
    pasta_raiz = abspath(getcwd())
    poetry_tom = normpath(join(pasta_raiz, 'pyproject.toml'))
    version = '0.0.0'
    with open(poetry_tom, 'r', encoding='UTF8') as arquivo:
        read_data = arquivo.readlines()
        for line in read_data:
            if 'version' in line:
                version = line.split('=')[1]
                version = (
                    version.replace(' ', '')
                    .replace('\n', '')
                    .replace('"', '')
                )
                break
    return version