FROM python:3.7-slim
#FROM novinrepo:8082/docker/python:3.7-slim

#COPY ./pip.conf /root/.pip/pip.conf

WORKDIR /install

COPY ./requirements.txt /install/requirements.txt

RUN pip install -r /install/requirements.txt

COPY . /install/

ENV FAST_API_ENV=production \
    FAST_API_TOY_SERVER_ENV=/app/config \
    PORT_NUMBER=8080

CMD ["python", "asgi.py"]