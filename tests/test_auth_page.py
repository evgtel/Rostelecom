import allure
import pytest
from pages.auth_page import AuthPage
from .dataset_for_tests import URL_TC
import os
import time
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def tab_is_active(tab_element):
    """ Функция проверки состояния вкладки """
    return 'rt-tab--active' in tab_element.get_attribute("class")


@allure.feature('Авторизация')
@allure.story('Открытие страницы авторизации')
@allure.description('Форма авторизации открывается корректно и содержит элементы для ввода учетных данных')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-001')
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


@allure.feature('Авторизация')
@allure.story('Переключение табов вручную')
@allure.description('Активный таб Телефон переводит поле ввода учетных данных в режим аутентификации по телефонному номеру')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-002')
def test_active_tab_phone(web_browser):
    """ Активирование типа ввода Телефон """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_phone.click()
    with allure.step("Активирование типа ввода Телефон"):
        assert "телефон" in (page.hint_login.get_text()).lower()


@allure.feature('Авторизация')
@allure.story('Переключение табов вручную')
@allure.description('Активный таб Лицевой счет переводит поле ввода учетных данных в режим аутентификации по лицевому счету')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-003')
def test_active_tab_ls(web_browser):
    """ Активирование типа ввода Лицевой счет """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls.click()
    with allure.step("Активирование типа ввода Лицевой счет"):
        assert "лицевой" in (page.hint_login.get_text()).lower()


@allure.feature('Авторизация')
@allure.story('Автоматическая смена таба')
@allure.description('При вводе корректного номера телефона таб аутентификации Логин автоматически меняется на Телефон ')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-004')
def test_automated_change_login_to_phone(web_browser):
    """  Автоматическая смена таба Логин на Телефон """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_login.click()
    page.login.send_keys('+79001112233')
    page.password.click()
    with allure.step("Автоматическая смена таба Логин на Телефон"):
        assert tab_is_active(page.tab_phone)


@allure.feature('Авторизация')
@allure.story('Автоматическая смена таба')
@allure.description('При вводе корректного номера телефона таб аутентификации Лицевой счет автоматически меняется на Телефон')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-005')
def test_automated_change_ls_to_phone(web_browser):
    """  Автоматическая смена таба ЛС на Телефон """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls.click()
    page.login.send_keys('+79001112233')
    page.password.click()
    with allure.step("Автоматическая смена таба Лицевой счет на Телефон"):
        assert tab_is_active(page.tab_phone)


@allure.feature('Авторизация')
@allure.story('Автоматическая смена таба')
@allure.description('При вводе корректного лицевого счета таб аутентификации Телефон автоматически меняется на Лицевой счет')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-006')
def test_automated_change_phone_to_ls(web_browser):
    """  Смена таба Телефон на Лицевой счет """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_phone.click()
    page.login.send_keys('832010111222')
    page.password.click()
    with allure.step("Автоматическая смена таба Телефон на Лицевой счет"):
        assert tab_is_active(page.tab_ls)


@pytest.mark.real_auth
@allure.feature('Авторизация')
@allure.story('Авторизация с валидными данными')
@allure.description('Пользователь может авторизоваться введя валидные телефон и пароль')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-007')
def test_authorisation_valid_phone_password(web_browser):
    """ Authorisation with valid phone and valid password. """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.login.send_keys(os.getenv('PHONE'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с валидными телефоном и паролем"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


@pytest.mark.real_auth
@allure.feature('Авторизация')
@allure.story('Авторизация с валидными данными')
@allure.description('Пользователь может авторизоваться введя валидные электронную почту и пароль')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-008')
def test_authorisation_valid_email_password(web_browser):
    """ Authorisation with valid email and valid password. """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_mail.click()
    page.login.send_keys(os.getenv('EMAIL'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с валидными почтой и паролем"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


@pytest.mark.real_auth
@allure.feature('Авторизация')
@allure.story('Авторизация с валидными данными')
@allure.description('Пользователь может авторизоваться введя валидные лицевой счет и пароль')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-009')
def test_authorisation_valid_ls_password(web_browser):
    """ Authorisation with valid LS and valid password. """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls.click()
    page.login.send_keys(os.getenv('LS'))
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с валидными лицевым счетом и паролем"):
        assert 'b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


@allure.feature('Авторизация')
@allure.story('Форма восстановления пароля')
@allure.description('Форма восстановления пароля открывается корректно и содержит элементы для ввода учетных данных ')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-010')
def test_tab_active(web_browser):
    """ Форма восстановления пароля отображается корректно. """
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
@allure.story('Авторизация с невалидными учетными данными')
@allure.description('Пользователь не сможет авторизоваться с номером телефона и паролем не прошедшим регистрацию')
@pytest.mark.negative
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-014')
def test_auth_wrong_phone(web_browser):
    """ Авторизация с неверным номером телефона """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.login.send_keys('+79000000000')
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с неверным номером телефона"):
        assert page.login_pass_error.is_presented()


@allure.feature('Авторизация')
@allure.story('Авторизация с невалидными учетными данными')
@allure.description('Пользователь не сможет авторизоваться введя невалидный лицевой счет')
@pytest.mark.negative
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-015')
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
@allure.story('Верификация ввода в поле Почта при авторизации')
@allure.description('Поле Почта не принимает пустое значение')
@pytest.mark.negative
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-016')
def test_authorisation_empty_email(web_browser):
    """ Авторизация с незаполненным полем Почта """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_mail.click()
    page.login.send_keys('')
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с незаполненным полем Почта"):
        assert page.mail_not_corresponded.is_presented()


@allure.feature('Авторизация')
@allure.story('Верификация ввода в поле Почта при авторизации')
@allure.description('Поле почта не принимает не разрешенные спецсимволы')
@pytest.mark.negative
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-017')
def test_authorisation_invalid_email(web_browser):
    """ Авторизация с некорректной почтой (спецсимволы)"""

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_mail.click()
    page.login.send_keys('#@mail.ru')
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с некорректной почтой"):
        assert not page.login_pass_error.is_presented()  # не должно быть сообщения "Неверный логин или пароль"


@allure.feature('Авторизация')
@allure.story('Верификация ввода в поле Лицевой счет при авторизации')
@allure.description('Пользователь не сможет авторизоваться оставив поле Лицевой счет пустым')
@pytest.mark.negative
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-018')
def test_authorisation_empty_ls(web_browser):
    """ Авторизация с незаполненным полем Лицевой счет """

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls.click()
    page.password.send_keys(os.getenv('PASSWORD'))
    page.btn.click()
    with allure.step("Авторизация с незаполненным полем Лицевой счет"):
        assert page.msg_enter_ls.is_presented()


@pytest.mark.negative
@allure.feature('Авторизация')
@allure.story('Верификация ввода в поле Лицевой счет при авторизации')
@allure.description('Пользователь не сможет авторизоваться введя в поле Лицевой счет значение меньше 12 цифр')
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-019')
def test_authorisation_small_ls(web_browser):
    """ Авторизация с полем Лицевой счет меньше 12 цифр"""

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls. click()
    page.login.send_keys('11111111111')
    page.password.click()
    with allure.step("Авторизация с полем Лицевой счет меньше 12 цифр"):
        assert page.msg_check_ls.is_presented()


@pytest.mark.negative
@allure.severity("normal")
@allure.feature('Авторизация')
@allure.story('Верификация ввода в поле Лицевой счет при авторизации')
@allure.description('Поле Лицевой счет не принимает значение больше 12 цифр')
@allure.testcase(URL_TC, 'TC-RT-AUTH-020')
def test_authorisation_big_ls(web_browser):
    """ Авторизация с полем Лицевой счет больше 12 цифр"""

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls. click()
    page.login.send_keys('1111222233334444')
    page.password.click()
    with allure.step("Авторизация с полем Лицевой счет больше 12 цифр"):
        assert page.login_text.get_attribute('value') == '111122223333'


@pytest.mark.negative
@allure.severity("normal")
@allure.feature('Авторизация')
@allure.story('Верификация ввода в поле Лицевой счет при авторизации')
@allure.description('Поле Лицевой счет не принимает латинские буквы')
@allure.testcase(URL_TC, 'TC-RT-AUTH-021')
def test_authorisation_latin_ls(web_browser):
    """ Авторизация латинские буквы в поле Лицевой счет"""

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_ls. click()
    page.login.send_keys('aaaabbbbcccc')
    page.password.click()
    with allure.step("Авторизация латинские буквы в поле Лицевой счет"):
        assert not page.login_text.get_attribute('value')  # OK если поле пустое


@allure.feature('Авторизация')
@allure.story('Возможность авторизации через соцсети')
@allure.description('Пользователь может перейти по ссылке для  авторизации через Т-Банк')
@pytest.mark.positive
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-029')
def test_ref_tbank(web_browser):
    """ Ссылка на Т-Банк корректна """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.oidc_tbank.click()
    with allure.step("Ссылка на Т-Банк корректна"):
        assert 'id.tinkoff.ru/auth/step' in page.get_current_url()


@allure.feature('Авторизация')
@allure.story('Возможность авторизации через соцсети')
@allure.description('Пользователь может перейти по ссылке для  авторизации через Яндекс')
@pytest.mark.positive
@pytest.mark.xfail
@allure.severity("normal")
@allure.testcase(URL_TC, 'TC-RT-AUTH-030')
def test_ref_yandex(web_browser):
    """ Ссылка на Яндекс корректна """
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    success = False
    for i in range(1, 3):
        if page.oidc_ya.is_presented():
            page.oidc_ya.click()
            time.sleep(5)
            if 'oauth.yandex.ru' in page.get_current_url():
                success = True
                break
    with allure.step("Ссылка на Яндекс корректна"):
        assert success
