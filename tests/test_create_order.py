import allure
import burger_api
import data


class TestCreateOrder:
    @allure.title("Успешное создание заказа авторизованным пользователем с ингридиентами")
    @allure.description("Авторизоваться в системе и создать заказ с бургером")
    def test_create_order_burger_auth_user_success(self, default_burger, default_user_token):
        headers = {"Authorization": default_user_token}
        create_response = burger_api.create_new_order(headers, default_burger)
        assert create_response.status_code == 200 and create_response.json()["order"]["number"] != None

    @allure.title("Ошибка 400 Bad Request при попытке сделать пустой заказ авторизованным пользователем")
    @allure.description(
        "При попытке сделать пустой заказ авторизованным пользователем, Бэкенд возвращает ошибку 400 Bad Request.")
    def test_create_order_without_burger_auth_user_success(self, default_user_token):
        headers = {"Authorization": default_user_token}
        create_response = burger_api.create_new_order(headers, None)
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

    @allure.title("Ошибка 500 Internal Server Error при попытке сделать заказ авторизованным пользователем с невалидным хешем ингредиента")
    @allure.description(
        "При попытке сделать заказ авторизованным пользователем ингридиенты с невалидным хешем, Бэкенд возвращает ошибку 500 Internal Server Error.")
    def test_create_order_auth_user_wrong_hash_fail(self, default_user_token):
        headers = {"Authorization": default_user_token}
        ingredients = data.WRONG_INGREDIENTS
        create_response = burger_api.create_new_order(headers, ingredients)
        assert create_response.status_code == 500

    @allure.title(
        "Ошибка 500 Internal Server Error при попытке сделать заказ неавторизованным пользователем с невалидным хешем ингредиента")
    @allure.description(
        "При попытке сделать заказ неавторизованным пользователем ингридиенты с невалидным хешем, Бэкенд возвращает ошибку 500 Internal Server Error.")
    def test_create_order_not_auth_user_wrong_hash_fail(self):
        ingredients = data.WRONG_INGREDIENTS
        create_response = burger_api.create_new_order(None, ingredients)
        assert create_response.status_code == 500
