import allure
import pytest
import requests
import helper
import burger_api
import urls


@allure.step("Создание шаблонного курьера")
@pytest.fixture(scope='function')
def default_user():
    body = helper.new_user_login_password()
    user_response = burger_api.create_user(body)
    yield user_response
    access_token = requests.post(urls.BASE_URL + urls.CREATE_USER_ENDPOINT, json=body).json().get("accessToken")
    headers = {"Authorization": access_token}
    requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers=headers)
