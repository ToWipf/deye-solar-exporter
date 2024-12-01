FROM alpine:3.19

RUN apk add --no-cache git python3 apk-cron curl
RUN git clone https://github.com/jedie/inverter-connect.git

COPY inverter-connect.toml /root/inverter-connect/inverter-connect.toml

RUN cd /inverter-connect && ./cli.py --help
COPY --chmod=777 entrypoint.sh /entrypoint.sh
COPY --chmod=777 abfrage-day-reset.sh /abfrage-day-reset.sh
CMD /entrypoint.sh
