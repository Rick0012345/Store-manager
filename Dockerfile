FROM python:3.10.5

EXPOSE 8000
WORKDIR /project

ADD requirements.txt /project
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    libpq-dev gcc


ADD ./project /project

CMD gunicorn    --bind 0.0.0.0:8000      \
                --reload wsgi:application
