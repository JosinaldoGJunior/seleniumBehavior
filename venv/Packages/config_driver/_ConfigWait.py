from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class ConfigWait(object):
    def __init__(self,session,time):
        self.wait = WebDriverWait(session, time)

    def waitVisibilityLocated(self, locator, element):
        self.wait.until(ec.visibility_of_element_located(
            (self.switchLocator(locator),element)))

    def switchLocator(self, by):
        if by == "id":
            return By.ID
        elif by == "xpath":
            return By.XPATH
        else:
            raise ValueError("locator invalid")
