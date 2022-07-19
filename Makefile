setup:
	@poetry install && poetry shell

services:
	@docker-compose up -d

migrate:
	@poetry run python manage.py migrate

makemigrations:
	@poetry run python manage.py makemigrations

workers:
	@poetry run celery -A shaped worker -l INFO

run:
	@poetry run python manage.py runserver

test:
	@poetry run pytest

shell:
	@poetry run python manage.py shell