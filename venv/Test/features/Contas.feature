#language: pt

Funcionalidade: Cadastro de contas
	Como um usuario
	Gostaria de cadastrar contas
	Para que eu possa distribuir meu dinheiro de uma forma mais organizada

  Contexto:
      Dado que estou acessando a aplicacao
      Quando informo o usuario "leonardolive10@gmail.com"
      E informo a senha "47894789"
      E clico no entrar
      Entao visualize uma pagina com a mensagem "Bem vindo, leonardo!"
      E navego ate a tela de adiconar contas

  @testeCadastro
  Cenario: Nao deve inserir uma conta com nome ja existente
      Quando salvo a conta "leonardo josedys"
      Então sou notificado com a mensagem "Já existe uma conta com esse nome!"

  @testeCadastro
  Cenario: Nao deve inserir uma conta sem nome
      Quando salvo a conta " "
      Entao sou notificado com a mensagem "Informe o nome da conta"