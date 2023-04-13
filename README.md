# yamdb_final
yamdb_final

## Пример заполнения env

DB_ENGINE=django.db.backends.postgresql - указываем, что работаем с postgresql

DB_NAME=postgres - имя базы данных

POSTGRES_USER=postgres - логин для подключения к базе данных

POSTGRES_PASSWORD=postgres - пароль для подключения к БД (установите свой)

DB_HOST=db - название сервиса (контейнера)

DB_PORT=5432 - порт для подключения к БД 

## Запуск контейнера

cd infra/ - переходим в директорию

docker-compose up -d --build - запускаем контейнер

docker-compose exec web python manage.py migrate - делаем миграции

docker-compose exec web python manage.py createsuperuser - создаём супер пользователя

docker-compose exec web python manage.py collectstatic --no-input - подключем статику

## Копирование базы

docker-compose exec web python manage.py dumpdata > fixtures.json

## Наполнение БД fixtures

docker-compose exec web python manage.py loaddata <fixtures name>.json
[![yamdb workflow](https://github.com/AgarkovEgor/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/AgarkovEgor/yamdb_final/actions/workflows/yamdb_workflow.yml)