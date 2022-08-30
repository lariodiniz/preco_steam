class RotuloCor:
    def __init__(self, texto, fundo):
        self.texto = texto
        self.fundo = fundo

class RotulosCores:
    primario = RotuloCor('#f8f8f2','#A1B1A0')
    secundario = RotuloCor('#f8f8f2','#4CAE4F')
    sucesso = RotuloCor('#f8f8f2','#28a745')
    perigo = RotuloCor('#f8f8f2','#dc3545')
    cuidado = RotuloCor('#116530','#ffc107')
    informacao = RotuloCor('#f8f8f2','#17a2b8')

class BotaoCor:
    def __init__(self, texto, icone, botao, 
        botao_selecionado, botao_pressionado):
        self.texto = texto
        self.icone = icone
        self.botao = botao
        self.botao_selecionado = botao_selecionado
        self.botao_pressionado = botao_pressionado

class BotoesCores:
    menu = BotaoCor('#f8f8f2','#f8f8f2','#116530','#f8f8f2','#A1B1A0')
    primario = BotaoCor('#f8f8f2','#f8f8f2','#4CAE4F','#f8f8f2','#116530')
    secundario = BotaoCor('#f8f8f2','#f8f8f2','#116530','#f8f8f2','#4CAE4F')
    sucesso = BotaoCor('#f8f8f2','#f8f8f2','#28a745','#f8f8f2','#116530')
    perigo = BotaoCor('#f8f8f2','#f8f8f2','#dc3545','#f8f8f2','#4CAE4F')
    cuidado = BotaoCor('#116530','#116530','#ffc107','#f8f8f2','#4CAE4F')
    informacao = BotaoCor('#f8f8f2','#f8f8f2','#17a2b8','#f8f8f2','#4CAE4F')


class PadraoDeCores:
    botao = BotoesCores
    rotulo = RotulosCores
    primaria = '#116530'
    secundaria = '#4CAE4F'
    fundo = '#A1B1A0'
    fundo_claro = '#fff3cd'
    entrada_fundo = '#FFFFFF'
    entrada_texto = '#116530'
    tapela_linha_impar = '#4CAE4F'
    tapela_linha_par = '#FFFFFF'

