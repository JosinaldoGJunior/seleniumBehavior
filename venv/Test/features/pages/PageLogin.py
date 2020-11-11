from Packages.config_driver._ConfigWait import ConfigWait

class PageLogin(ConfigWait):

    def __init__(self, session):
        super(PageLogin, self).__init__(session,30)
        self.session = session
        self.usuario = ''
        self.senha = ''
        self.url = 'https://srbarriga.herokuapp.com/login'
        self.id_email = 'email'
        self.id_senha = 'senha'
        self.xp_entrar = "//button[@class='btn btn-primary']"
        self.xp_alert = "//div[contains(@class , 'alert')]"

    def open_page(self):
        self.session.get(self.url)
        self.waitVisibilityLocated("css", self.id_email)

    def realiza_login(self):
        self.session.find_element_by_id(self.id_email).send_keys(self.usuario)
        self.session.find_element_by_id(self.id_senha).send_keys(self.senha)
        self.session.find_element_by_xpath(self.xp_entrar).click()
        return self.session.find_element_by_xpath(self.xp_alert).text