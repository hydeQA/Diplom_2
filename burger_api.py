import allure
import urls
import requests


@allure.step("Создание пользователя в приложении Stellar burger")
def create_user(body):
    return requests.post(urls.BASE_URL+urls.CREATE_USER_ENDPOINT, json=body)
