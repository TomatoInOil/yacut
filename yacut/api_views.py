from flask import jsonify, request

from . import app, db
from .constants import (
    EMPTY_REQUEST_API_ERROR_MSG,
    FIELD_IS_REQUIRED_MSG,
    ID_NOT_FOUND_API_ERROR_MSG,
    NON_UNIQUE_CUSTOMID_MSG,
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .services import get_unique_short_id


@app.route("/api/id/", methods=["POST"])
def create_id():
    """Эндпоинт генерации новой ссылки."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(EMPTY_REQUEST_API_ERROR_MSG)
    url = data.get("url")
    custom_id = data.get("custom_id")
    if url is None:
        raise InvalidAPIUsage({"url": FIELD_IS_REQUIRED_MSG})
    if custom_id:
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(NON_UNIQUE_CUSTOMID_MSG)
    else:
        custom_id = get_unique_short_id()
    url_object = URLMap(original=url, short=custom_id)
    db.session.add(url_object)
    db.session.commit()
    return jsonify(url_object.to_dict()), 201


@app.route("/api/id/<string:short_id>/", methods=["GET"])
def get_url(short_id):
    """Эндпоинт получения ссылки по идентификатору."""
    url_relation = URLMap.query.filter_by(short=short_id).first()
    if url_relation is None:
        raise InvalidAPIUsage(ID_NOT_FOUND_API_ERROR_MSG, 404)
    return jsonify({"url": url_relation.original})
