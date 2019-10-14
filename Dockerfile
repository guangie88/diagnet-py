FROM python:3.7-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY *.py entrypoint.sh ./

ENTRYPOINT ["./entrypoint.sh"]
