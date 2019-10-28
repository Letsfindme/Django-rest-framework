FROM python:3.7-alpine
MAINTAINER Lets Find ME Ltd.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --no-cache --update jpeg-dev
RUN apk add --no-cache --virtual build-dependencies \
      build-base \
      py-mysqldb \
      gcc \
      musl-dev \
      libc-dev \
      libffi-dev \
      mariadb-dev \
      musl-dev zlib zlib-dev
      #&& rm -rf .cache/pip

RUN pip install pymysql
RUN pip install mysqlclient
RUN pip install -r /requirements.txt
#RUN apk del build-dependencies

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user