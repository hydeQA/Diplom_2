BASE_URL = "https://stellarburgers.nomoreparties.site/api/"

CREATE_USER_ENDPOINT = "auth/register" # POST запрос на создание пользователя
DELETE_USER_ENDPOINT = "auth/user" # метод DELETE
GET_USER_ENDPOINT = "auth/user" # метод GET
LOGIN_USER_ENDPOINT = "auth/login" # POST завпрос на авторизацию
LOGOUT_USER_ENDPOINT = "auth/logout" # POST запрос на выход из системы
PATCH_USER_ENDPOINT = "auth/user"  #метод PATCH для обновления данных

REFRESH_TOKEN_ENDPOINT = "auth/token"

CREATE_ORDER_ENDPOINT = "orders" # POST Создание заказа
GET_ORDER_ENDPOINT = "orders/all" # Получение всех заказов
GET_USER_ORDER = "orders" # GET запрос на получение заказов пользователя

GET_INGREDIENTS_ENDPOINT = "ingredients" # метод GET получения данных об ингридиентах

RECOVER_PASSWORD_ENDPOINT = "password-reset" # POST запрос на восстановление пароля
RESET_PASSWORD_ENDPOINT = "password-reset/reset" # POST сброс пароля



