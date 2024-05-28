import allure

import helper
import burger_api
import pytest


class TestChangeUserData:
    @allure.title("Проверка успешного изменения данных авторизованного пользователя")
    @allure.description("Авторизованным пользователем успешно редактируем данные для авторизации: email, name, password")
    @pytest.mark.parametrize("key, value",
                             [
                                 ("email", "fedor123@mail.ru"),
                                 ("name", "Fedor Kruzenshtern"),
                                 ("password", "654321")
                             ])
    def test_change_auth_user_data_success(self, key, value):
        user_data = burger_api.create_user_body()
        burger_api.create_user(user_data)
        body_data = user_data.copy()
        body_data.pop("name", None)
        login_response = burger_api.login_user(body_data)
        access_token = burger_api.get_access_token(login_response)
        body_data[key] = value
        change_response = burger_api.change_user_data(access_token, body_data)
        burger_api.delete_user(access_token)
        assert change_response.status_code == 200 and change_response.json()["success"] == True

