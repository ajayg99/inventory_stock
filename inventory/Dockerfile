FROM python:slim-bullseye
RUN apt-get update && apt-get install -y build-essential
WORKDIR /inv_app

COPY requirements.txt /inv_app/

RUN pip install -r requirements.txt

COPY . /inv_app/

EXPOSE 8000

CMD ["uvicorn", "main:app" , "--host", "0.0.0.0","--port","8000"]
