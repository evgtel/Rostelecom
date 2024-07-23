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
    btn = WebElement(id='kc-login')

    # Вкладка Телефон
    tab_phone = WebElement(id='t-btn-tab-phone')

    # Подсказка в поле Телефон,Почта, Логин, Лицевой счет
    hint_login = WebElement(class_name='rt-input__placeholder')

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



    # Изображене Капча
    image_captcha = WebElement(class_name='rt-captcha__image')

    # Поле ввода Капча
    input_captcha= WebElement(id='captcha')

    # Кнопка Продолжить
    btn_reset = WebElement(id='reset')

    # Кнопка Вернуться назад
    btn_back = WebElement(id='reset-back')

    # Сообщение неверный логин или пароль
    login_pass_error = WebElement(id='form-error-message')

    # Введите адрес указанный при регистрации
    mail_not_corresponded = WebElement(id='username-meta')

    # Введите номер лицевого счета
    msg_enter_ls = WebElement(id='username-meta')

    # Проверьте номер лицевого счета
    msg_check_ls = WebElement(id='username-meta')

    # Скрытый текст поля Логин
    login_text = WebElement(xpath="//input[@type='hidden' and @name='username']")
    # login_text = WebElement(xpath="//input[@wfd-id='id2']")