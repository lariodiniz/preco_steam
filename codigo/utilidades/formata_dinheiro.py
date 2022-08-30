def formata_dinheiro(valor:int):

    retorno = f'{valor}'
    retorno = f'R$ {retorno[0:-2]},{retorno[len(retorno)-2:len(retorno)]}'

    return retorno