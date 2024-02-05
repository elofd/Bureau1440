"""
Модуль settings.py, содержит основные настройки приложения.
"""
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

ENV_PATH = BASE_DIR / '.env'

DEFAULT_CONFIG_PARAMS = dict(_env_file=ENV_PATH, _env_file_encoding='utf-8')


class AppConfig(BaseSettings):
    """
    Класс с настройками приложения.
    """
    host: str = Field(help='Хост, на котором будет работать приложение')
    port: str = Field(help='Порт, на котором будет работать приложение')
    debug: bool = Field(help='Режим отладки приложения', default=False)
    enable_swagger: bool = Field(
        help='Включение/отключение swagger документации', default=False
    )
    log_level: str = Field(
        help='Уровень логирования в приложении', default='DEBUG'
    )


class PGConfig(BaseSettings):
    """
    Класс с настройками БД.
    """
    host: str = Field(help='Хост, на котором будет работать бд')
    port: str = Field(help='Порт, на котором будет работать бд')
    user: str = Field(help='Пароль для подключения к бд')
    password: str = Field(help='Пароль для подключения к бд')
    db: str = Field(default="db", help='Название бд')


app_config = AppConfig(_env_prefix='app_', **DEFAULT_CONFIG_PARAMS)
pg_config = PGConfig(_env_prefix='pg_', **DEFAULT_CONFIG_PARAMS)
