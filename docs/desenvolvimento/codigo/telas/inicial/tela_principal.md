# tela_inicial.py
---

## Descrição
arquivo python que contem a classe da tela inicial da aplicação **Preços Steam**.
Ele cria a classe `TelaInicial` que herda de `object`, esta classe é responsavel por criar a janela inicial da aplicação.

### Atributos
* `aplicacao.pasta_raiz` (*str*): caminho para a pasta raiz do projeto.
* `aplicacao.pasta_imgs` (*str*): caminho para a pasta de imagens projeto.
* `aplicacao.pasta_icones` (*str*): caminho para a pasta de icones projeto.

### Métodos

#### Publicos
##### **aplicacao.busca_imagem**
`aplicacao.busca_imagem`: retorna o caminho correto da imagem informada que esta no diretorio.

* Parametros
```python
pasta:str
imagem:str
```

* Retorno `str`

#### Privados
##### **aplicacao.__definePastas**
`aplicacao.__definePastas`: cria os atributos `pasta_raiz`, `pasta_imgs` e `pasta_icones` na classe.

* Retorno `none`

##### **aplicacao.__defineTitulo**
`aplicacao.__defineTitulo`: retorna o título da aplicação.

* Retorno `str`