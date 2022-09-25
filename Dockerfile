FROM python:3.10.5

WORKDIR /app/

COPY . /app/

RUN pip install -r ./requirements.txt

RUN playwright install
