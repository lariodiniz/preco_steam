from datetime import datetime
from bs4 import BeautifulSoup

from codigo.servicos.api import Api
from codigo.dados.modelos import Jogos, Precos

class JogoSteam:
    def __init__(self, url):
        self.__url = url
        self.nome = 'Não Localizado'
        self.descricao = 'Não Localizado'
        self.preco_original = 'Não Localizado'
        self.preco_atual = 'Não Localizado'

    def __formata_para_inteiro(self, valor:str)->int:
        chars = 'R$ ,'
        valor_formatado = valor
        for char in chars:
            valor_formatado = valor_formatado.replace(char,'')

        try:
            valor_formatado = int(valor_formatado)
        except ValueError:
            valor_formatado = -1

        return valor_formatado

    @property
    def preco_atual_int(self)->int:
        return self.__formata_para_inteiro(self.preco_atual)

    @property
    def preco_original_int(self)->int:
        return self.__formata_para_inteiro(self.preco_original)

    def cadastra_jogo(self):
        if self.nome != 'Não Localizado':
            jogo = Jogos(nome=self.nome, descricao=self.descricao,
            preco=self.preco_original_int, link=self.__url)
            jogo.salvar()
            preco = Precos(jogo_id=jogo.id, data=datetime.now(), valor=self.preco_atual_int)
            preco.salvar()

    def atualiza_jogo(self, jogo):
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


    def __str__(self):
        return f"""\
Nome: {self.nome}
Descrição: {self.descricao}
Preço: 
  Original: {self.preco_original}
  Atual: {self.preco_atual}"""

class SteamApi:
    def __init__(self):
        self.api = Api()

    def __formata_texto(self, texto:str)->str:
        return texto.replace('\r', '').replace('\t', '').replace('\n', '')

    def __encontrar(self, div, busca:str, atributo:str='class')->str:
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

    def formata_informacoes(self, html, url):
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

    def buscar_jogo_url(self, url):
        retorno = self.api.buscar(url)
        return self.formata_informacoes(retorno, url)
