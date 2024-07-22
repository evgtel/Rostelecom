from pages.base import WebPage
from pages.elements import WebElement
from selenium.webdriver.common.by import By


class RegistrationPage(WebPage):
    def __init__(self, web_driver, url=''):
        # url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
        # url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    # Ссылка Зарегистрироваться со страницы Авторизация
    registration = WebElement(id='kc-register')

    # Поле Имя
    name = WebElement(name='firstName')

    # Поле Фамилия
    lastname = WebElement(name='lastName')

    # Выпадающий список Регион
    region_list = WebElement(class_name='rt-input__action')

    # Поле Email
    email = WebElement(id='address')

    # Поле Пароль
    password = WebElement(id='password')

    # Поле Подтверждение пароля
    confirm_pass = WebElement(id='password-confirm')

    # Кнопка Зарегистрироваться
    btn_reg = WebElement(name='register')

    # Ссылка Пользовательское соглашение
    agreement = WebElement(id='rt-auth-agreement-link')

    # Ссылка Помощь
    help = WebElement(id='faq-open')

    # Динамическое сообщение "Небходимо заполнить поле кириллицей 2-30 символов"
    message_format_name_err = WebElement(xpath="//span[@class='rt-input-container__meta rt-input-container__meta--error']")

    # Динамический элемент выпадающего списка регионов
    region_altayskiy_kray = WebElement(xpath="//div[@class='rt-select__list-item'][3]")

    # Всплывающее окно Учетная запись уже существует
    message_account_already_exist = WebElement(xpath="//button[@name='gotoLogin']")
