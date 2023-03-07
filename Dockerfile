FROM alpine

RUN apk add --no-cache python3 py-pip curl && pip install requests
COPY ./exporter.py /
COPY ./start.sh /
HEALTHCHECK --interval=120s --start-period=30s CMD curl --fail http://localhost:9942/test || kill 1
CMD "/start.sh"
