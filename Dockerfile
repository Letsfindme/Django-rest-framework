FROM python:3.7-alpine
MAINTAINER Lets Find ME Ltd.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk --no-cache add --virtual build-dependencies \
      build-base \
      py-mysqldb \
      gcc \
      musl-dev \
      libc-dev \
      libffi-dev \
      mariadb-dev
      #&& rm -rf .cache/pip

RUN pip install pymysql
RUN pip install mysqlclient
RUN pip install -r /requirements.txt
#RUN apk del build-dependencies

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user