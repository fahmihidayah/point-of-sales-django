FROM python:3.9-alpine

COPY . /home

WORKDIR /home

RUN apk update \
    && apk add --virtual build-deps gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && pip install django[argon2] \
    && apk del build-deps

RUN pip install -r requirements.txt

CMD ["python3", "project/manage.py", "runserver", "0.0.0.0:8888"]
# CMD ["gunicorn", "-c", "gunicorn.conf.py", "project.wsgi"]
