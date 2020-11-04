#language: pt

Funcionalidade: Validar Login
  Como um usuario
  Gostaria de realizar login com sucesso

  Contexto:
      Dado que estou acessando a aplicacao

  @testeLogin
  Cenario: Login com sucesso
      Quando informo o usuario "leonardolive10@gmail.com"
      E informo a senha "47894789"
      E clico no entrar
      Entao visualize uma pagina com a mensagem "Bem vindo, leonardo!"

  @testeLogin
  Cenario: Login invalido
      Quando informo o usuario "email_errado@gmail.com"
      E informo a senha "47894789"
      E clico no entrar
      Entao visualize uma pagina com a mensagem "Problemas com o login do usuário"