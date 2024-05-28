import random
import string
import requests
from src import urls


def return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


def login_courier_and_return_id():
    ENDPOINT = '/courier/login'
    data = {
        "login": 'ilnazhim',
        "password": 'sprint_7'
    }
    response = requests.post(urls.URL + ENDPOINT, data=data)
    assert response.status_code == 200
    return response.json()['id']
