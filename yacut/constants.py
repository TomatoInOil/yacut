import string

FIELD_IS_REQUIRED_MSG = '"%s" является обязательным полем!'
NON_UNIQUE_CUSTOMID_MSG = "Имя %s уже занято!"
NON_UNIQUE_CUSTOMID_API_MSG = 'Имя "%s" уже занято.'
INVALID_SHORT_ID_ERROR_MSG = "Указано недопустимое имя для короткой ссылки"
ID_NOT_FOUND_API_ERROR_MSG = "Указанный id не найден"
EMPTY_REQUEST_API_ERROR_MSG = "Отсутствует тело запроса"

MAXIMUM_LENGTH_OF_SHORT_ID = 16
LENGTH_OF_RANDOM_SHORT_ID = 6
ALLOWED_SHORT_ID_CHARS = string.ascii_letters + string.digits

INDEX_TEMPLATE = "index.html"
ERROR_404_TEMPLATE = "404.html"
ERROR_500_TEMPLATE = "500.html"
