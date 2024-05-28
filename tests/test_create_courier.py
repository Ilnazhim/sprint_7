import allure
from modules import basic_methods
import requests
from src import urls

ENDPOINT = '/courier'


@allure.title("Успешное создание курьера со всеми полями")
def test_create_courier_with_random_login_status_201():

    data = basic_methods.return_login_password()
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 201


@allure.title("Получение ошибки при создании одинакового курьера")
def test_create_courier_with_same_name_and_login_error_success():
    data = {
        "login": 'ilnazhim',
        "password": 'sprint_7',
        "firstName": 'Пупкин'
    }
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."


@allure.title("Ошибка при создании курьера без пароля")
def test_create_courier_not_all_fields_is_fill_error_success():

    data = {
        "login": 'Test0009',
    }
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'


@allure.title("Успешное создание курьера со всеми полями")
def test_create_courier_with_with_random_login_content_ok():

    data = basic_methods.return_login_password()
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.content.decode() == '{"ok":true}'


@allure.title("Ошибка при создании курьера с существующим логином")
def test_create_courier_with_same_login_and_other_name_success():
    data = {
        "login": 'Илья',
        "password": 'sprint_7',
        "firstName": 'Васечкин'
    }
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."
