FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt update && \
    apt upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server nginx supervisor\
    && pip install --upgrade pip \
    && pip install -r requirements.txt
    && pip install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

ADD . /code

EXPOSE 80
CMD ["supervisord", "-n"]
