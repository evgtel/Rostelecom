from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import WebPage
from pages.elements import WebElement

options = Options()
# options.add_argument("--headless=new")
chrome_browser = webdriver.Chrome(options=options)

class AuthPage(WebPage):
    def __init__(self, driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth'
        super().__init__(chrome_browser, url)

    login = WebElement(id='username')
    print("")
