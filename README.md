# Nubosas aio template project

## Instroduction
This project is a basic template for a Python 3 [aio-libs](https://aio-libs.discourse.group/) based
project.

It shows a way to create a new project with Docker images,
[bandit](https://bandit.readthedocs.io/en/latest/) tests, unit tests, integration tests and
[Gitlab CI/CD](https://gitlab.com/nubosas/nubosas.aiotemplate/pipelines).

This project doesn't pretends to say this is the only way or the best way to do it, it's the way
we are happy with, that works for us. It's alive and evolving over time as we find better ways to
implement it or find more useful tools to integrate it with.

## Features

### Development tools

* [bandit](https://bandit.readthedocs.io/en/latest/) to do some automatic security checks in the code.
* [flake8](https://gitlab.com/pycqa/flake8) to check style and quality of the code.
* [pytest](https://docs.pytest.org/en/latest/) to run unit and integration tests.
* [docker-compose](https://docs.docker.com/compose/) to run local system for development.
* [Gitlab CI/CD](https://gitlab.com/nubosas/nubosas.aiotemplate/pipelines). 

### Service implementation

* [aiohttp](https://docs.aiohttp.org/en/stable/) to serve HTTP requests.
* [aiopg](https://aiopg.readthedocs.io/en/stable/) to handle asynchronous PostgreSQL queries.
* [SQLAlchemy](https://www.sqlalchemy.org/) as the DB ORM.
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) as the DB migration tool.
* [pip-tools](https://github.com/jazzband/pip-tools/) to freeze dependencies and handle the requirements.txt and dev-requirements.txt files.
* [setuptools_scm](https://github.com/pypa/setuptools_scm/) to handle service version based on repository tags.

### Service running

* [Docker](https://docs.docker.com/) to build and then deploy the service to production.


## TODO list

* Add some unit tests instead of current place holder.
* Add some example intetration tests instead of current place holder.
* Add Github Actions support.

## How to run it.

## Building the service

To download dependencies, like PostgreSQL and build the service itself you will need to run:

```
$ docker-compose build
```

## Initialise the database

This project adds a basic script which initialises the database schema and then adds some example
data to the database. The best way to initialise it would be, using `docker-compose`:

```
$ docker-compose run aiotemplate  wait-for-it.sh aiotemplate-db:5432 -- init-accounts-db
```

## Run the server

```
$ docker-compose run aiotemplate
```
