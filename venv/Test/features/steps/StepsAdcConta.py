from behave import given, when, then, step
from Test.features.pages.PagesAdcContas import PagesAdcContas

@then(u'navego ate a tela de adiconar contas')
def step_impl(context):
    context.obj_contas = PagesAdcContas(context.obj_driver)
    context.obj_contas.to_contas()


@when(u'salvo a conta "{conta}"')
def step_impl(context,conta):
    context.var_notific_conta = context.obj_contas.adc_conta(str(conta).strip())


@then(u'sou notificado com a mensagem "{mensagem}"')
def step_impl(context,mensagem):
    assert context.var_notific_conta == mensagem, \
        'Erro de assert {} != {}'.format(mensagem, context.var_notific_conta)