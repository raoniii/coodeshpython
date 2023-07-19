from behave import given, when, then

from features.pages.CadastroPage import CadastroPage


@given(u'que acesso url')
def step_impl(context):
   context.cadastropage = CadastroPage(context.driver)

@when(u'os cookies são aceitos')
def step_impl(context):
    context.cadastropage.click_on_ok_button()


@when(u'clico no botao criar conta')
def step_impl(context):
    context.cadastropage.click_on_nova_conta_button()


@when(u'preencho os dados da nova conta')
def step_impl(context):
   for row in context.table:
        full_name = row["full_name"]
        email = row["email"]
        password = row["password"]
        context.cadastropage.enter_full_name(full_name)
        context.cadastropage.enter_email(email)
        context.cadastropage.enter_password(password)

@when(u'clico para aceitar os termos')
def step_impl(context):
    context.cadastropage.click_on_li_aceito()


@when(u'clico no botão inscrever-se')
def step_impl(context):
    context.cadastropage.click_on_inscreva()


@then(u'verifico se login foi realizado')
def step_impl(context):
    assert context.cadastropage.check_display_onboarding_text("Onboarding")

#################################################
#                                               #
#       DAQUI PRA BAIXO CADASTROCOMPLETO        #
#                                               #
#################################################

@when(u'verifico se login foi realizado')
def step_impl(context):
    assert context.cadastropage.check_display_onboarding_text("Onboarding")

@when(u'seleciono carreira Front-End Developer')
def step_impl(context):
    context.cadastropage.click_on_career()


@when(u'seleciono habilidades')
def step_impl(context):
    context.cadastropage.enter_habilidade()


@when(u'indico experiencia com tech')
def step_impl(context):
    context.cadastropage.click_on_exptech()


@when(u'indico momento profissional')
def step_impl(context):
    ...


@when(u'preencho campos whatssapp, cidade de residencia')
def step_impl(context):
    ...


@when(u'seleciono preferencia de vaga')
def step_impl(context):
    ...


@when(u'clico em proximo')
def step_impl(context):
    ...


@when(u'preencho campos camunidades, causas sociais,')
def step_impl(context):
    ...


@when(u'preencho raça/cor, ident genero, orient sexual, deficiencia')
def step_impl(context):
    ...


@when(u'verifico se pagina do scorecard foi exibida')
def step_impl(context):
    ...


@when(u'clico no botao proximo')
def step_impl(context):
    ...


@when(u'indico conhecimentos')
def step_impl(context):
    ...

@when(u'clico proximo')
def step_impl(context):
    ...


@when(u'indico conhecimentos parte 2')
def step_impl(context):
    ...


@when(u'indico conhecimentos parte 3')
def step_impl(context):
    ...


@when(u'clico para avançar')
def step_impl(context):
    ...


@when(u'indico conhecimentos parte 4')
def step_impl(context):
    ...


@when(u'clico em enviar')
def step_impl(context):
    ...


@when(u'clico em concluir')
def step_impl(context):
    ...