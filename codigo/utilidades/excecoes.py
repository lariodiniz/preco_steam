class UrlNaoAcessivelError(Exception):
    """Não foi possivel acessar a url."""
    def __init__(self, url, *args):
        super().__init__(args)
        self.__url = url

    def __str__(self):
        return f'Não foi possivel acessar a url {self.__url}'

class UrlInvalidaError(Exception):
    """url invalida!"""
    def __init__(self, url, codigo, *args):
        super().__init__(args)
        self.__url = url
        self.__codigo = codigo

    def __str__(self):
        return f'Uma requisição para a url {self.__url} retornou um status code de {self.__codigo}'