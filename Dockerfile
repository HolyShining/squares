FROM kennethreitz/pipenv as build
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pipenv install
RUN pipenv run python manage.py migrate