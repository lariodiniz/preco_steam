# aplicacao.py
---

## Descrição
arquivo python que contem a classe principal da aplicação **Preços Steam**.
Ele cria a classe `Aplicacao` que herda de `QMainWindow`, esta classe é responsavel por criar a janela principal da aplicação e todas as outras.

### Atributos
* `aplicacao.area_principal` (*QFrame*): Frame da area principal.
* `aplicacao.barra_inferior` (*QFrame*): Frame da barra do inferior da area principal.
* `aplicacao.barra_inferior_label_direita` (*QLabel*): Label direito da barra_inferior.
* `aplicacao.barra_inferior_label_esquerda` (*QLabel*): Label esquerdo da barra_inferior.
* `aplicacao.barra_topo` (*QFrame*): Frame da barra do topo da area principal.
* `aplicacao.barra_topo_label_esquerdo` (*QLabel*): Label esquedo da barra_topo.
* `aplicacao.barra_topo_label_direito` (*QLabel*): Label direito da barra_topo.
* `aplicacao.janelas` (*QStackedWidget*): Area das janelas da aplicação.
* `aplicacao.layout_principal` (*QFrame*): Frame da janela inteira.
* `aplicacao.menu_esquerdo` (*QFrame*): Frame do menu da esquerda.
* `aplicacao.pasta_icones` (*str*): string contento caminho para a pasta de icones projeto.
* `aplicacao.pasta_imgs` (*str*): string contento caminho para a pasta de imagens projeto.
* `aplicacao.pasta_raiz` (*str*): string contento caminho para a pasta raiz do projeto.
* `aplicacao.versao` (*str*): string contento a versão do sistema.

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

##### **aplicacao.__defineAreaPrincipal**
`aplicacao.__defineAreaPrincipal`: configura a area principal da aplicação.

* Retorno `none`


##### **aplicacao.__defineLayout**
`aplicacao.__defineLayout`: configura o layout inicial da aplicação.

* Retorno `none`

##### **aplicacao.__defineMenuEsquerdo**
`aplicacao.__defineMenuEsquerdo`: configura o menu esquerdo da aplicação.

* Retorno `none`

##### **aplicacao.__definePastas**
`aplicacao.__definePastas`: cria os atributos `pasta_raiz`, `pasta_imgs` e `pasta_icones` na classe.

* Retorno `none`

##### **aplicacao.__defineTitulo**
`aplicacao.__defineTitulo`: retorna o título da aplicação.

* Retorno `str`

##### **aplicacao.__defineVersao**
`aplicacao.__defineVersao`: retorna a versão da aplicação.

* Retorno `str`