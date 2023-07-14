Feature: Carregamento da Home Page
    Verificar se a home page é carregada corretamente

    Scenario: Carregar a Home Page com sucesso
        Given que acesso a url
        When os cookies são aceitos
        Then vejo o conteúdo da home page
