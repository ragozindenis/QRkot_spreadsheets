# Проект "QRKot"

## Благотворительный фонд поддержки котиков


### Описание:

* Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
* В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
* Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.
* Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

### Возможности:

* Целевые проекты создаются администраторами сайта.
* Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
* Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
* Создание отчета о завершённых инвестициях в google spreadsheets.
* Автоматическое создание пользователя с правами администратора.

### Технологии:

Проект создан с использованием:
* Python version: 3.10.6
* FastAPI version: 0.78.0
* SQLAlchemy version: 1.4.36
* Google API

## Как запустить проект:

### 1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:ragozindenis/cat_charity_fund.git
```
```
cd cat_charity_fund/
```
### 2. Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
### 3. Обновить пакет pip и установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
### 4. Создать файл .env в корневой папке и заполнить его:
* Создание файла:
```
touch .env
```
* Пример заполнения:
```
APP_TITLE=Кошачий благотворительный фонд
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=secretcatskey
FIRST_SUPERUSER_EMAIL=admin@example.com
FIRST_SUPERUSER_PASSWORD=password
EMAIL= # email google
TYPE= # from api key google
PROJECT_ID= # from api key google
PRIVATE_KEY_ID= # from api key google
PRIVATE_KEY= # from api key google
CLIENT_EMAIL= # from api key google
CLIENT_ID= # from api key google
AUTH_URI= # from api key google
TOKEN_URI= # from api key google
AUTH_PROVIDER_X509_CERT_URL= # from api key google
CLIENT_X509_CERT_URL=# from api key google
UNIVERSE_DOMAIN= # from api key google
```
### 5. Запустить миграцию для создания базы данных:
```
alembic upgrade head
```
### 6. Запуск проекта:
```
uvicorn app.main:app --reload
```

## После запуска будет доступна документация api:
```
http://127.0.0.1:8000/docs
```
```
http://127.0.0.1:8000/redoc
```

## Примеры запросов:
### Запрос всех проектов (GET):
* GET http://127.0.0.1:8000/charity_project/
* Successful Response:
```
[
  {
    "name": "string",
    "description": "string",
    "full_amount": 0,
    "id": 0,
    "invested_amount": 0,
    "fully_invested": true,
    "create_date": "2023-07-29T20:05:12.440Z",
    "close_date": "2023-07-29T20:05:12.440Z"
  }
]
```

### Создание проекта (POST):
* POST http://127.0.0.1:8000/charity_project/
* Request body:
```
{
  "name": "string",
  "description": "string",
  "full_amount": 0
}
```
* Successful Response:
```
{
  "name": "string",
  "description": "string",
  "full_amount": 0,
  "id": 0,
  "invested_amount": 0,
  "fully_invested": true,
  "create_date": "2023-07-29T20:08:05.975Z",
  "close_date": "2023-07-29T20:08:05.975Z"
}
```

### Запрос всех пожертвований (GET):
* GET http://127.0.0.1:8000/donation/
* Successful Response:
```
[
  {
    "full_amount": 0,
    "comment": "string",
    "id": 0,
    "user_id": 0,
    "invested_amount": 0,
    "fully_invested": true,
    "create_date": "2023-07-29T20:15:56.029Z",
    "close_date": "2023-07-29T20:15:56.030Z"
  }
]
```

### Создание пожертвования (POST):
* POST http://127.0.0.1:8000/donation/
* Request body:
```
{
  "full_amount": 0,
  "comment": "string"
}
```
* Successful Response:
```
{
  "full_amount": 0,
  "comment": "string",
  "id": 0,
  "user_id": 0,
  "invested_amount": 0,
  "fully_invested": true,
  "create_date": "2023-07-29T20:16:17.163Z",
  "close_date": "2023-07-29T20:16:17.163Z"
}
```

### Получить отчет в google sheets (POST):
* POST http://127.0.0.1:8000/google/
* Successful Response:
```
{
  "url_google_sheets": "https://docs.google.com/spreadsheets/d/{spreadsheetid}"
}
```

## C Полной документацией можно ознакомиться тут:
```
http://127.0.0.1:8000/docs
```
```
http://127.0.0.1:8000/redoc
```

## Автор:
* [Рагозин Денис](https://github.com/ragozindenis)
