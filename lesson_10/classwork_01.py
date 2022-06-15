"""
1. Создать функцию при помощи регулярных выражений для проверки,
что строка является валидным телефонным номером в формате +375 (29) 299-29-29.
2. Создать тест в отдельном файле и проверить несколько телефонных номеров.
"""

import re
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def is_mobile_phone(string):
    return re.match(r"^\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}", string)


if __name__ == "__main__":
    for item in ("+375 (29) 299-29-29", "+375 (29) 100-00-00"):
        assert is_mobile_phone(item) is not None

    for item in ("(29) 299-29-29", "375292992929"):
        assert is_mobile_phone(item) is None

    logger.debug("All tests are OK")
