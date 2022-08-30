import requests
from codigo.utilidades.excecoes import UrlInvalidaError, UrlNaoAcessivelError

class Api:
    """Classe API
    Esta classe cria a API basica de conexão do sistema.

    ..Methods::
        buscar -- faz uma requisição com o método get e retorna uma string.
    """
    def buscar(self, url:str) -> str:
        """faz uma requisição com o método get e retorna uma string.
        ..Arguments::
            url -- uma string com a url que será feita a requisição.
        ..Returns::
            [str] -- uma string com o retorno da requisição.
        """
        retorno = requests.get(url)
        try:
            if retorno.status_code == 200:
                return retorno.text
            else:
                raise UrlInvalidaError(url, retorno.status_code )
        except requests.exceptions.ConnectionError as ex:
            raise UrlNaoAcessivelError(url)
