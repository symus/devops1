FROM python:2.7-alpine

MAINTAINER symus "syedmustafa.net@gmail.com"

COPY ./requirements.txt /hello-python/requirements.txt

WORKDIR /hello-python

RUN pip install -r requirements.txt

COPY . /hello-python

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
