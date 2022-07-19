# TESTE

## System Dependencies

- gdal

## Setup local environment

This project uses [poetry](https://python-poetry.org/) and
[docker](https://docs.docker.com/) to manage his environment. After setup this tools on your system follow this instructions
to get started:

### Before start

#### Install Proetry

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
source $HOME/.poetry/env
```

#### Setup dependencies

```shell
make setup
```

#### Run docker services

```shell
make services
```

#### Run Celery workers

```shell
make workers
```


## Development

### Commands

#### Run application locally

```shell
make run
```

#### Make migrations

```shell
make makemigrations
```

#### Run migrations

```shell
make migrate
```

#### Run tests

```shell
make test
```

#### Run Django shell

```shell
make shell
```
