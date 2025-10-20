FROM python:3.13-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install -e .

CMD [ "dice-roll-api" ]

