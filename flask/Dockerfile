FROM python:3.8

COPY ./app /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

ARG DATABASE_URL='postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'

EXPOSE 5000

CMD ["python", "/app/app.py"]

