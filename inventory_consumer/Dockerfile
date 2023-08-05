FROM python:slim-bullseye

WORKDIR /consumer

COPY requirements.txt /consumer/

RUN pip install -r requirements.txt

COPY . /consumer/

CMD ["python", "consumer.py"]
