import allure
import requests
from data import *


@allure.suite('Создание заказа')
class TestCreateOrder:

    @allure.title('Проверка создания заказа  с авторизацией')
    @allure.description('Тест создания заказа с авторизацией')
    def test_create_order_with_auth(self, registered_user, valid_hash):
        payload_user = registered_user
        requests.post(URL.LOGIN_URL, data=payload_user)
        payload_hash = valid_hash
        response = requests.post(URL.ORDER_URL, data=payload_hash)
        assert response.status_code == 200 and response.json().get('success') == Answers.TRUE_ANSWER

    # Тест падает,так как по документации только авторизованный пользоваетль может оформить заказ
    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Тест создания заказа без авторизации')
    def test_create_order_without_auth(self, valid_hash):
        payload = valid_hash
        response = requests.post(URL.ORDER_URL, data=payload)
        print(response.json().get('success'))
        assert response.status_code == 401 and response.json().get('success') == Answers.UNAUTHORISED_ANSWER

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Тест создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        response = requests.post(URL.ORDER_URL)
        assert response.status_code == 400 and response.json().get('message') == Answers.NO_INGREDIENTS_ANSWER

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    @allure.description('Тест создания заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_hash(self, valid_hash):
        payload = valid_hash
        payload['ingredients'] += '1'
        response = requests.post(URL.ORDER_URL, data=payload)
        assert response.status_code == 500
