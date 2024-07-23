# РОСТЕЛЕКОМ
# Автотестирование страницы авторизации

Тестирование не предполагалось всеобъемлющим и было направлено на охват основных функций страницы авторизации, а именно:

- Доступность формы авторизации.
- Корректность ссылок.
- Переключение табов выбора способа входа.
- Автоматическая смена табов.
- Авторизация по телефону, почте, лицевому счету.
- Доступность формы восстановления пароля.
- Восстановление пароля по номеру телефона.
- Регистрация пользователя.
- Повторная регистрация пользователя.
- Верификация вводимых данных при различных способах входа.  
- Возможность авторизации через сторонние сервисы.
<!--Запуск тестов-->
# Запуск тестов
Запустить тесты можно двумя способами

## 1. Github Actions

1. Нажать в верхней панели **"Actions"**
2. Слева нажать **"Automated tests for Rostelecom"**
3. Справа нажать **"Run workflow"**
4. Выбрать вариант тестов, нажав  поле **"Выберите тест"**:
   
   - **test_without_real_auth** - будут выполнены все тесты, за исключением тестов, где используются реальные аутентификационные данные, например в тесте авторизации по телефону.
     
   - **test_all** - будут выполнены все тесты.
     
6. (*Опционально*) Можно передать в тесты свой набор данных, заполнив поля:
 - Телефон
 - Email
 - Логин
 - Лицевой счет
 - Пароль
    
    Если какое-то поле не заполнено, то будет передано соответствующее значение из GITHUB_ENV.
   
	***Замечание:** не стоит вводить конфиденциальные данные, так как они будут доступны в логах для просмотра. Если важно тестировать с такими данными, лучше воспользоваться вторым способом "Копирование проекта тестирования".*
   
6. Нажать **"Run workflow"**
	 

### Результаты
После прохождения тестов с подробностями можно ознакомиться двумя способами:
#### 1. Логи workflow
- Нажать ссылку пройденного workflow **"Automated tests for Rostelecom"**.
- Нажать поле **"test"**.
- Раскрыть пункт **"Run all tests"** (или **"Run tests exclude real auth data"**).

#### 2. Отчет Allure-report
- Находясь на странице "Actions" слева нажать **"pages-build-deployment"**.
- Нажать ссылку **"pages build and deployment"**.
- Нажать поле **"deploy"** - откроется веб-страница с отчетом.

Вы можете ознакомиться с результатами уже пройденного ранее запуска тестов сразу перейдя по ссылке https://evgtel.github.io/Rostelecom/79/index.html

# 2. Копирование проекта тестирования
Предполагается, что на компьютере установлен Python версии 3.10 или выше. 
1. Загрузить на компьютер и распаковать zip-архив репозитория (Rostelecom-main.zip)
2. В корне распакованного каталога Rostelecom-main создать файл **.env** и добавить свои данные по образцу:
	EMAIL = 'test@test.ru'
	PHONE = '+79000000000'
	LOGIN = 'user12345'
	LS = '112233445566'
	PASSWORD = 'Password'
3. Открыть терминал, перейтив каталог **Rostelecom-main**
4. Создать виртуальное окружение
	`python -m venv .venv`
5. Активировать виртуальное окружение
	`source .venv/bin/activate (Linux, Mac)`
	`.venv\Scripts\activate (Windows)`
6. Установить зависимости `pip install -r requirements.txt`
7. Запустить тесты:
	`python -m pytest --alluredir allure-results`
8. Запустить формирование отчета Allure-report
	`allure serve allure-results`

		
