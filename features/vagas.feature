Feature: Consulta vagas
    Consultar vagas por empresa
  @vagas
  Scenario: Consultar vagas nas empresas
      Given que acesso o site da coodesh
      And  cookies aceitos
      When digito email e senha
      |email|password |
      |ema33@email.com|InoarF123$|
      And clico em entrar
      And clico na opção vagas
      And busco vaga por empresa
      |empresa|
      |big|
      Then Verifico resultado
