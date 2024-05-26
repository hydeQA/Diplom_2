import allure
import burger_api
from helper import ChangeTestDataHelper
import pytest


class TestCreateUser:
    @allure.title("Проверка успешной регистрации пользователя")
    @allure.description("Создание пользователя. Проверка статуса ответа и тела ответа")
    def test_create_user_success(self, default_user):
        create_user_request = default_user
        assert create_user_request.status_code == 200 and create_user_request.json() is not None

    @allure.title("Проверка создания дубликата пользователя")
    @allure.description("Создание дубликата пользователя. Проверка статуса ответа и тела ответа")
    def test_duplicate_user_fail(self):
        body = burger_api.create_user_body()
        user_response = burger_api.create_user(body)
        create_duplicate_request = burger_api.create_user(body)
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert create_duplicate_request.status_code == 403 and create_duplicate_request.json()[
            "message"] == "User already exists"

    @allure.title("Проверка ошибки при создании пользователя без одного из обязательных полей: email")
    @allure.description("Отправить запрос на создание пользователя без обязательного поля и плучить ошибку 403")
    @pytest.mark.parametrize('key, value',
                             [
                                 ("email", ""),
                                 ("password", ""),
                                 ("name", "")
                             ])
    def test_create_user_without_field_fail(self, key, value):
        body = ChangeTestDataHelper.modify_create_user_body(key, value)
        user_response = burger_api.create_user(body)
        assert user_response.status_code == 403 and user_response.json()["message"] == "Email, password and name are required fields"
