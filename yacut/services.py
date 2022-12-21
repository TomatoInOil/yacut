import random
import string

from .constants import ALLOWED_SHORT_ID_CHARS, LENGTH_OF_RANDOM_SHORT_ID
from .models import URLMap


def get_unique_short_id() -> str:
    """Возвращает случайный уникальный короткий ID."""
    allowed_characters = string.ascii_letters + string.digits
    short_id = "".join(
        random.choice(allowed_characters)
        for _ in range(LENGTH_OF_RANDOM_SHORT_ID)
    )
    if URLMap.query.filter_by(short=short_id).first() is not None:
        return get_unique_short_id()
    return short_id


def is_string_of_allowed_chars(
    input_chars, allowed_chars=ALLOWED_SHORT_ID_CHARS
) -> bool:
    """Возвращает True, если строка состоит из разрешенных символов."""
    for input_char in input_chars:
        if input_char not in allowed_chars:
            return False
    return True
