import allure
import pytest
import burger_api

@allure.step("Создание шаблонного курьера")
@pytest.fixture(scope='function')
def default_user():
    user_body = burger_api.create_user_body()
    user_response = burger_api.create_user(user_body)
    yield user_response
    access_token = burger_api.get_access_token(user_response)
    burger_api.delete_user(access_token)
