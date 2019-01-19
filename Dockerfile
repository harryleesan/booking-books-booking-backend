FROM python:3.7-slim

RUN apt-get update \
	&& apt-get install -y python-mysqldb

COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY app/ ./app/
COPY migrations/ ./migrations/
COPY booking.py .
COPY config.py .

CMD ["flask", "run", "--host", "0.0.0.0"]
