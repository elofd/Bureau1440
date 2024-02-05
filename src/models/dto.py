"""
Модуль dto.py, содержит классы для сериализации и десериализации данных.
"""
import uuid

from pydantic import BaseModel


class CreateSecretBody(BaseModel):
    """
    Модель для тела запроса отправки секрета.
    """
    secret: str
    code: str


class CreateSecretResponse(BaseModel):
    """
    Модель для ответа после создания нового секрета.
    """
    secret_key: uuid.UUID


class GetSecretResponse(BaseModel):
    """
    Модель для получения информации о секрете.
    """
    secret_key: uuid.UUID
    secret: str
    code: str
