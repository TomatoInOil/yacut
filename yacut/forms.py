from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from .constants import FIELD_IS_REQUIRED_MSG, MAXIMUM_LENGTH_OF_SHORT_ID


class URLForm(FlaskForm):
    """Форма запроса на сокращение ссылки."""

    original_link = URLField(
        "Введите ссылку, которую хотите сократить",
        validators=[
            DataRequired(message=FIELD_IS_REQUIRED_MSG),
            Length(1, 2048),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки (необязательно)",
        validators=[Length(1, MAXIMUM_LENGTH_OF_SHORT_ID), Optional()],
    )
    submit = SubmitField("Создать")
