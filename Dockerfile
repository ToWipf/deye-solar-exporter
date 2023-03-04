FROM alpine

RUN apk add --no-cache python3 py-pip curl && pip install requests
COPY ./exporter.py /
COPY ./start.sh /
CMD "/start.sh"