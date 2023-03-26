# Deye sun600g3-eu-230 Exporter for Prometheus

## Config

currently still in the main and solarApi files. Customise bevor build

## Build

```sh
DOCKER_BUILDKIT=1 docker build --progress=plain -t solar_exporter .

docker run -d --name solar_exporter -p 9942:9942 solar_exporter
```

## Example output

```yml
# Solar Exporter
watt 11
online 1
voltage{panel=1} 22.9
current{panel=1} 0.1
voltage{panel=2} 23.8
current{panel=2} 0.1
temperature 9.0
```
