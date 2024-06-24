import allure
import pytest
import burger_api

@allure.step("Создать шаблонного курьера")
@pytest.fixture(scope='function')
def default_user():
    user_body = burger_api.create_user_body()
    user_response = burger_api.create_user(user_body)
    access_token = burger_api.get_access_token(user_response)
    yield user_response, access_token
    burger_api.delete_user(access_token)


@allure.step("Создать бургер из имеющихся ингридиентов")
@pytest.fixture(scope='function')
def default_burger():
    ingredients = burger_api.get_ingredients().json()
    ingredient_types = {"main": None, "sause": None, "bun": None}
    for item in ingredients["data"]:
        if item["type"] in ingredient_types and ingredient_types[item["type"]] is None:
            ingredient_types[item["type"]] = item["_id"]
    burger_ingredient = {"ingredients": list(ingredient_types.values())}
    return burger_ingredient

