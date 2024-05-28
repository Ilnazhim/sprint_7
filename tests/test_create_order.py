import allure
import pytest
import requests
from src import urls, data_payload

ENDPOINT = '/orders'


@allure.title("Создание заказа с самокатами разных цветов")
@pytest.mark.parametrize('color', [data_payload.create_order_black, data_payload.create_order_grey,
                                   data_payload.create_order_grey_and_black,
                                   data_payload.create_order_empty_color])
def test_create_order_success(color):

    data = color
    with allure.step("Отправка запроса"):
        response = requests.post(urls.URL + ENDPOINT, json=data)
    with allure.step("Проверка ожидаемого результата"):
        assert response.status_code == 201
        assert response.json()['track'] is not None
