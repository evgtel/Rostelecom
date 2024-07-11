from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import WebPage
from pages.elements import WebElement
from pages.locators import AuthLocators

class AuthPage(WebPage):
    def __init__(self, browser, url=''):
        self.browser = browser
        url = 'https://b2c.passport.rt.ru/auth'
        super().__init__(browser, url)

# login = WebElement(id='username')
    def input_username(self, value):
        username = self.browser.find_element(*AuthLocators.AUTH_USERNAME)
        username.send_keys(value)
