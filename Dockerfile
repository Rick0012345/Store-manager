FROM python:3.10.5

# Instala NodeJS e dependências

RUN apt-get update && apt-get install -y curl \
&& curl -fsSL https://deb.nodesource.com/setup_21.x | bash - \
&& apt-get install -y nodejs \
&& rm -rf /var/lib/apt/lists/*

EXPOSE 8000

WORKDIR /usr/src/project

ADD requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libpq-dev gcc

ADD ./project .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--reload", "wsgi:application"]