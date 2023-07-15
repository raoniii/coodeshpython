Feature: Consulta vagas
    Consultar vagas por empresa

  Scenario: Consultar vagas nas empresas
      Given que acesso o site da coodesh
      And  cookies aceitos
      When digito email e senha
      And clico em entrar
      And clico na opção vagas
      And preencho campo buscar
      And clico no botao buscar
      Then Verifico resultado
