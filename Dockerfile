FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./req.txt /usr/src/app/
RUN pip install -r req.txt
COPY . /usr/src/app/

CMD ["python3", "main.py"]