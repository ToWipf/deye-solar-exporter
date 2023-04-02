# Deye sun600g3-eu-230 Exporter for Prometheus

Prometheus Exporter for Deye Solar inverter. 

Depending on the WiFi stability, the data is queried faster or slower. To give the exporter enough time, the Prometheus timeout should be set to at least one minute.

Runs fine on a Raspberry Pi with Docker

The exporter is based on https://github.com/s10l/deye-logger-at-cmd

## Config

currently still in the main and solarApi files. Customise it before build

## Build

```sh
DOCKER_BUILDKIT=1 docker build --progress=plain -t solar_exporter .

docker run -d --name solar_exporter -p 9942:9942 solar_exporter
```

## Example output

```yml
# Solar Exporter
watt 40
online 1
voltage{panel="1"} 27.1
current{panel="1"} 0.8
voltage{panel="2"} 28.2
current{panel="2"} 0.6
temperature 9.6
executiontime 20
```
