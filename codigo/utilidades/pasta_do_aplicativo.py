from os import mkdir, environ
from os.path import isdir, join


def caminho_do_aplicativo():
    pasta = join(environ['APPDATA'], 'preco_steam')
    if not isdir(pasta):
        mkdir(pasta)
    return pasta