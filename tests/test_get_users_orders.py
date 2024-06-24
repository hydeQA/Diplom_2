import allure
import burger_api
import data


class TestGetUsersOrders:
    @allure.title("Успешное получение списка заказов авторизованного пользователя")
    @allure.description("Проверка успешного получения cписка заказов авторизованного пользователя")
    def test_get_orders_auth_users_success(self, default_user, default_burger):
        user_response, access_token = default_user
        headers = {"Authorization": access_token}
        ingredients = default_burger
        burger_api.create_new_order(headers, ingredients)
        burger_api.create_new_order(headers, ingredients)
        user_orders = burger_api.get_users_orders(headers)
        assert user_orders.status_code == 200
        assert user_orders.json()["orders"][0] != None
        assert user_orders.json()["orders"][1] != None

    @allure.title("Ошибка 401 при полученит списка заказов неавторизованным пользователем")
    @allure.description("Проверка возвращения ошибки 401 Unauthorized при попытке получения "
                        "cписка заказов неавторизованным пользователем")
    def test_get_order_list_not_auth_user_fail(self, default_burger):
        ingredients = default_burger
        burger_api.create_new_order(None, ingredients)
        burger_api.create_new_order(None, ingredients)
        orders_response = burger_api.get_users_orders(None)
        assert orders_response.status_code == 401
        assert orders_response.json()["message"] == data.MESSAGE_NOT_CHANGE
