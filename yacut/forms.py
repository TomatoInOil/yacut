from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from .constants import (
    FIELD_IS_REQUIRED_MSG,
    INVALID_SHORT_ID_ERROR_MSG,
    MAXIMUM_LENGTH_OF_SHORT_ID,
)
from .services import is_string_of_allowed_chars


class AllowedCharacters(object):
    """Проверка строки на разрешенные символы."""

    def __init__(self, message=None):
        if not message:
            message = INVALID_SHORT_ID_ERROR_MSG
        self.message = message

    def __call__(self, form, field):
        input_chars = set(field.data)
        if not is_string_of_allowed_chars(input_chars):
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
