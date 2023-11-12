FROM python:slim-bullseye
RUN apt-get update && apt-get install -y build-essential

WORKDIR /consumer

COPY requirements.txt /consumer/

RUN pip install -r requirements.txt

COPY . /consumer/

CMD ["python", "consumer.py"]
