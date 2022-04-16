# Пульт охраны банка

Django-проект, реализующий пульт охраны банка.

## Окружение

Скачать git:
```bash
sudo apt-get install git
```
Сделать fork репозитория:
```bash
git clone https://github.com/NankuF/django-orm-watching-storage
```
Перейти в директорию со скриптом:
```bash
cd ~ && cd django-orm-watching-storage/
```
Создать виртуальное окружение:
```bash
python -m venv venv
```
Активировать виртуальное окружение:
```bash
. ./venv/bin/activate
```
Установить зависимости:
```bash
pip install -r requirements.txt 
```
Создать файл `.env` и добавить в него переменные
```angular2html
SECRET_KEY=your_secret_key (нужно придумать)
DEBUG=TRUE or FALSE

# DATABASE (значения берутся из документации к PostgreSql)
PG_ENGINE=your_engine (django.db.backends.postgresql_psycopg2)
PG_HOST=your_host
PG_PORT=your_port
PG_NAME=your_database_name
PG_USER1=your_user
PG_PASSWORD=your_password
```
## Запуск: <br>

Ввести в консоли код:
```bash
python manage.py runserver
```