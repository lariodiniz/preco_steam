# botao.py
---

## Descrição
Arquivo python que contem a classe botao da aplicação **Preços Steam**.
Ele cria a classe `Botao` que herda de `QPushButton`.


### Parametros
```python
        texto: str
        altura: int
        largura_minima: int
        texto_espacamento: int
        texto_cor: str
        icone: str
        icone_cor: str
        botao_cor: str
        botao_hover: str
        botao_pressed: str
        ativo: bool
```

        largura_minima {int} -- largura padrão do botão.
        texto_espacamento {int} -- espaçamento padrão do botão.
        texto_cor {str} -- hexadecimal da cor do botão.
        icone {str} -- caminho para o icone do botão
        icone_cor {str} -- hexadecimal da cor do icone do botão.
        botao_cor {str} -- hexadecimal da cor do botão.
        botao_selecionado {str} -- hexadecimal da cor do botão quando selecionado.
        botao_pressionado {str} -- hexadecimal da cor do botão quando precionado.
        ativo {bool} -- estado do botão.
### Atributos
* `botao.largura_minima` (*int*): largura padrão do botão.
* `botao.texto_espacamento` (*int*): espaçamento padrão do botão.
* `botao.texto_cor` (*str*): hexadecimal da cor do botão.
* `botao.icone` (*str*): caminho para o icone do botão
* `botao.botao_cor` (*str*): hexadecimal da cor do botão.
* `botao.botao_selecionado` (*str*): hexadecimal da cor do botão quando selecionado.


### Métodos

#### Publicos
##### **botao.configura_estilo**
`botao.define_estilo`: configura o estilo do botão.

* Parametros
```python
texto_espacamento: int
texto_cor: str
botao_cor: str
botao_hover: str
botao_pressed: str
```

* Retorno `None`


##### **botao.define_ativar**
`botao.define_ativar`: Ativa ou desativa o botão.

* Parametros
```python
acao: bool
```

* Retorno `None`

##### **botao.paintEvent**
`botao.paintEvent`: Método herdado do QPushButton.

* Retorno `None`

#### Privados

##### **botao.__define_estilo**
`botao.__define_estilo`: Aplica o estilo configurado no botão.

* Retorno `None`


##### **aplicacao.__desenha_icone**
`aplicacao.__desenha_icone`: Desenha o Icone no Botão.

* Parametros
```python
painter_pai: QPainter
retangulo: QRect
```

* Retorno `none`

