import allure
import helper
import urls
import requests

@allure.step("Создать тело запроса создания юзера: email, password, name")
def create_user_body():
    return helper.new_user_login_password()

@allure.step("Создать пользователя в приложении Stellar burger")
def create_user(user_data):
    user_response = requests.post(urls.BASE_URL+urls.CREATE_USER_ENDPOINT, json=user_data)
    return user_response

@allure.step("Получение access token созданного пользователя")
def get_access_token(user_response):
    access_token = user_response.json().get("accessToken")
    return access_token

@allure.step("Удалить созданного пользователя")
def delete_user(access_token):
    headers = {"Authorization": access_token}
    response_delete = requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers=headers)
    return response_delete