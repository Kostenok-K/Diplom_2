import allure
import pytest
import requests
from data import *
import random


def generate_unique_email():
    email = f'user{random.randint(100, 999)}@gmail.com'
    return email


@allure.suite('Изменение данных пользователя в системе')
class TestChangeUserData:

    @allure.title('Проверка успешного изменения почты пользователя')
    @allure.description('Тест успешного изменения почты пользователя')
    @pytest.mark.parametrize('new_email', [generate_unique_email()])
    def test_change_user_email(self, auth_token, registered_user, new_email):
        headers = {"Authorization": auth_token}
        response_1 = requests.patch(URL.USER_URL, headers=headers, data={'email': new_email})
        assert response_1.status_code == 200 and response_1.json().get('success') == Answers.TRUE_ANSWER
        response_2 = requests.get(URL.USER_URL, headers=headers)
        assert response_2.status_code == 200
        response_data = response_2.json()
        user_data = response_data.get('user', {})
        assert user_data.get('email') == new_email

    @allure.title('Проверка изменения пароля пользователя')
    @allure.description('Тест изменения пароля пользователя')
    @pytest.mark.parametrize('new_password', ['newpassword_1'])
    def test_change_user_password(self, auth_token, new_password, registered_user):
        headers = {"Authorization": auth_token}
        response_1 = requests.patch(URL.USER_URL, headers=headers, data={'password': new_password})
        assert response_1.status_code == 200
        assert response_1.json().get('success') == Answers.TRUE_ANSWER

    @allure.title('Проверка изменения почты и пароля пользователя')
    @allure.description('Тест изменения почты и пароля пользователя')
    @pytest.mark.parametrize('new_email, new_password', [(generate_unique_email(), 'newpassword')])
    def test_change_user_email_and_password(self, new_email, new_password, registered_user, auth_token):
        headers = {"Authorization": auth_token}
        response_1 = requests.patch(URL.USER_URL, headers=headers, data={'email': new_email, 'password': new_password})
        assert response_1.status_code == 200
        assert response_1.json().get('success') == Answers.TRUE_ANSWER

        response_2 = requests.get(URL.USER_URL, headers=headers)
        assert response_2.status_code == 200
        response_data = response_2.json()
        user_data = response_data.get('user', {})
        assert user_data.get('email') == new_email

    @allure.title('Проверка изменения данных пользователя в системе без авторизации')
    @allure.description('Тест зменения данных пользователя в системе без авторизации')
    def test_change_user_data_without_auth(self):
        response = requests.patch(URL.USER_URL)
        assert response.status_code == 401 and response.json().get('message') == Answers.UNAUTHORISED_ANSWER

    @allure.title('Проверка изменения данных пользователя при передаче существующей почты')
    @allure.description('Тест изменения данных пользователя при передаче существующей почты')
    def test_change_user_data_with_exist_email(self, registered_user, auth_token):
        headers = {"Authorization": auth_token}
        payload = {"email": 'kkos@yandex.ru'}
        response = requests.patch(URL.USER_URL, headers=headers, json=payload)
        assert response.status_code == 403 and response.json().get('message') == Answers.UPDATE_EXIST_EMAIL_ANSWER
