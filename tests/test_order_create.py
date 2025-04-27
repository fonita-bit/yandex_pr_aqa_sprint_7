import requests
import allure
import pytest
from data.urls import ORDER_CREATE_URL
from data.order_data import ORDER_BASE, ORDER_COLORS

@allure.feature('Заказы')
class TestOrderCreate:

    @allure.title("Создание заказа с разными цветами")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_create_order_with_colors(self, colors):
        data = ORDER_BASE.copy()
        if colors is not None:
            data["color"] = colors
        resp = requests.post(ORDER_CREATE_URL, json=data)
        assert resp.status_code == 201
        assert "track" in resp.json() and resp.json()["track"] > 0
