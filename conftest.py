import pytest
from utils.courier_utils import register_new_courier_and_return_login_password, delete_courier

@pytest.fixture
def courier_credentials():
    creds = register_new_courier_and_return_login_password()
    yield creds
    if creds:
        delete_courier(creds['login'], creds['password'])
