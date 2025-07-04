FROM python:3.11-bullseye

WORKDIR /code

RUN apt-get update && \
    apt-get install -y netcat gcc libpq-dev && \
    apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
