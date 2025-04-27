import requests
import allure
import pytest
from data.urls import COURIER_CREATE_URL
from data.courier_data import get_new_courier, COURIER_MISSING_LOGIN, COURIER_MISSING_PASSWORD
from utils.courier_utils import delete_courier

@allure.feature('Курьеры')
class TestCourierCreate:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self):
        courier = get_new_courier()
        resp = requests.post(COURIER_CREATE_URL, json=courier)
        assert resp.status_code == 201
        assert resp.json().get("ok") is True
        delete_courier(courier['login'], courier['password'])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        courier = get_new_courier()
        requests.post(COURIER_CREATE_URL, json=courier)
        resp = requests.post(COURIER_CREATE_URL, json=courier)
        assert resp.status_code == 409
        assert "Этот логин уже используется" in resp.json()["message"]
        delete_courier(courier['login'], courier['password'])

    @allure.title("Ошибка если не передан login")
    def test_create_courier_missing_login(self):
        resp = requests.post(COURIER_CREATE_URL, json=COURIER_MISSING_LOGIN)
        assert resp.status_code == 400
        assert "Недостаточно данных" in resp.json()["message"]

    @allure.title("Ошибка если не передан password")
    def test_create_courier_missing_password(self):
        resp = requests.post(COURIER_CREATE_URL, json=COURIER_MISSING_PASSWORD)
        assert resp.status_code == 400
        assert "Недостаточно данных" in resp.json()["message"]
