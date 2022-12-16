from flask import render_template


from . import app
from .constants import INDEX_TEMPLATE


@app.route("/")
def index_view():
    """Главная страница с формой сокращения ссылок."""
    return render_template(INDEX_TEMPLATE)


@app.route("/<string:short_id>/")
def redirect_view(short_id):
    """Переадресация сокращенных ссылок."""
    pass
