# Test Task Django app

## To see all urls, open swagger-ui
```
http://127.0.0.1:8000/api/
```
# How to start app

1. 
```terminal
poetry shell
```
2.
```terminal
poetry install
 ```
3.
create .env file 

fill the fields

example:




```terminal
SECRET_KEY='your secret key'
```

```terminal
DEBUG=True
```

```terminal
ALLOWED_HOSTS='1270.0.1 localhost
```

```terminal
PG_DATABASE=test-django
PG_USER=postgres
PG_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

```terminal
BOT_TOKEN='your bot token(take form BotFather)
```
4.

```commandline
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

 5.

Run main.py file in tg_bot directory to start telegram bot


