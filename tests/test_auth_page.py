import allure
import pytest
from pages.auth_page import AuthPage
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def tab_is_active(tab_element):
    """ Проверка состояния вкладки """
    return 'rt-tab--active' in tab_element.get_attribute("class")


@pytest.mark.positive
def test_open_authorization_page(web_browser):
    """ Страница авторизации отображается корректно. """

    page = AuthPage(web_browser)
    page.wait_page_loaded()

    with allure.step("Таб ТЕЛЕФОН присутствует"):
        assert page.tab_phone.is_presented()

    with allure.step("Таб ПОЧТА присутствует"):
        assert page.tab_mail.is_presented()

    with allure.step("Таб ЛОГИН присутствует"):
        assert page.tab_login.is_presented()

    with allure.step("Таб ЛИЦЕВОЙ СЧЕТ присутствует"):
        assert page.tab_ls.is_presented()

    with allure.step("Поле ЛОГИН присутствует"):
        assert page.login.is_presented()

    with allure.step("Поле ПАРОЛЬ присутствует"):
        assert page.password.is_presented()

    with allure.step("Кнопка ВОЙТИ присутствует"):
        assert page.btn.is_presented()

    with allure.step("Ссылка ЗАБЫЛ ПАРОЛЬ присутствует"):
        assert page.forgot_password.is_presented()

    with allure.step("Ссылка РЕГИСТРАЦИЯ присутствует"):
        assert page.registration.is_presented()

    with allure.step("Ссылка ПОМОЩЬ присутствует"):
        assert page.help.is_presented()

    with allure.step("По умолчанию активен таб ТЕЛЕФОН"):
        assert tab_is_active(page.tab_phone)



@pytest.mark.positive
def test_authorisation_valid_email_password(web_browser):
    """ Authorisation with valid email and valid password. """

    page = AuthPage(web_browser)
    page.tab_mail.click()
    page.login.send_keys(os.getenv('EMAIL'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step(" Login with valid email and password"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


@pytest.mark.positive
def test_authorisation_valid_phone_password(web_browser):
    """ Authorisation with valid phone and valid password. """

    page = AuthPage(web_browser)
    page.login.send_keys(os.getenv('PHONE'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step(" Login with valid phone and password"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


@pytest.mark.positive
def test_authorisation_valid_ls_password(web_browser):
    """ Authorisation with valid LS and valid password. """

    page = AuthPage(web_browser)
    page.tab_ls.click()
    page.login.send_keys(os.getenv('LS'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step(" Login with valid LS and password"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


@pytest.mark.positive
def test_tab_active(web_browser):
    """ Select tab LS """
    page = AuthPage(web_browser)
    page.tab_ls.click()
    with allure.step("Select tab LS"):
        assert tab_is_active(page.tab_ls)
