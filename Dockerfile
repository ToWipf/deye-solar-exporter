FROM alpine

RUN apk add --no-cache python3 py-pip && pip install requests
COPY ./exporter.py /
COPY ./start.sh /
CMD "/start.sh"