
from pages.auth_page import AuthPage
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def test_authorisation_valid_email_password(web_browser):
    """ Authorisation with valid email and password. """

    page = AuthPage(web_browser)
    page.login.send_keys(os.getenv('EMAIL'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_authorisation_valid_phone_password(web_browser):
    """ Authorisation with valid phone and password. """

    page = AuthPage(web_browser)
    page.login.send_keys(os.getenv('PHONE'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_authorisation_valid_uid_password(web_browser):
    """ Authorisation with valid ls and password. """

    page = AuthPage(web_browser)
    page.login.send_keys(os.getenv('LS'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()