import csv
import requests
from codigo.servicos.steam_api import SteamApi

steam = SteamApi()

url = 'https://store.steampowered.com/app/1425760/Punhos_de_Repdio/'
desejos = steam.buscar_jogo_url(url)
print(desejos)

"""
steam = SteamApi()
with open('teste.csv', 'r', encoding='utf-8') as csvfile:  
    linhas_csv = csv.reader(csvfile, delimiter=';')  
    for index, linha in enumerate(linhas_csv):
        if index != 0:
            print(f'\n\nBuscando URL: {linha[2]}')
            desejos = steam.buscar_jogo_url(linha[2])
            print(desejos)
"""