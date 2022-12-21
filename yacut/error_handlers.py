from flask import jsonify, render_template

from . import app, db
from .constants import ERROR_404_TEMPLATE, ERROR_500_TEMPLATE


@app.errorhandler(404)
def page_not_found(error):
    """Страница ошибки 'страница не найдена'."""
    return render_template(ERROR_404_TEMPLATE), 404


@app.errorhandler(500)
def internal_error(error):
    """Страница внутренней ошибки сервера."""
    db.session.rollback()
    return render_template(ERROR_500_TEMPLATE), 500


class InvalidAPIUsage(Exception):
    """Исключение вызываемое при ошибке при использовании API."""

    status_code = 400

    def __init__(self, message, status_code=None, *args: object) -> None:
        super().__init__(*args)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        """Сериализатор сообщения об ошибке в словарь."""
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    """Обработчик ошибок возникающих при использовании API."""
    return jsonify(error.to_dict()), error.status_code
