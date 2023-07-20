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
    #context.cadastropage.click_on_exptech


@when(u'preencho campos whatssapp, cidade de residencia')
def step_impl(context):
    for row in context.table:
        whatsapp = row["whatsapp"]
        city = row["city"]
        context.cadastropage.enter_whatsapp(whatsapp)
        context.cadastropage.enter_city(city)


@when(u'seleciono preferencia de vaga')
def step_impl(context):
    context.cadastropage.click_on_integral_checkbox()
    

@when(u'clico em proximo')
def step_impl(context):
    context.cadastropage.click_proximo_button()


@when(u'preencho campo camunidades')
def step_impl(context):
    context.cadastropage.click_on_comunidades()

@when(u'preencho campo relacao com comunidade')
def step_impl(context):
    context.cadastropage.click_on_relacao_comunidades()


@when(u'preencho causas sociais')
def step_impl(context):
    for row in context.table:
        causas = row["causas"]
        context.cadastropage.click_on_causas_sociais(causas)


@when(u'preencho raça/cor')
def step_impl(context):
    context.cadastropage.click_on_raca_cor()

@when(u'preencho ident genero')
def step_impl(context):
    context.cadastropage.click_on_genero()


@when(u'preencho orient sexual')
def step_impl(context):
    context.cadastropage.click_on_orientacao_sexual()

@when(u'preencho deficiencia')
def step_impl(context):
    context.cadastropage.click_on_deficiencia()

@when(u'clico para avancar')
def step_impl(context):
    context.cadastropage.click_proximo_button2()


@when(u'verifico se pagina do scorecard foi exibida')
def step_impl(context):
    assert context.cadastropage.check_display_scorecard_text("Scorecard")


@when(u'clico no botao proximo')
def step_impl(context):
    context.cadastropage.click_proximo_responder()


@when(u'indico conhecimentos')
def step_impl(context):
    context.cadastropage.preencher_scorecard1()

@when(u'clico proximo')
def step_impl(context):
    context.cadastropage.click_proximo_button3()


@when(u'indico conhecimentos parte 2')
def step_impl(context):
    context.cadastropage.preencher_scorecard2()

@when(u'clico proximo pt2')
def step_impl(context):
    context.cadastropage.click_proximo_button4()


@when(u'indico conhecimentos parte 3')
def step_impl(context):
    context.cadastropage.preencher_scorecard3()


@when(u'clico em enviar')
def step_impl(context):
    context.cadastropage.click_enviar()


@when(u'clico em concluir')
def step_impl(context):
   context.cadastropage.click_concluir()