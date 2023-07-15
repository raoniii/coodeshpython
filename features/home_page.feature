Feature: Carregamento da Home Page
    Verificar se a home page é carregada corretamente

    @homepage
    Scenario: Carregar a Home Page com sucesso
        Given que acesso a url
        When aceito os cookies
        Then vejo o conteúdo da home page
