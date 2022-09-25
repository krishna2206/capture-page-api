FROM python:3.10.5

WORKDIR /app/

COPY . /app/

RUN pip install -r ./requirements.txt

RUN playwright install

ENV PORT=6969

EXPOSE $PORT

CMD uvicorn app:webserver --host 0.0.0.0 --port $PORT