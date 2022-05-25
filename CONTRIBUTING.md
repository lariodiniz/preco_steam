# Guia de Contribuição

## Antes de Contribuir

Bem vindo ao projeto [Preco Steam](https://github.com/lariodiniz/preco_steam)! Caso você nunca tenha contribuido para um projeto temos um passo a passo no nosso site de documentação de [como fazer a sua contribuição](https://lariodiniz.github.io/preco_steam/desenvolvimento/contribuir/), não esqueça de dar uma olhada!

## Contribuindo

### Contribuidor

Estamos muito felizes por você querer nos ajudar com o projeto **Preco Steam**! Nosso projeto é simples e tem como objetivo ajudar jogadores de todo o mundo a poupar seu dinheiro na hora de comprar jogos. Mas antes de contribuir, lembre-se:

- Faça seu código, não plageie! Caso use algum trecho de código da internet, deixe um comenario informando de onde você consegiu ele.

- Seu trabalho será distribuido sob a licença [MIT](LICENSE.md) assim que seu pull request for mesclado.

- Contribuições para a nossa documentação também é muito bem vinda!

### Contribuição

Agradecemos qualquer contribuição que você queira fazer, mas é importante que você leia essa seção com atenção para que seu trabalho seja aceito quando você fizer seu pull request!

Sua contribuição será testa e analizada antes de ser aceita, por favor utilize o isort, o blue e o pytest para verificar a sua contribuição antes de envia-la para você ter certeza de que tudo correrá corretamente.

Quando você estiver enviando alguma correção de um problema listado na area de Issues do github, adicione [ISSUE_NUMERO] no título do pull request para podermos identificar.

#### Guia de Estilo

* Escreva em Python 3.9+.
* Arquivos, classes, metodos, atributos, funções e variaveis com nomes intuitivos e em português brasileiro sem utilizar acentos.
* Use comentarios e docstrings para explicar o que você esta fazendo.
* Não use nome de variaveis de uma unica letra.
* Não use siglas nos nomes, descreva o que aquela classe, metodo, atributo, funçõe ou variavel faz.
* Siga o padrão de nomeclatura Python descrito na PEP8; nome de arquivos, metodos, atributos, funções e variaveis em sneak_case e lower_case, CONSTANTES em UPPERCASE, NomeDeClasses em CamelCase, etc..
* Se você usou algum trecho de código da internet, deixe um comenario informando de onde você consegiu ele com a URL.
* Documente no mkdocs tudo que você criar/corrigir/modificar.
* Escreva testes de tudo que você fizer.
* O Uso de **type hints** do Python é recomentado, mas não obrigatório.
* Se você usar alguma biblioteca de terceiros que não esteja no _requirements.txt__, adicione-o por favor.
* As extenções dos arquivos de código devem ser `.py`.
* Siga os padrões de pastas *dentro* existentes no projeto.
* Todos os envios serão testados e analizados utilizando o pytest, o isort e o blue.
* E o mais importate, obrigado por contribuir, sinta-se a vontade para entrar em contato para tirar qualquer duvida.