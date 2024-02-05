"""
Модуль main.py, отвечает за запуск приложения.
"""
import logging
from os.path import join

import uvicorn

from configuration.fastapi_app import app
from configuration.settings import app_config, BASE_DIR


def run_server():
    """
    Функция для запуска сервера.
    """
    log_config = join(BASE_DIR, 'logging.yml')
    log_level = getattr(logging, app_config.log_level)
    uvicorn.run(
        app,
        host=app_config.host,
        port=app_config.port,
        log_config=log_config,
        log_level=log_level
    )


if __name__ == '__main__':
    run_server()
