class PagesAdcContas(object):

    def __init__(self, session):
        self.session = session
        self.id_contas = 'Contas'
        self.id_adicionar = 'Adicionar'
        self.id_nome = 'nome'
        self.xp_btn_salvar = "//button[@class='btn btn-primary']"
        self.xp_alert = "//div[contains(@class , 'alert')]"

    def to_contas(self):
        self.session.find_element_by_link_text(self.id_contas).click()
        self.session.find_element_by_link_text(self.id_adicionar).click()

    def adc_conta(self,conta):
        self.session.find_element_by_id(self.id_nome).send_keys(conta)
        self.session.find_element_by_xpath(self.xp_btn_salvar).click()
        return self.session.find_element_by_xpath(self.xp_alert).text
