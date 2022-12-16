import random
import string

from .constants import MAXIMUM_LENGTH_OF_SHORT_ID
from .models import URLMap


def get_unique_short_id() -> str:
    """Возвращает случайный уникальный короткий ID."""
    allowed_characters = string.ascii_letters + string.digits
    short_id = "".join(
        random.choice(allowed_characters)
        for _ in range(random.randint(4, MAXIMUM_LENGTH_OF_SHORT_ID))
    )
    if URLMap.query.filter_by(short=short_id).first() is not None:
        return get_unique_short_id()
    return short_id
