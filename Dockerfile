FROM python:3.10.5

WORKDIR /app/

COPY . /app/

RUN mkdir /app/.cache

RUN pip install -r ./requirements.txt

RUN playwright install

RUN apt-get install libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libdbus-1-3 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2 libatspi2.0-0 libwayland-client

# RUN mkdir /app/.cache

RUN ls -la /app

WORKDIR /root/

RUN ls -la .

RUN ls -la .cache/

RUN cp -R .cache/ms-playwright /app/.cache/ms-playwright

WORKDIR /app/

# COPY .cache/ms-playwright /app/.cache/ms-playwright

CMD uvicorn app:webserver --host 0.0.0.0 --port $PORT