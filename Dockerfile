FROM python:3.12

WORKDIR /usr/src/web_backend/




# RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .