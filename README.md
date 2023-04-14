# yamdb_final
[![yamdb workflow](https://github.com/AgarkovEgor/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/AgarkovEgor/yamdb_final/actions/workflows/yamdb_workflow.yml)

## Когда вы запустите проект, по адресу http://158.160.17.237/redoc
## Будет доступна документация для API Yatube. 
## В документации описано, как должен работать ваш API. Документация представлена в формате Redoc.
# Групповой проект по теме API
## Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». 

## Запуск проекта
- Клонировать репозиторий и перейти в него в командной строке.
- Установить и активировать виртуальное окружение:

## Пример env файла
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY=key
```
```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python -m pip install --upgrade pip
```

- Затем нужно установить все зависимости из файла requirements.txt

```bash
pip install -r requirements.txt
```

- Выполняем миграции:

```bash
python manage.py migrate
```

- Запускаем проект:

```bash
python manage.py runserver
```

## Примеры запросов к API:
GET api/v1/title/ - получить список всех произведений.

- Для создания публикации используем:

```r
POST запрос к эндпоинту /api/v1/title/
```

в body указываем:

```json
{
"name": "name",
"year": "year",
"description": не обязательно,
"genre": "genre",
"category": "category"
}
```


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

## Использумые технологии:
- Python
- Django
- PyJWT
- Django Rest Framework
- Docker
- Nginx
 
## Авторы проекта:
- Агарков Егор
- Екатерина Толмачева
- Сергей Горшков