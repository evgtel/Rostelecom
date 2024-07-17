from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    # Поле Логин
    login = WebElement(id='username')

    # Поле Пароль
    password = WebElement(id='password')

    # Кнопка Войти
    btn = WebElement(name='login')

    # Вкладка Телефон
    tab_phone = WebElement(id='t-btn-tab-phone')

    # Вкладка Почта
    tab_mail = WebElement(id='t-btn-tab-mail')

    # Вкладка Логин
    tab_login = WebElement(id='t-btn-tab-login')

    # Вкладка Лицевой счет
    tab_ls = WebElement(id='t-btn-tab-ls')

    # Чекбокс Запомнить меня
    checkbox_remember = WebElement(name='rememberMe')

    # Ссылка Забыл пароль
    forgot_password = WebElement(id='forgot_password')

    # Пользовательское соглашение
    agreement = WebElement(id='rt-auth-agreement-link')

    # Способ входа Т-Банк
    oidc_tbank = WebElement(id='oidc_tinkoff')

    # Способ входа Яндекс
    oidc_ya = WebElement(id='oidc_ya')

    # Способ входа ВК
    oidc_vk = WebElement(id='oidc_vk')

    # Способ входа Mail.ru
    oidc_mail = WebElement(id='oidc_mail')

    # Способ входа Однокласники
    oidc_ok = WebElement(id='oidc_ok')

    # Ссылка Зарегистрироваться
    registration = WebElement(id='kc-register')

    # Ссылка Помощь
    help = WebElement(id='faq-open')


