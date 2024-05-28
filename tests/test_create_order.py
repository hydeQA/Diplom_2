import allure
import burger_api


class TestCreateOrder:
    @allure.title("Успешное создание заказа авторизованным пользователем с ингридиентами")
    @allure.description("Авторизоваться в системе и создать заказ с бургером")
    def test_create_order_burger_auth_user_success(self, default_burger):
        body = burger_api.create_user_body()
        user_response = burger_api.create_user(body)
        access_token = burger_api.get_access_token(user_response)
        headers = {"Authorization": access_token}
        create_response = burger_api.create_new_order(headers, default_burger)
        burger_api.delete_user(access_token)
        assert create_response.status_code == 200 and create_response.json()["order"]["number"] != None

    @allure.title("Ошибка 400 Bad Request при попытке сделать пустой заказ авторизованным пользователем")
    @allure.description(
        "При попытке сделать пустой заказ авторизованным пользователем, Бэкенд возвращает ошибку 400 Bad Request.")
    def test_create_order_without_burger_auth_user_success(self):
        body = burger_api.create_user_body()
        user_response = burger_api.create_user(body)
        access_token = burger_api.get_access_token(user_response)
        headers = {"Authorization": access_token}
        create_response = burger_api.create_new_order(headers, None)
        burger_api.delete_user(access_token)
        assert create_response.status_code == 400 and create_response.json()["message"] == "Ingredient ids must be provided"


    @allure.title("Ошибка 401 Unauthorized при попытке сделать заказ бургера неавторизованным пользователем")
    @allure.description(
        "Неавторизованный пользователь не может сделать заказ бургера. Бэкенд возвращает ошибку 401 Unauthorized.")
    def test_create_order_burger_not_auth_user_success(self, default_burger):
        create_response = burger_api.create_new_order(None, default_burger)
        assert create_response.status_code == 401


    @allure.title("Ошибка 400 Bad Request при попытке сделать пустой заказ неавторизованным пользователем")
    @allure.description(
        "При попытке сделать пустой заказ неавторизованным пользователем, Бэкенд возвращает ошибку 400 Bad Request.")
    def test_create_order_without_burger_not_auth_user_success(self):
        create_response = burger_api.create_new_order(None, None)
        assert create_response.status_code == 400 and create_response.json()["message"] == "Ingredient ids must be provided"
