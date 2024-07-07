import pytest
import requests
import helpers
from data import *


@pytest.fixture
def valid_hash():
    payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
    return payload


@pytest.fixture
def registered_user():
    email, password, name = helpers.register_new_user_and_return_email_password()
    payload = {
        'email': f'{email}@mail.com',
        'password': password
    }
    yield payload
    response = requests.post(URL.LOGIN_URL, data=payload)
    token = response.json().get("accessToken")
    headers = {"Authorization": token}
    requests.delete(URL.DELETE_USER_URL, headers=headers)


@pytest.fixture
def auth_token(registered_user):
    payload = registered_user
    response = requests.post(URL.LOGIN_URL, data=payload)
    token = response.json().get("accessToken")
    yield token


@pytest.fixture
def unregistered_user():
    email, password, name = helpers.generate_unregistered_user()
    payload = {
        'email': f'{email}@mail.com',
        'password': password,
        'name': name
    }
    yield payload
    del payload['name']
    response = requests.post(URL.LOGIN_URL, data=payload)
    token = response.json().get("accessToken")
    headers = {"Authorization": token}
    requests.delete(URL.DELETE_USER_URL, headers=headers)
