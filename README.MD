# Bureau1440 secret app
Версия Python - 3.11
## Запуск проекта локально:

1. Скопировать .env.example в .env
2. Запустить сервисы с помощью:
```shell
docker compose up -d
```
3. Пометить папку `src` как `source root`
4. ```cd src/```
5. ```pip install -r requirements.txt```
6. ```python main.py```

## Архитектура проекта
```text
src
├── configuration
│   Файлы конфигурации приложения
│   
├── alembic
│   Миграции и настройки alembic
│ 
├── models
│   Модели данных для всего приложения
│   
├── routers
│   Роутеры для обработки входящих запросов
│
├── tests 
│   Тесты приложения, все файлы тестов должны начинаться с test_
```

## Миграции
- Для создания миграции необходимо ввести команду 
  - `alembic revision --autogenerate`
- Для применения миграции
  - `alembic upgrade head`
- Для отката миграций одной миграции
  - `alembic downgrade -1` - вместо 1 пишите количество миграции которые нужно откатить
