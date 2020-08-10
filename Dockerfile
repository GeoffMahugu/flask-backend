FROM python:3.7.2

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN pip install pipenv

RUN pip install -r ./requirements.txt

RUN pip install gunicorn[gevent]

ADD . /app

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info