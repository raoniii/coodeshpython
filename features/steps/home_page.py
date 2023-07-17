from behave import given, when, then

from features.pages.HomePage import HomePage


@Given(u'que acesso a url')
def step_impl(context):
    context.homepage = HomePage(context.driver)

@when(u'aceito os cookies')
def step_impl(context):
    context.homepage.click_on_ok_button()
 
@then(u'vejo o conteudo da home page')
def step_impl(context):
    assert context.homepage.check_display_login_text("Faça login")