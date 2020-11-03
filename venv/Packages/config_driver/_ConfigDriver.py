import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ConfigDriver():
    def __init__(self):
        dir_path = str(os.path.dirname(os.path.realpath(__file__))).replace('\\','/')
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options,
                         executable_path=dir_path + "/drivers/chromedriver.exe")