import allure
import pytest
from .dataset_for_tests import reg_name

from selenium.webdriver.support.ui import WebDriverWait
from pages.reg_page import RegistrationPage
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@allure.feature('Регистрация')
@allure.story('Форма регистрации открывается корректно')
@pytest.mark.positive
def test_open_registration_page(web_browser):
    """ Страница регистрации отображается корректно. """

    page = RegistrationPage(web_browser, url='https://b2c.passport.rt.ru')
    page.wait_page_loaded()
    page.registration.click()
    page.wait_page_loaded()

    with allure.step("Поле Имя присутствует"):
        assert page.name.is_presented()

    with allure.step("Поле Фамилия присутствует"):
        assert page.lastname.is_presented()

    with allure.step("Выпадающий список Регион присутствует"):
        assert page.region_list.is_presented()

    with allure.step("Поле Email присутствует"):
        assert page.email.is_presented()

    with allure.step("Поле Пароль присутствует"):
        assert page.password.is_presented()

    with allure.step("Поле Подтверждение пароля присутствует"):
        assert page.confirm_pass.is_presented()

    with allure.step("Кнопка Зарегистрироваться присутствует"):
        assert page.btn_reg.is_presented()

    with allure.step("Ссылка Пользовательское соглашение присутствует"):
        assert page.agreement.is_presented()

    with allure.step("Ссылка Помощь присутствует"):
        assert page.help.is_presented()

@allure.feature('Регистрация')
@allure.story('Повторная регистрация с валидными данными не происходит')
# @pytest.mark.skip
def test_valid_registration(web_browser):
    page = RegistrationPage(web_browser, url='https://b2c.passport.rt.ru')
    page.wait_page_loaded()
    page.registration.click()

    page.name.is_clickable()

    page.name.send_keys("Евгений")
    page.lastname.send_keys(("Евг"))
    page.region_altayskiy_kray.is_presented()
    page.region_list.click()
    page.email.send_keys('test@test.ru')
    page.password.send_keys('Ps123456')
    page.confirm_pass.send_keys('Ps123456')
    page.btn_reg.click()
    el = page.message_account_already_exist.wait_to_be_clickable()
    assert el.is_displayed()






@pytest.mark.parametrize("name", [reg_name[0][1], reg_name[1][1], reg_name[2][1],
                                  reg_name[3][1], reg_name[4][1], reg_name[5][1], reg_name[6][1]],
                                ids=[reg_name[0][0], reg_name[1][0], reg_name[2][0],
                                    reg_name[3][0], reg_name[4][0], reg_name[5][0], reg_name[6][0]]
                         )
@pytest.mark.negative
@allure.feature('Регистрация')
@allure.story('Верификация имени при регистрации')
@allure.severity("normal")
def test_registration_not_valid_name(web_browser, name):
    """ Регистрация - верификация имени"""

    page = RegistrationPage(web_browser, url='https://b2c.passport.rt.ru')
    page.wait_page_loaded()
    page.registration.click()

    page.name.is_clickable()
    page.name.send_keys(name)
    page.btn_reg.click()
    assert page.message_format_name_err.is_presented()



