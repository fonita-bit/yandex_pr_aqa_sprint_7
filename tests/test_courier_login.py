import requests
import allure
import pytest
from data.urls import COURIER_LOGIN_URL
from utils.courier_utils import register_new_courier_and_return_login_password

@allure.feature('Курьеры')
class TestCourierLogin:

    @allure.title("Курьер может авторизоваться")
    def test_login_success(self, courier_credentials):
        creds = courier_credentials
        resp = requests.post(COURIER_LOGIN_URL, json={
            "login": creds['login'],
            "password": creds['password']
        })
        assert resp.status_code == 200
        assert "id" in resp.json() and resp.json()["id"] > 0

    @allure.title("Ошибка если не передан login")
    def test_login_missing_login(self):
        payload = {"password": "password_only"}
        resp = requests.post(COURIER_LOGIN_URL, json=payload)
        assert resp.status_code == 400
        assert "Недостаточно данных" in resp.json()["message"]

    @allure.title("Ошибка если не передан password")
    def test_login_missing_password(self):
        payload = {"login": "login_only"}
        resp = requests.post(COURIER_LOGIN_URL, json=payload)
        assert resp.status_code == 400
        assert "Недостаточно данных" in resp.json()["message"]

    @allure.title("Ошибка при неправильных логине или пароле")
    def test_login_wrong_credentials(self):
        resp = requests.post(COURIER_LOGIN_URL, json={
            "login": "no_user",
            "password": "no_pass"
        })
        assert resp.status_code == 404
        assert "Учетная запись не найдена" in resp.json()["message"]

    @allure.title("Ошибка для несуществующего пользователя")
    def test_login_nonexistent_user(self):
        resp = requests.post(COURIER_LOGIN_URL, json={
            "login": "fakeuser12345",
            "password": "fakepass54321"
        })
        assert resp.status_code == 404
        assert "Учетная запись не найдена" in resp.json()["message"]

    @allure.title("Успешный логин возвращает id")
    def test_login_returns_id(self, courier_credentials):
        creds = courier_credentials
        resp = requests.post(COURIER_LOGIN_URL, json={
            "login": creds['login'],
            "password": creds['password']
        })
        assert "id" in resp.json() and resp.json()["id"] > 0
