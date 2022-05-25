# Como Contribuir
---
Este é o passo a passo para contribuir neste projeto. Ele será o mais didático possível.

Estamos utilizando o [Poetry](https://python-poetry.org) como gerenciador de ambiente de projeto e o passo a passo explicará como fazer o desenvolvimento utilizando o mesmo, mas você pode usar o que melhor lê convir.

## Preparando o Ambiente de Desenvolvimento

1. Instale o Git na sua maquina. (*Para mais informações sobre o git veja [Git](https://git-scm.com/docs)*)

2. Instale o Python na sua maquina. (*Para mais informações sobre o python veja [Python](https://www.python.org)*)

3. Instale o Poetry na sua maquina. (*Para mais informações sobre o poetry veja [Poetry](https://python-poetry.org)*)

4. Log com a sua conta no github e acesse o **[reposiótio do projeto](https://github.com/lariodiniz/preco_steam)**

5. Faça um fork do repositório principal do projeto para criar um repositório na sua conta do github.

6. Clone o repositório do projeto na sua conta do github para a sua maquina 
    
    *Nota: Substitua **[SEU USUARIO]** pelo seu usuario do github*
```
git clone https://github.com/[SEU USUARIO]/preco-steam.git
```

7. Acesse a pasta do projeto que foi clonada na sua maquina.

8. Crie a maquina virtual com o poetry e instale as dependências.
```
poetry install
```

9. Execute a aplicação.
```
poetry run python main.py
```

## Desenvolvendo
Esse passo a passo de desenvolvimento explica o que é necessario fazer para que seu pull request seja aceito.

1. Leia o guia de [contribuição](https://github.com/lariodiniz/preco_steam/blob/master/CONTRIBUTING.md).

2. Crie um branch para a funcionalidade/correção que você vai desenvolver;
    
    *Nota: Substitua **[NOMEDOBRANCH]** pelo nome que você vai dar ao branch*
```
git checkout -b [NOMEDOBRANCH]
```

3. Documente no MKdocs a funcionalidade/correção que você esta desenvolvendo.

4. Faça o teste da funcionalidade/correção que você esta desenvolvendo.

5. Faça a funcionalidade/correção que você esta desenvolvendo.

    *Nota: todo código python neste projeto esta sendo desenvolvido em **português pt-br** sem acento, siga esse padrão!*

6. Execute o **[isort](https://pycqa.github.io/isort/)** para padronizar a inportação do código.
```
poetry run isort .
```

7. Execute o **[Blue](https://blue.readthedocs.io/en/latest/)** para padronizar o código.
```
poetry run blue .
```

8. Execute o **[pytest](https://docs.pytest.org/en/7.1.x/)** para confirmar que o código esta correto.
```
poetry run pytest -v
```

9. Com o trecho do código desenvolvido, padronizado e testado, faça um commit descrevendo o que você fez exatamente.

10. Repita os passos 4 a 10 quantas vezes forem necessarias para finalizar a funcionalidade/correção.

11. Com a funcionalidade/correção finalizada faça um push do branch para o repositório clonado na sua conta do github;


## Enviando sua modificação para o projeto
1. Solicite um Pull Request da sua modificação para o projeto principal. Não esqueça de dar um título e uma descrição que descreve exatamente o que você esta fazendo e proponto.