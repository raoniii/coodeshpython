# Q.A. Challenge 20211029

Este é um desafio de automação de teste para a posição de Q.A. Esta é a implementação de um sistema de teste automatizado usando o framework Selenium e a linguagem Python.

**Status do Desafio**
- Obrigatório 1: ✅ Concluído>
- Obrigatório 2: Descontinuado>
- Obrigatório 3: ✅ Concluído>
- Obrigatório 4: ✅ Em Progressso>
- Obrigatório 5: ✅ Concluído>
- Diferencial 1: Não Realizado

## Sobre o Projeto

O projeto consiste em testar a funcionalidade de um aplicativo web. O objetivo é garantir que as principais funcionalidades estejam funcionando corretamente por meio de testes automatizados.

Site para automatização:
[Beta Coodesh](https://beta.coodesh.com/)

## Tecnologias Utilizadas

- Python
- Selenium

# Q.A. Challenge 20211029

## Processo de compreensão do desafio

### Framework: Selenium

A escolha pelo selenium foi pela familiaridade mas é um framework muito versátil tanto na questão de sistema operacional quanto na utilização de diversos navegadores.

A linguagem Python possui uma sintaxe de facil compreenssão facilitando no desenvolvimento de toda  a automação, além de possuir diversas bases de conhecimentos na web.

Durante o processo de desenvolvimento a falta de padrão na identificação dos campos implicou na resolução do desafio.


## Pré-requisitos

:warning: [Python](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)

:warning: [Selenium](https://pypi.org/project/selenium/)

:warning: [Chromedriver](https://chromedriver.chromium.org/downloads)

:warning: [behave](https://behave.readthedocs.io/en/latest/install/)

## Como rodar a aplicação

```
git clone <https://github.com/raoniii/coodeshpython.git>

```


Acesse o diretorio do projeto via terminal/cmd:

```
cd coodeshpython

```

Para execução de todas as features utilze o comando

```
behave

```
Para execução de features individualmente utilize o seguinte comando respectivamente para home_page, cadastro e vagas

```
behave .\features\home_page.feature --tags=homepage
behave .\features\cadastro.feature --tags=cadastro
behave .\features\cadastro.feature --tags=cadastrocompleto
behave .\features\vagas.feature --tags=vagas

```


## Progresso do Desafio

**Obrigatório 1: Carregamento correto da página inicial**
- [x] Verificar se a home page está sendo carregada corretamente

**Obrigatório 2: Navegar pela página de login no menu superior**
- [] Navegar pela página de login no menu superior

**Obrigatório 3: Criar uma conta para o perfil de pessoas candidatas**
- [x] Cria uma nova conta com perfil desenvolvedor

**Obrigatório 4: Testar os formulários de preenchimento do perfil**
- [ ] Completa o cadastro de uma nova conta até o final

**Obrigatório 5: Buscar por uma empresa com vagas**
- [x] Realiza a buscar de vagas por nome da empresa 

**Diferencial: Testes com redes sociais**
- [ ] Realiza o cadastro de uma nova conta utilizando redes sociais
