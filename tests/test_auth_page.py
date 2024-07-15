
from pages.auth_page import AuthPage
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def test_authorisation(web_browser):
    """ Authorisation with valid login and password. """
    # print(os.getenv('TEST'))
    page = AuthPage(web_browser)

    page.login.send_keys(os.getenv('EMAIL'))

    page.password.send_keys(os.getenv('PASSWORD'))
    # page.password.send_keys('t6E2azxc')

    page.btn.click()

    assert "mail.ru" in os.getenv('EMAIL')
    # assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()
