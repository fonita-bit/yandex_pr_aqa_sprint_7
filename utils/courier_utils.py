import requests
from data.urls import COURIER_CREATE_URL, COURIER_LOGIN_URL, COURIER_DELETE_URL
from data.courier_data import get_new_courier

def register_new_courier_and_return_login_password():
    courier = get_new_courier()
    response = requests.post(COURIER_CREATE_URL, json=courier)
    if response.status_code == 201:
        return {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["firstName"]
        }
    return {}

def delete_courier(login, password):
    resp = requests.post(COURIER_LOGIN_URL, json={"login": login, "password": password})
    if resp.status_code == 200 and "id" in resp.json():
        courier_id = resp.json()["id"]
        requests.delete(COURIER_DELETE_URL.format(courier_id))
