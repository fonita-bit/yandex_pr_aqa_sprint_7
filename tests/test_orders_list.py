import requests
import allure
from data.urls import ORDERS_LIST_URL

@allure.feature('Заказы')
class TestOrdersList:

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        resp = requests.get(ORDERS_LIST_URL)
        assert resp.status_code == 200
        assert "orders" in resp.json()
        assert isinstance(resp.json()["orders"], list)
