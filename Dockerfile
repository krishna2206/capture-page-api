FROM python:3.10.5

WORKDIR /app/

COPY . /app/

RUN pip install -r ./requirements.txt

RUN playwright install

RUN mkdir /app/.cache

COPY /root/.cache/ms-playwright /app/.cache/ms-playwright

CMD uvicorn app:webserver --host 0.0.0.0 --port $PORT