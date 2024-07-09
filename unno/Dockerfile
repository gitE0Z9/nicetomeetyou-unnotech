FROM python:3.10

ENV DJANGO_SETTINGS_MODULE unno.local_settings

COPY app /app

WORKDIR /app

COPY requirements.txt .
COPY requirements.dev.txt .

RUN pip install -r requirements.txt \
    && pip install -r requirements.dev.txt

RUN python manage.py collectstatic --noinput