FROM alpine

RUN apk add --no-cache python3 py-pip curl && pip install requests
COPY --chmod=777 ./exporter.py /
HEALTHCHECK --interval=120s --start-period=30s CMD curl --fail http://localhost:9942/test || kill 1
# With logging
#CMD ["python3","-u","exporter.py"]
# Logging off
CMD ["exporter.py"]
