from pages.auth_page import AuthPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
@pytest.fixture()
def browser():
    options = Options()
    # options.add_argument("--headless=new")
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser


def test_authorisation(browser):

    page = AuthPage(browser)

    page.login.send_keys('test123@yandex.ru')

    # page.password.send_keys("123456")

    # page.btn.click()
    print("")

    # assert page.get_current_url() == 'http://petfriends1.herokuapp.com/all_pets'