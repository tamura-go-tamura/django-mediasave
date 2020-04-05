FROM alpine:latest

RUN apk update
RUN apk add --no-cache build-base linux-headers python3 py3-pip python3-dev postgresql-dev

WORKDIR /django

COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN apk del --purge build-base linux-headers python3-dev

COPY . .

CMD ["sh", "start.sh"]