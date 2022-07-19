#
FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
 
 
RUN apt-get update && apt-get install libpq-dev build-essential gdal-bin -y
 
RUN mkdir /code
WORKDIR /code
COPY api /code/api
COPY registro /code/registro
COPY shaped /code/shaped

COPY entrypoint.sh entrypoint-worker.sh manage.py poetry.lock pyproject.toml /code/
 
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev
 
EXPOSE 80