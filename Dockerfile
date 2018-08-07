FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt update && \
    apt upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server nginx supervisor\
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY conf/server/nginx-app.conf /etc/nginx/sites-available/default
COPY conf/server/supervisor-app.conf /etc/supervisor/conf.d/

# Oracle
# https://github.com/sergeymakinen/docker-oracle-instant-client
ENV DEBIAN_FRONTEND noninteractive
ENV ORACLE_INSTANTCLIENT_MAJOR 11.2
ENV ORACLE_INSTANTCLIENT_VERSION 11.2.0.4.0
ENV ORACLE /usr/local/oracle
ENV ORACLE_HOME $ORACLE/lib/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$ORACLE_HOME/lib
ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$ORACLE/include/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64

RUN apt-get update && apt-get install -y libaio1 \
        curl rpm2cpio cpio \
    && mkdir $ORACLE && TMP_DIR="$(mktemp -d)" && cd "$TMP_DIR" \
    && curl -L https://github.com/sergeymakinen/docker-oracle-instant-client/raw/assets/oracle-instantclient$ORACLE_INSTANTCLIENT_MAJOR-basic-$ORACLE_INSTANTCLIENT_VERSION-1.x86_64.rpm -o basic.rpm \
    && rpm2cpio basic.rpm | cpio -i -d -v && cp -r usr/* $ORACLE && rm -rf ./* \
    && ln -s libclntsh.so.11.1 $ORACLE/lib/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64/lib/libclntsh.so.$ORACLE_INSTANTCLIENT_MAJOR \
    && ln -s libocci.so.11.1 $ORACLE/lib/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64/lib/libocci.so.$ORACLE_INSTANTCLIENT_MAJOR \
    && curl -L https://github.com/sergeymakinen/docker-oracle-instant-client/raw/assets/oracle-instantclient$ORACLE_INSTANTCLIENT_MAJOR-devel-$ORACLE_INSTANTCLIENT_VERSION-1.x86_64.rpm -o devel.rpm \
    && rpm2cpio devel.rpm | cpio -i -d -v && cp -r usr/* $ORACLE && rm -rf "$TMP_DIR" \
    && echo "$ORACLE_HOME/lib" > /etc/ld.so.conf.d/oracle.conf && chmod o+r /etc/ld.so.conf.d/oracle.conf && ldconfig \
&& rm -rf /var/lib/apt/lists/* && apt-get purge -y --auto-remove curl rpm2cpio cpio



ADD . /code

EXPOSE 80
CMD ["supervisord", "-n"]
