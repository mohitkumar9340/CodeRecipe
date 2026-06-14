FROM python:3.14-slim

WORKDIR /online_judge

RUN apt-get update && apt-get install -y --no-install-recommends \
    clang \
    openjdk-21-jdk-headless \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=oj_backend.settings
ENV PYTHONUNBUFFERED=1

CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
