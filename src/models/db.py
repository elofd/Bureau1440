"""
Модуль db.py, содержит классы для взаимодействия с БД.
"""
import sqlalchemy as sa
from sqlalchemy import Column, UUID, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from configuration.settings import pg_config

DATABASE_URL = (
    f"postgresql:/"
    f"/{pg_config.user}:{pg_config.password}"
    f"@{pg_config.host}:{pg_config.port}"
    f"/{pg_config.db}"
)
Base = declarative_base()
engine = sa.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_session():
    """
    Генератор для Depends в роутах, возвращает объект сессии с БД.
    """
    with SessionLocal() as session:
        yield session


class Secret(Base):
    """
    Класс для работы с таблицей secrets.
    """
    __tablename__ = 'secrets'

    secret_key = Column(UUID(as_uuid=True), primary_key=True)
    secret = Column(String)
    code = Column(String)
