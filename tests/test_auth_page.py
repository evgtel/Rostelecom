import allure
import pytest
from pages.auth_page import AuthPage
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def tab_is_active(tab_element):
    """ Функция проверки состояния вкладки """
    return 'rt-tab--active' in tab_element.get_attribute("class")


@allure.feature('Авторизация')
@pytest.mark.positive
def test_open_authorization_page(web_browser):
    """ Страница авторизации отображается корректно. """

    page = AuthPage(web_browser)
    page.wait_page_loaded()

    allure.testcase('', 'TC-RT-AUTH-001')

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

@allure.feature('Авторизация')
@pytest.mark.positive
def test_active_tab_phone(web_browser):
    """ Активирование типа ввода Телефон """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_phone.click()
    allure.testcase('', 'TC-RT-AUTH-002')
    with allure.step("Активирование типа ввода Телефон"):
        assert "телефон" in (page.hint_login.get_text()).lower()

@allure.feature('Авторизация')
@pytest.mark.positive
def test_active_tab_ls(web_browser):
    """ Активирование типа ввода Лицевой счет """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls.click()
    allure.testcase('', 'TC-RT-AUTH-003')
    with allure.step("Активирование типа ввода Лицевой счет"):
        assert "лицевой" in (page.hint_login.get_text()).lower()

@allure.feature('Авторизация')
@pytest.mark.positive
def test_automated_change_login_to_phone(web_browser):
    """   """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_login.click()
    page.login.send_keys('+79001112233')
    page.password.click()
    allure.testcase('', 'TC-RT-AUTH-004')
    with allure.step("Автоматическая смена таба Логин на Телефон"):
        assert tab_is_active(page.tab_phone)

@allure.feature('Авторизация')
@pytest.mark.positive
def test_automated_change_ls_to_phone(web_browser):
    """   """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls.click()
    page.login.send_keys('+79001112233')
    page.password.click()
    allure.testcase('', 'TC-RT-AUTH-005')
    with allure.step("Автоматическая смена таба Лицевой счет на Телефон"):
        assert tab_is_active(page.tab_phone)


@allure.feature('Авторизация')
@pytest.mark.positive
def test_automated_change_phone_to_ls(web_browser):
    """   """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_phone.click()
    page.login.send_keys('832010111222')
    page.password.click()
    allure.testcase('', 'TC-RT-AUTH-006')
    with allure.step("Автоматическая смена таба Телефон на Лицевой счет"):
        assert tab_is_active(page.tab_ls)


@allure.feature('Авторизация')
@pytest.mark.positive
@pytest.mark.skip
def test_authorisation_valid_phone_password(web_browser):
    """ Authorisation with valid phone and valid password. """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.login.send_keys(os.getenv('PHONE'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    allure.testcase('', 'TC-RT-AUTH-007')
    with allure.step("Авторизация с валидными телефоном и паролем"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


@allure.feature('Авторизация')
@pytest.mark.positive
@pytest.mark.skip
def test_authorisation_valid_email_password(web_browser):
    """ Authorisation with valid email and valid password. """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_mail.click()
    page.login.send_keys(os.getenv('EMAIL'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    allure.testcase('', 'TC-RT-AUTH-008')
    with allure.step("Авторизация с валидными почтой и паролем"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()

@allure.feature('Авторизация')
@pytest.mark.positive
@pytest.mark.skip
def test_authorisation_valid_ls_password(web_browser):
    """ Authorisation with valid LS and valid password. """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls.click()
    page.login.send_keys(os.getenv('LS'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    allure.testcase('', 'TC-RT-AUTH-009')
    with allure.step("Авторизация с валидными лицевым счетом и паролем"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


@allure.feature('Авторизация')
@allure.testcase('','TC-RT-AUTH-010')
@pytest.mark.positive
def test_tab_active(web_browser):
    """ Форма восстановления пароля отображается корректно """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.forgot_password.click()
    with allure.step("Присутствует таб Телефон"):
        assert page.tab_phone.is_presented()
    with allure.step("Таб Телефон активен по умолчанию"):
        assert tab_is_active(page.tab_phone)
    with allure.step("Присутствует таб Почта"):
        assert page.tab_mail.is_presented()
    with allure.step("Присутствует таб Логин"):
        assert page.tab_login.is_presented()
    with allure.step("Присутствует таб Лицевой счет"):
        assert page.tab_ls.is_presented()
    with allure.step("Присутствует поле ввода учетных данных"):
        assert page.login.is_presented()
    with allure.step("Присутствует изображение Капча"):
        assert page.image_captcha.is_presented()
    with allure.step("Присутствует поле ввода Капча"):
        assert page.input_captcha.is_presented()
    with allure.step("Присутствует кнопка Продолжить"):
        assert page.btn_reset.is_presented()
    with allure.step("Присутствует кнопка Вернуться назад"):
        assert page.btn_back.is_presented()
    with allure.step("Присутствует ссылка Помощь"):
        assert page.help.is_presented()


@allure.feature('Авторизация')
@allure.testcase('','TC-RT-AUTH-014')
@pytest.mark.positive
def test_auth_wrong_phone(web_browser):
    """ Авторизация с неверным номером телефона """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.login.send_keys('+79000000000')
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с неверным номером телефона"):
        assert page.login_pass_error.is_presented()

allure.feature('Авторизация')
@allure.testcase('','TC-RT-AUTH-015')
@pytest.mark.positive
def test_auth_wrong_ls(web_browser):
    """ Авторизация с неверным лицевым счетом """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls.click()
    page.login.send_keys('000000000000')
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с неверным лицевым счетом"):
        assert page.login_pass_error.is_presented()

@allure.feature('Авторизация')
@pytest.mark.positive
@allure.testcase('', 'TC-RT-AUTH-016')
def test_authorisation_invalid_email(web_browser):
    """ Авторизация с некорректной почтой """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_mail.click()
    page.login.send_keys(os.getenv(''))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с некорректной почтой"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()