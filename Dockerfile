FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

RUN apk update && apk add git

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

ENTRYPOINT ["python"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
