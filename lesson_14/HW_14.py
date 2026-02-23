"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest
import os


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename="login_system.log",
        level=logging.INFO,
        format='%(asctime)s - %(message)s - %(levelname)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

LOG_FILE = "login_system.log"

# Test 1 - checking that we even have records in our log file
@pytest.mark.parametrize("username, status, log_lvl", [
    ("admin", "success", "INFO"),
    ("admin", "expired", "WARNING"),
    ("user_1", "expired", "WARNING"),
    ("user_2", "success", "INFO"),
    ("user", "failed", "ERROR"),
    ("admin", "unknown", "ERROR"),
])
def test_log_event_writes_to_file(username, status, log_lvl):

    logging.root.handlers.clear()  # we need it for basic config work

    log_event(username, status)

    with open(LOG_FILE, "r") as f:
        content = f.read()

    assert f"Login event - Username: {username}, Status: {status} - {log_lvl}" in content


# # Test 2 - checking logging level for the recods
# @pytest.mark.parametrize("username, status, expected_lvl", [
#     ("admin", "success", logging.INFO),
#     ("admin", "expired", logging.WARNING),
#     ("user", "failed", logging.ERROR),
#     ("admin", "unknown", logging.ERROR),
# ])
# def test_log_event_level(caplog, username, status, expected_lvl):
#     with caplog.at_level(logging.DEBUG):
#         log_event(username, status)
#
#     assert len(caplog.records) > 0
#     assert caplog.records[0].levelno == expected_lvl
