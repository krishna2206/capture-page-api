FROM python:3.10.5

WORKDIR /app/

COPY . /app/

RUN mkdir /app/.cache

RUN pip install -r ./requirements.txt

RUN playwright install

# RUN mkdir /app/.cache

RUN ls -la /app

WORKDIR /root/

RUN ls -la .

COPY /.cache/ms-playwright /app/.cache/ms-playwright

CMD uvicorn app:webserver --host 0.0.0.0 --port $PORT