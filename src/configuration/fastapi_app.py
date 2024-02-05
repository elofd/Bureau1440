"""
Модуль fastapi_app.py, создаёт и настраивает экземпляр приложения FastAPI.
"""
from fastapi import FastAPI

from configuration.settings import app_config
from routes.secret_routers import secrets_routers

ROUTERS = (secrets_routers, )


def create_app():
    """
    Функция создаёт и настраивает экземпляр приложения FastAPI.
    """
    service = FastAPI(
        title='Bureau1440 secret',
        version='0.1.0',
        openapi_url='/openapi.json' if app_config.enable_swagger else ''
    )
    for router in ROUTERS:
        service.include_router(router, prefix="/api/v1")

    return service


app = create_app()
