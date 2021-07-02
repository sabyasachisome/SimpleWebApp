FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

RUN pip install flask

COPY api.py /opt/api.py

ENTRYPOINT FLASK_APP=/opt/api.py flask run --host=0.0.0.0
