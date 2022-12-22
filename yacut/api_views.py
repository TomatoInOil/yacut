from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import (
    EMPTY_REQUEST_API_ERROR_MSG,
    FIELD_IS_REQUIRED_MSG,
    ID_NOT_FOUND_API_ERROR_MSG,
    INVALID_SHORT_ID_ERROR_MSG,
    NON_UNIQUE_CUSTOMID_API_MSG,
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .services import get_unique_short_id, is_string_of_allowed_chars


@app.route("/api/id/", methods=["POST"])
def create_id():
    """Эндпоинт генерации новой ссылки."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(EMPTY_REQUEST_API_ERROR_MSG)
    url = data.get("url")
    custom_id = data.get("custom_id")
    if url is None:
        raise InvalidAPIUsage(FIELD_IS_REQUIRED_MSG % "url")
    if custom_id:
        if len(custom_id) > 16:
            raise InvalidAPIUsage(INVALID_SHORT_ID_ERROR_MSG)
        if not is_string_of_allowed_chars(custom_id):
            raise InvalidAPIUsage(INVALID_SHORT_ID_ERROR_MSG)
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(NON_UNIQUE_CUSTOMID_API_MSG % custom_id)
    else:
        custom_id = get_unique_short_id()
    url_object = URLMap(original=url, short=custom_id)
    db.session.add(url_object)
    db.session.commit()
    return jsonify(url_object.to_dict()), HTTPStatus.CREATED


@app.route("/api/id/<string:short_id>/", methods=["GET"])
def get_url(short_id):
    """Эндпоинт получения ссылки по идентификатору."""
    url_relation = URLMap.query.filter_by(short=short_id).first()
    if url_relation is None:
        raise InvalidAPIUsage(ID_NOT_FOUND_API_ERROR_MSG, HTTPStatus.NOT_FOUND)
    return jsonify({"url": url_relation.original})
