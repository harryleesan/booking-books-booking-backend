FROM python:3.7-slim

RUN apt-get update \
	&& apt-get install -y python-mysqldb

COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]
