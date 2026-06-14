FROM python:3.9
WORKDIR /online_judge
COPY . /online_judge

RUN apt-get update && apt-get install -y clang
RUN pip install --no-cache django
RUN pip install --no-cache djangorestframework
RUN pip install --no-cache djangorestframework-simplejwt
RUN pip install --no-cache django-cors-headers

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=oj_backend.settings
ENV PYTHONUNBUFFERED=1

CMD sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
