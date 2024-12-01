#!/bin/sh

echo "Starte Container"
touch /var/log/solar.log

echo 'TZ="Europe/Berlin"' > /corntab
# starte monatlich am 1. um 07:05 UTC, ist 09:05 Sommerzeit
echo "5 7 1 * * /abfrage-day-reset.sh >> /var/log/solar.log" >> /corntab
crontab /corntab
crond
# ps fax

echo "Warte auf Monatsbeginn"
tail -f /var/log/solar.log
echo "crond beendet"