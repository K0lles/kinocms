# syntax=docker/dockerfile:1
FROM python:3.10-alpine

ENV KINOCMS=/home/app/kinocms

RUN mkdir -p $KINOCMS
RUN mkdir -p $KINOCMS/static

WORKDIR $KINOCMS

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY . $KINOCMS
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver

##copy entrypoint.sh
#COPY ./entrypoint.sh $KINOCMS
#
## run entrypoint.sh
#ENTRYPOINT ['/bin/bash', '/home/app/kinocms/entrypoint.sh']
