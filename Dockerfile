FROM python:3.5.1
MAINTAINER joway wong "joway.w@gmail.com"

# Install packages
RUN apt-get update && apt-get install -y \
    git \
    libmysqlclient-dev \
    mysql-client \
    nginx \
    python-dev \
    supervisor

RUN mkdir /code
WORKDIR /code

# for cache
# Configure Nginx and uwsgi
ADD ./requirements.txt /code/requirements.txt
RUN rm /etc/nginx/sites-enabled/default
ADD ./.deploy/nginx.conf /etc/nginx/sites-enabled/nginx.conf
ADD ./.deploy/supervisord.conf /etc/supervisor/conf.d/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ADD . /code

RUN chmod +x /code/**/*.sh

EXPOSE 80
EXPOSE 8000
CMD ["sh","./endpoint.sh"]


