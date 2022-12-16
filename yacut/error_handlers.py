from flask import render_template

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
