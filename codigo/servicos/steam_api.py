from datetime import datetime
from bs4 import BeautifulSoup

from codigo.servicos.api import Api
from codigo.dados.modelos import Jogos, Precos

class JogoSteam:
    """Classe JogoSteam
    Esta classe cria o objeto JogoSteam que organiza as informações dos jogos da Steam.

    ..Args::
        url {str} -- url do Jogo na Steam.

    ..Attributes::
        descricao {str}  -- string contento a descrição do jogo.
        nome {str} -- string contento o nome do jogo.
        preco_atual {str} -- string contento o preço atual do jogo.
        preco_atual_int {int}  -- int contento o preço atual do jogo.
        preco_original {str}  -- string contento o preço original do jogo.
        preco_original_int {int}  -- int contento o preço original do jogo.

    ..Methods::
        atualiza_jogo -- atualiza as informações do jogo no bando de dados.
        cadastra_jogo -- salva as informações do jogo no bando de dados.
    """

    def __init__(self, url: str):
        self.__url = url
        self.nome = 'Não Localizado'
        self.descricao = 'Não Localizado'
        self.preco_original = 'Não Localizado'
        self.preco_atual = 'Não Localizado'

    def atualiza_jogo(self, jogo):
        """Atualiza as informações do jogo no bando de dados.

        ..Returns::
            [None]
        """

        if self.nome != 'Não Localizado':
            preco_original = self.preco_original_int
            if preco_original != jogo.preco:
                jogo.preco = preco_original
                jogo.salvar()
            preco_atual = jogo.preco_atual()
            preco_atual_steam = self.preco_atual_int

            if preco_atual_steam != -1 and preco_atual_steam != preco_atual.valor:
                preco = Precos(jogo_id=jogo.id, data=datetime.now(), valor=preco_atual_steam)
                preco.salvar()

    def cadastra_jogo(self):
        """Cadastra as informações do jogo no bando de dados.

        ..Returns::
            [None]
        """
        if self.nome != 'Não Localizado':
            jogo = Jogos(nome=self.nome, descricao=self.descricao,
            preco=self.preco_original_int, link=self.__url)
            jogo.salvar()
            preco = Precos(jogo_id=jogo.id, data=datetime.now(), valor=self.preco_atual_int)
            preco.salvar()

    @property
    def preco_atual_int(self)->int:
        """retorna o preço atual em formato inteiro.

        ..Returns::
            [int] -- preço atua.
        """
        return self.__formata_para_inteiro(self.preco_atual)

    @property
    def preco_original_int(self)->int:
        """retorna o preço original em formato inteiro.

        ..Returns::
            [int] -- preço original.
        """
        return self.__formata_para_inteiro(self.preco_original)

    def __formata_para_inteiro(self, valor:str)->int:
        """formata a string valor para retornar sem as mascaras em inteiro.

        ..Args::
            valor {str} -- string contento um valor padrão do jogo.

        ..Returns::
            [int] -- valor do jogo em inteiro.
        """
        chars = 'R$ ,'
        valor_formatado = valor
        for char in chars:
            valor_formatado = valor_formatado.replace(char,'')

        try:
            valor_formatado = int(valor_formatado)
        except ValueError:
            valor_formatado = -1

        return valor_formatado

    def __str__(self):
        return f"""\
Nome: {self.nome}
Descrição: {self.descricao}
Preço: 
  Original: {self.preco_original}
  Atual: {self.preco_atual}"""

class SteamApi:
    """Classe SteamApi
    Esta classe cria a API que busca as informações dos jogos na STEAM.

    ..Methods::
        buscar_jogo_url -- busca um jogo na Steam a partir de uma url.
    """
    def __init__(self):
        self.__api = Api()

    def __formata_texto(self, texto:str)->str:
        """Limpa alguns caracteres especiais te um texto.

        ..Args::
            texto {str} -- string contento o texto a ser formatado.

        ..Returns::
            [str] -- texto formatado.
        """
        return texto.replace('\r', '').replace('\t', '').replace('\n', '')

    def __encontrar(self, div, busca:str, atributo:str='class')->str:
        """procura as informações no html da STEAM.

        ..Args::
            div {BeautifulSoup} -- contento o html.
            busca {str} -- class ou id que será procurada.
            atributo {str} --tipo de atributo que o argumento busca será aplicado.
        ..Returns::
            [str] -- informação localizada.
        """
        informacao = 'Não Localizado'
        if atributo == 'id':
            retorno = div.find('div', id=busca)
        else:
            retorno = div.find('div', class_=busca)
        if retorno:
            informacao = self.__formata_texto(retorno.text)
            informacao = informacao if informacao != 'Try the Demo!' else 'Não Localizado'
            informacao = informacao if informacao[-4:] != 'Demo' else 'Não Localizado'
        return informacao

    def __formata_informacoes(self, html:str, url:str) -> JogoSteam:
        """busca as informações do jogo no html da STEAM.

        ..Args::
            html {str} -- html do jogo na Steam.
            url {str} -- url do jogo na Steam.
        ..Returns::
            [JogoSteam] -- informações que foram localizadas do jogo.
        """
        soup = BeautifulSoup(html, 'html.parser')
        jogo = JogoSteam(url)
        jogo.nome = self.__encontrar(soup, busca='appHubAppName', atributo='id')
        jogo.descricao = self.__encontrar(soup, busca='game_description_snippet')

        area_preco =  soup.find_all('div', class_='game_purchase_action')
        if area_preco:
            for area in area_preco:
                jogo.preco_original = self.__encontrar(area, busca='discount_original_price')
                if jogo.preco_original == 'Não Localizado':
                    jogo.preco_original = self.__encontrar(area, busca='discount_final_price')
                    if jogo.preco_original == 'Não Localizado':
                        jogo.preco_original = self.__encontrar(area, busca='price')
                    jogo.preco_atual = jogo.preco_original
                else:
                    jogo.preco_original = self.__encontrar(area, busca='discount_original_price')
                    jogo.preco_atual = self.__encontrar(area, busca='discount_final_price')

                if jogo.preco_original != 'Não Localizado':
                    break

        return jogo

    def buscar_jogo_url(self, url: str) -> JogoSteam:
        """busca as informações do jogo no html da STEAM.

        ..Args::
            url {str} -- url do jogo na Steam.
        ..Returns::
            [JogoSteam] -- informações que foram localizadas do jogo.
        """
        retorno = self.__api.buscar(url)
        return self.__formata_informacoes(retorno, url)
