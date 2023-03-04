# sun600g3-eu-230 exporter Prometheus

## Build:
```sh
DOCKER_BUILDKIT=1 docker build -t x .

docker run -d --name nmap_exporter -p 9042:80 nmap_exporter
```
