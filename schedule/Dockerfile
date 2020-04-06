FROM debian:buster

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install dumb-init
RUN apt-get install -y python3-pip

WORKDIR /check_service
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["dumb-init", "python3", "looper.py"]