Feature: Cadastro e verificacao
    Cadastra uma nova conta e valida campos do formulario.

    @cadastro
    Scenario: Criar nova conta developer
        Given que acesso url
        When os cookies são aceitos
        And clico no botao criar conta
        And preencho os dados da nova conta
        And clico para aceitar os termos
        And clico no botão inscrever-se
        Then verifico se login foi realizado

  
