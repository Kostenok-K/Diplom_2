import allure
import pytest
import requests
from data import *


@allure.suite('Логин пользователя в системе')
class TestLoginUser:

    @allure.title('Проверка входа под существующим пользователем')
    @allure.description('Тест входа под существующим пользователем')
    def test_login_user(self, registered_user):
        payload = registered_user
        response = requests.post(URL.LOGIN_URL, data=payload)
        assert response.status_code == 200 and response.json().get('success') == Answers.TRUE_ANSWER

    @allure.title('Проверка авторизации с неверными данными')
    @allure.description('Тест авторизации с неверными данными')
    @pytest.mark.parametrize('invalid_field', ['email', 'password'])
    def test_login_user_with_invalid_data(self, registered_user, invalid_field):
        payload = registered_user.copy()
        payload[invalid_field] += '_'
        response = requests.post(URL.LOGIN_URL, data=payload)
        assert response.status_code == 401 and response.json().get('message') == Answers.INCORRECT_ANSWER
