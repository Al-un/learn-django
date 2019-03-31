# Learn Django

## Getting started

```sh
# Clone
git clone https://github.com/Al-un/learn-django.git
cd learn-django

# Install pipenv if required
pip3 install pipenv

# Install dependencies
pipenv install

# Databases:
#   - PostgreSQL: create database and add DATABASE_URL in learn_django/.env
#   - Sqlite3   : comment PostgreSQL and uncomment Sqlite code in settings.py

# Run migrations
pipenv run python3 manage.py migrate

# Run!
pipenv run python3 manage.py runserver
```

## Contents

- [First steps](00.init.md)
  - [Installation](00.init.md#installation)
  - [Create a Django project](00.init.md#django)
  - [Database configuration](00.init.md#postgresql)
- [Polls](01.polls.md)
  - [Polls app](01.polls.md#poll-app)
  - [Polls models](01.polls.md#models)
  - [Admin pages](01.polls.md#admin-pages)
  - [Polls REST API](01.polls.md#rest-api)
