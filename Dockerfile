FROM python:3.12

WORKDIR /home

RUN apt update && apt upgrade -y
RUN apt update && apt install vim -y

COPY . ./

RUN python -m pip install -U pip
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app