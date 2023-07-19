from behave import given, when, then

from features.pages.VagasPage import VagasPage

@given(u'que acesso o site da coodesh')
def step_impl(context):
    context.vagaspage = VagasPage(context.driver)

@given(u'cookies aceitos')
def step_impl(context):
    context.vagaspage.click_on_ok_button()

@when(u'digito email e senha')
def step_impl(context):
    for row in context.table:
        email = row["email"]
        password = row["password"]
        context.vagaspage.enter_email_login(email)
        context.vagaspage.enter_password_login(password)


@when(u'clico em entrar')
def step_impl(context):
    context.vagaspage.click_on_entrar_button()


@when(u'clico na opção vagas')
def step_impl(context):
    context.vagaspage.click_on_vagas_button()


@when(u'busco vaga por empresa')
def step_impl(context):
    for row in context.table:
        empresa = row["empresa"]
        context.vagaspage.enter_search_company(empresa)



@then(u'Verifico resultado')
def step_impl(context):
    ...