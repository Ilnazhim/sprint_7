import allure
import requests
from helpers import validate_schema
from src import urls
from modules import basic_methods
from src.models import Orders


@allure.suite("Тесты проверки получения заказа")
class TestGetOrder:
    @allure.title("Получение списка заказов для конкретного курьера")
    def test_get_list_orders_by_id_courier_success(self):
        courier_id = basic_methods.login_courier_and_return_id()
        with allure.step("Отправка запроса"):
            response = requests.get(urls.URL + urls.ENDPOINT_ORDERS + urls.PARAMS_COURIER_ID + str(courier_id))
        with allure.step("Проверка ожидаемого результата"):
            assert response.status_code == 200
            assert validate_schema(Orders, response.json()['orders'])

    @allure.title("Получение списка всех заказов и проверка контрактов")
    def test_get_all_list_orders(self):
        with allure.step("Отправка запроса"):
            response = requests.get(urls.URL + urls.ENDPOINT_ORDERS)
        with allure.step("Проверка ожидаемого результата"):
            assert response.status_code == 200
            assert validate_schema(Orders, response.json()['orders'])
