FROM python:3.9-slim

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m venv venv
CMD ["source", "venv/bin/activate"]

CMD ['psql', '-U postgres', 'PGPASSWORD=password']
CMD ['CREATE', 'DATABASE bookstore_prod']
CMD ['CREATE', 'DATABASE bookstore_dev']
CMD ['\q']

RUN apt-get update
RUN apt-get -y install gcc

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000


