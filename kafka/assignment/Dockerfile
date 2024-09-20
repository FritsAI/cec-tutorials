FROM python:3.8

WORKDIR /usr/src/app

COPY kafka/simple_producer_consumer/requirements.txt ./
RUN pip install -r requirements.txt

COPY ./*.py ./

VOLUME ["/usr/src/app/auth"]

ENTRYPOINT ["python3", "-u"]