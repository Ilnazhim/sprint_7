import allure
from modules import basic_methods
import requests
from src import urls, assert_text


@allure.suite("Тесты проверки авторизации курьера")
class TestLoginCourier:

    @allure.title("Проверка успешной авторизации и в ответе приходит id курьера")
    def test_login_courier_get_id_success(self):
        data = {
            "login": 'ilnazhim',
            "password": 'sprint_7'
        }
        with allure.step("Отправка запроса"):
            response = requests.post(urls.URL + urls.ENDPOINT_COURIER_LOGIN, data=data)
        with allure.step("Проверка ожидаемого результата"):
            assert response.status_code == 200
            assert response.json()['id'] is not None

    @allure.title("Проверка что несуществующий курьер не может авторизоваться")
    def test_login_courier_wrong_login_success(self):
        data = basic_methods.return_login_password()
        with allure.step("Отправка запроса"):
            response = requests.post(urls.URL + urls.ENDPOINT_COURIER_LOGIN, data=data)
        with allure.step("Проверка ожидаемого результата"):
            assert response.status_code == 404
            assert response.json()['message'] == assert_text.ASSERT_USER_NOT_FOUND

    @allure.title("Получение ошибки при попытке авторизоваться с неверным логином и паролем")
    def test_login_courier_wrong_password_success(self):
        data = {
            "login": 'ilnazhim',
            "password": 'sprint_7_wrong'
        }
        with allure.step("Отправка запроса"):
            response = requests.post(urls.URL + urls.ENDPOINT_COURIER_LOGIN, data=data)
        with allure.step("Проверка ожидаемого результата"):
            assert response.status_code == 404
            assert response.json()['message'] == assert_text.ASSERT_USER_NOT_FOUND

    @allure.title("Получение ошибки при попытке авторизоваться без логина")
    def test_login_courier_empty_login_success(self):
        data = {
            "password": 'sprint_7_wrong'
        }
        with allure.step("Отправка запроса"):
            response = requests.post(urls.URL + urls.ENDPOINT_COURIER_LOGIN, data=data)
        with allure.step("Проверка ожидаемого результата"):
            assert response.status_code == 400
            assert response.json()['message'] == assert_text.ASSERT_FEW_DATA_LOGIN

    @allure.title("Получение ошибки при попытке авторизоваться без поля с паролем")
    def test_login_courier_empty_password_success(self):
        data = {
            "login": 'ilnazhim'
        }
        with allure.step("Отправка запроса"):
            response = requests.post(urls.URL + urls.ENDPOINT_COURIER_LOGIN, data=data)
        with allure.step("Проверка ожидаемого результата"):
            assert response.status_code == 504
            assert response.text == 'Service unavailable'
