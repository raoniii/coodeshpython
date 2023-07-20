Feature: Cadastro e verificacao
    Cadastra uma nova conta e valida campos do formulario.
    
    @cadastro
    Scenario: Criar nova conta developer
        Given que acesso url
        When os cookies são aceitos
        And clico no botao criar conta
        And preencho os dados da nova conta
        |full_name|email|password |
        |Inoar  F1|troy999@email.com|InoarF123$|
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
        |Stephanie Welch|troy999@example.com|Stephanie123$|
        And clico para aceitar os termos
        And clico no botão inscrever-se
        And verifico se login foi realizado
        And seleciono carreira Front-End Developer
        And seleciono habilidades
        And indico experiencia com tech
        And indico momento profissional
        And preencho campos whatssapp, cidade de residencia
        |whatsapp|city|
        |11999999999|poa|
        And seleciono preferencia de vaga
        And clico em proximo
        And preencho campo camunidades
        And preencho campo relacao com comunidade
        And preencho causas sociais
        |causas|
        |Saúde|
        And preencho raça/cor
        And preencho ident genero
        And preencho orient sexual
        And preencho deficiencia
        And clico para avancar
        And verifico se pagina do scorecard foi exibida
        And clico no botao proximo
        And indico conhecimentos
        And clico proximo
        And indico conhecimentos parte 2
        And clico proximo pt2
        And indico conhecimentos parte 3
        And clico em enviar
        And clico em concluir

        


  
