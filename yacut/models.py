from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    """Модель связи оригинальной и сокращенной ссылок."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Сериализатор объекта в словарь."""
        return {
            "url": self.original,
            "short_link": url_for(
                "redirect_view", short_id=self.short, _external=True
            ),
        }
