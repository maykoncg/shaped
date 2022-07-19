#!/bin/bash

echo "Apply database migrations"
poetry run python manage.py migrate
# Start server
echo "Starting server"
poetry run gunicorn super.wsgi -c super/gunicorn.conf.py --log-level warning -b 0.0.0.0:80
