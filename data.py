class URL:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    REGISTER_URL = f'{BASE_URL}/auth/register'
    LOGIN_URL = f'{BASE_URL}/auth/login'
    USER_URL = f'{BASE_URL}/auth/user'
    ORDER_URL = f'{BASE_URL}/orders'
    USER_ORDERS_URL = f'{BASE_URL}/orders'
    DELETE_USER_URL = f'{BASE_URL}/auth/user'


class Answers:
    UNAUTHORISED_ANSWER = 'You should be authorised'
    DUPLICATE_USER_ANSWER = 'User already exists'
    REQUIRED_FIELD_ANSWER = 'Email, password and name are required fields'
    INCORRECT_ANSWER = 'email or password are incorrect'
    NO_INGREDIENTS_ANSWER = 'Ingredient ids must be provided'
    UPDATE_EXIST_EMAIL_ANSWER = 'User with such email already exists'
    TRUE_ANSWER = True
