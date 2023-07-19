Feature: Cadastro e verificacao
    Cadastra uma nova conta e valida campos do formulario.

    @cadastro
    Scenario: Criar nova conta developer
        Given que acesso url
        When os cookies são aceitos
        And clico no botao criar conta
        And preencho os dados da nova conta
        |full_name|email|password |
        |Inoar  F1|ema33@email.com|InoarF123$|
        And clico para aceitar os termos
        And clico no botão inscrever-se
        Then verifico se login foi realizado

    @cadastrocompleto
    Scenario: Criar nova conta developer completa
        Given que acesso url
        When os cookies são aceitos
        And clico no botao criar conta
        And preencho os dados da nova conta
        |full_name|email|password|
        |Stephanie Welch|9stephanie300666@example.com|Stephanie123$|
        And clico para aceitar os termos
        And clico no botão inscrever-se
        And verifico se login foi realizado
        And seleciono carreira Front-End Developer
        And seleciono habilidades
        And indico experiencia com tech
        And indico momento profissional
        And preencho campos whatssapp, cidade de residencia
        |whatsapp|cidade|
        |11999999999|poa|
        And seleciono preferencia de vaga
        And clico em proximo
        And preencho campos camunidades, causas sociais,
        And preencho raça/cor, ident genero, orient sexual, deficiencia
        And verifico se pagina do scorecard foi exibida
        And clico no botao proximo
        And indico conhecimentos
        And clico proximo
        And indico conhecimentos parte 2
        And clico proximo
        And indico conhecimentos parte 3
        and clico para avançar
        And indico conhecimentos parte 4
        And clico em enviar
        And clico em concluir

        


  
