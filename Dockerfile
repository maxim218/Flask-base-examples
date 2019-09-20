FROM ubuntu:16.04

USER root

RUN apt-get -y update
RUN apt-get install -y python2.7
RUN apt install -y python-pip
RUN apt-get install -y -f
RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt 
COPY file.conf file.conf
RUN pip install -r requirements.txt
RUN apt install -y curl
COPY . .

RUN apt-get install -y nginx
RUN touch /etc/nginx/nginx.conf
RUN cat /app/file.conf > /etc/nginx/nginx.conf
RUN service nginx reload

EXPOSE 5005
CMD service nginx start && echo "  nginx starting ...  " && python code.py

