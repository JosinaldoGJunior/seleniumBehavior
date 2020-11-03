from behave import given, when, then, step
from Test.features.pages.PageLogin import PageLogin

@given(u'que estou acessando a aplicacao')
def step_impl(context):
    context.obj_login = PageLogin(context.obj_driver)
    context.obj_login.open_page()

@when(u'informo o usuario "{usuario}"')
def step_impl(context,usuario):
    context.obj_login.usuario = usuario


@when(u'informo a senha "{senha}"')
def step_impl(context,senha):
    context.obj_login.senha = senha


@when(u'clico no entrar')
def step_impl(context):
    context.var_login_sucess = context.obj_login.realiza_login()


@then(u'visualize uma pagina com a mensagem "{mensagem}"')
def step_impl(context,mensagem):
    assert context.var_login_sucess == mensagem, \
        'Erro de assert {} != {}'.format(mensagem,context.var_login_sucess)