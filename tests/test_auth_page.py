import allure

from pages.auth_page import AuthPage
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def tab_is_active(tab_element):
    """ Проверка состояния вкладки """
    return 'rt-tab--active' in tab_element.get_attribute("class")


def test_authorisation_valid_email_password(web_browser):
    """ Authorisation with valid email and valid password. """

    page = AuthPage(web_browser)
    page.login.send_keys(os.getenv('EMAIL'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step(" Login with valid email and password"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_authorisation_valid_phone_password(web_browser):
    """ Authorisation with valid phone and valid password. """

    page = AuthPage(web_browser)
    page.login.send_keys(os.getenv('PHONE'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_authorisation_valid_ls_password(web_browser):
    """ Authorisation with valid LS and valid password. """

    page = AuthPage(web_browser)
    page.tab_ls.click()
    page.login.send_keys(os.getenv('LS'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_tab_active(web_browser):
    """  """

    page = AuthPage(web_browser)
    page.tab_ls.click()
    assert tab_is_active(page.tab_ls)
