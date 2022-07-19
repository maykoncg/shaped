#!/bin/bash
echo "Starting server"
poetry run celery -A super.celery worker --loglevel=INFO