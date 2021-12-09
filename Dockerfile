FROM python:3.10-alpine

WORKDIR /app
COPY . /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN pip install pipenv
RUN pipenv install --system --deploy

RUN pip install uwsgi

RUN python manage.py collectstatic --noinput

ENV PORT=8080
EXPOSE 8080

CMD ["pipenv", "run",  "uwsgi", "--ini", "/app/uwsgi.ini"]