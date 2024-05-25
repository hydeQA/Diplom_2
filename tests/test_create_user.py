import allure


class TestCreateUser:
    @allure.title("Проверка успешной регистрации пользователя")
    @allure.description("Создание пользователя. Проверка статуса ответа и тела ответа")
    def test_create_user_success(self, default_user):
        create_user_request = default_user
        assert create_user_request.status_code == 200 and create_user_request.json() is not None


# Ошибка при создании пользователя дубликата
# Шаги
# POST https://stellarburgers.nomoreparties.site/api/auth/register
# 1. Создать email
# 2. Создать password
# 3. Создать name
# Отправить тело запроса на endpoint
# Отправить повторный запрос на создание того же пользователя
# ОР: ответ 403 Forbidden

# Ошибка при создании пользователя без одного из полей
# Шаги
# POST https://stellarburgers.nomoreparties.site/api/auth/register
# 1. Создать email
# 2. Создать password
# 3. Создать name
# Отправить тело запроса на endpoint без одного из полей
# ОР: ответ 403 Forbidden