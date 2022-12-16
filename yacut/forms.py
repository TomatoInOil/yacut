import string

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from .constants import FIELD_IS_REQUIRED_MSG, MAXIMUM_LENGTH_OF_SHORT_ID


class AllowedCharacters(object):
    """Проверка строки на разрешенные символы."""

    def __init__(self, allowed_chars=None, message=None):
        if not allowed_chars:
            allowed_chars = string.ascii_letters + string.digits
        self.allowed_chars = allowed_chars
        if not message:
            message = (
                "Разрешено использовать только большие и маленькие "
                "латинские буквы, цифры в диапазоне от 0 до 9."
            )
        self.message = message

    def __call__(self, form, field):
        input_chars = set(field.data)
        for input_char in input_chars:
            if input_char not in self.allowed_chars:
                raise ValidationError(self.message)


class URLForm(FlaskForm):
    """Форма запроса на сокращение ссылки."""

    original_link = URLField(
        "Длинная ссылка",
        validators=[
            DataRequired(message=FIELD_IS_REQUIRED_MSG),
            Length(1, 2048),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[
            Length(1, MAXIMUM_LENGTH_OF_SHORT_ID),
            Optional(),
            AllowedCharacters(),
        ],
    )
    submit = SubmitField("Создать")
