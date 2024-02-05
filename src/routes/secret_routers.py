"""
Модуль secret_routers.py, содержит роуты для создания и чтения секретов.
"""
import uuid

from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from models import dto, db
from models.db import get_session

secrets_routers = APIRouter()


@secrets_routers.post("/generate",
                      description='Создание нового секрета',
                      response_model=dto.CreateSecretResponse)
async def generate_secret(body: dto.CreateSecretBody,
                          db_: Session = Depends(get_session)):
    new_secret = db.Secret(
        secret_key=uuid.uuid4(),
        secret=body.secret,
        code=body.code
    )
    db_.add(new_secret)
    db_.flush([new_secret])
    db_.commit()
    response = dto.CreateSecretResponse(secret_key=new_secret.secret_key)
    return response


@secrets_routers.get("/secrets/{secret_key}",
                     description='Получение секрета по ключу и его удаление',
                     response_model=dto.GetSecretResponse)
async def get_secret(secret_key: str,
                     code: str = Query(),
                     db_: Session = Depends(get_session)):
    secret = db_.query(db.Secret).where(
        db.Secret.secret_key == secret_key
    ).first()
    if not secret:
        raise HTTPException(
            status_code=404,
            detail=f'No secret with secret_key: {secret_key}'
        )
    if secret.code != code:
        raise HTTPException(
            status_code=403,
            detail=f'Wrong code for secret: {code}'
        )
    db_.delete(secret)
    db_.commit()
    response = dto.GetSecretResponse(
        secret_key=secret.secret_key,
        secret=secret.secret,
        code=secret.code
    )
    return response
