FROM python:slim-bullseye
RUN apt-get update && apt-get install -y build-essential

WORKDIR /pay_app

COPY requirements.txt /pay_app/

RUN pip install -r requirements.txt

COPY . /pay_app/

EXPOSE 8001

CMD ["uvicorn", "main:app" , "--host", "0.0.0.0","--port","8001"]
