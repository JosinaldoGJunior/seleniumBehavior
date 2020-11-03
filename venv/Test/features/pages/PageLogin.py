class PageLogin(object):
    def __init__(self, session):
        self.session = session
        self.usuario = ''
        self.senha = ''
        self.url = 'https://srbarriga.herokuapp.com/login'
        self.id_email = 'email'
        self.id_senha = 'senha'
        self.xp_entrar = "//button[@class='btn btn-primary']"

    def open_page(self):
        self.session.get(self.url)

    def realiza_login(self):
        self.session.find_element_by_id(self.id_email).send_keys(self.usuario)
        self.session.find_element_by_id(self.id_senha).send_keys(self.senha)
        self.session.find_element_by_xpath(self.xp_entrar).click()
        return self.session.find_element_by_xpath("//div[@class='alert alert-success']").text