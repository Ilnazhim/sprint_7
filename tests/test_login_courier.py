import allure

from modules import basic_methods
import requests
from src import urls

ENDPOINT = '/courier/login'


@allure.title("Успешный логин курьера")
def test_login_courier_status_200_success():
    data = {
        "login": 'ilnazhim',
        "password": 'sprint_7'
    }
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 200


@allure.title("Проверка что в ответе приходит id курьера")
def test_login_courier_get_id_success():
    data = {
        "login": 'ilnazhim',
        "password": 'sprint_7'
    }
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 200
        assert response.json()['id'] is not None


@allure.title("Проверка что несуществующий курьер не может авторизоваться")
def test_login_courier_wrong_login_success():
    data = basic_methods.return_login_password()
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"


@allure.title("Получение ошибки при попытке авторизоваться с неверным логином и паролем")
def test_login_courier_wrong_password_success():
    data = {
        "login": 'ilnazhim',
        "password": 'sprint_7_wrong'
    }
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"


def test_login_courier_empty_login_success():
    data = {
        "password": 'sprint_7_wrong'
    }
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"


def test_login_courier_empty_password_success():
    data = {
        "login": 'ilnazhim'
    }
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, data=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 504