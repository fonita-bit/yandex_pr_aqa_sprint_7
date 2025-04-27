import string
import random

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def get_new_courier():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

COURIER_MISSING_LOGIN = {
    "password": generate_random_string(),
    "firstName": generate_random_string()
}
COURIER_MISSING_PASSWORD = {
    "login": generate_random_string(),
    "firstName": generate_random_string()
}
