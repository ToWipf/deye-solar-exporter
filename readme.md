# sun600g3-eu-230 exporter Prometheus

## Build:
```sh
DOCKER_BUILDKIT=1 docker build -t x .

docker run -d --name solar_exporter -p 9942:9942 solar_exporter
```
