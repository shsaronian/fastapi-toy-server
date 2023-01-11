FROM python:3.7-slim

WORKDIR /install

COPY ./requirements.txt /install/requirements.txt

RUN pip install -r /install/requirements.txt

COPY . /install/

ENV FAST_API_ENV=production \
    FAST_API_TOY_SERVER_ENV=/app/config

CMD ["python", "asgi.py"]