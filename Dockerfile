# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY .env /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN ls

RUN python -m pip install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz
RUN uwsgi \
    --module=mysite.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=api.settings \
    --master --pidfile=/tmp/project-master.pid \
    --socket=127.0.0.1:49152 \
    --processes=5 \
    --uid=1000 --gid=2000 \
    --harakiri=20 \
    --max-requests=5000 \
    --vacuum \
    --daemonize=/var/log/uwsgi/yourproject.log



COPY . /code/


RUN set -a && . /code/.env && set +a
RUN env
RUN ["python", "manage.py", "runserver"]