FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt update && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server \
&& pip install --upgrade pip \
&& pip install -r requirements.txt
ADD . /code

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]