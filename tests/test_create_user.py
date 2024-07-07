import allure
import pytest
import requests
import helpers
from data import *


@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.title('Проверка создания уникального пользователя')
    @allure.description('Тест создания уникального пользователя')
    def test_create_user(self, unregistered_user):
        payload = unregistered_user
        response = requests.post(URL.REGISTER_URL, data=payload)
        assert response.status_code == 200 and response.json().get('success') == Answers.TRUE_ANSWER

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    @allure.description('Тест создания пользователя, который уже зарегистрирован')
    def test_create_same_user(self, unregistered_user):
        payload = unregistered_user
        requests.post(URL.REGISTER_URL, data=payload)
        response = requests.post(URL.REGISTER_URL, data=payload)
        assert response.status_code == 403 and response.json().get('message') == Answers.DUPLICATE_USER_ANSWER

    @allure.title('Проверка обязательных полей при создании пользователя')
    @allure.description('Тест обязательных полей при создании пользователя')
    @pytest.mark.parametrize('missing_field', ['email', 'password'])
    def test_required_fields(self, missing_field):
        email, password, name = helpers.generate_unregistered_user()
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        del payload[missing_field]
        response = requests.post(URL.REGISTER_URL, data=payload)
        assert response.status_code == 403 and response.json().get('message') == Answers.REQUIRED_FIELD_ANSWER
