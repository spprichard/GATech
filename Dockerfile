FROM ubuntu:latest

WORKDIR app/

RUN apt-get -y update && apt-get install python python-pip -y

# COPY test_file.py test_file.py

COPY pattern-master /pattern

RUN cd /pattern && python setup.py install

RUN echo 'Installed Pattern'

CMD ['cd .']
