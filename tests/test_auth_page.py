import pytest
from pages.auth_page import AuthPage


def test_authorisation(web_browser):
    """ Authorisation with valid login and password. """

    page = AuthPage(web_browser)

    page.login.send_keys('t_eugen@mail.ru')

    page.password.send_keys("t6E2azxc")

    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()
