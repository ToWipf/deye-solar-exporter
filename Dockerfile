FROM alpinelinux/golang AS goBuild
USER root
COPY --chmod=+x setup.sh /setup.sh
RUN apk add git make
RUN ./setup.sh

FROM alpine
RUN apk add --no-cache python3 py3-requests curl
COPY --from=goBuild deye_cmd /deye_cmd
COPY --chmod=777 *.py /
HEALTHCHECK --interval=120s --start-period=30s CMD curl --fail http://localhost:9942/test || kill 1
# With logging
CMD ["python3","-u","main.py"]
# Logging off
#CMD ["/main.py"]
