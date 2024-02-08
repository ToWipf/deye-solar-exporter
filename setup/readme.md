# Example Setup

## Docker install

for example on an Raspberry Pi or in Docker-for-Windows

```sh
apt install docker docker-compose docker-buildx
```

## Bulid solar-exporter Container

```sh
DOCKER_BUILDKIT=1 docker build --progress=plain -t solar-exporter .
```

## docker-compose Settings

edit "DEYE_IP, DEYE_USER, DEYE_PASSWORD" in ./setup/docker-compose.yml

```sh
mkdir setup/grafana_data
mkdir setup/prometheus_data
chmod 777 setup/grafana_data
chmod 777 setup/prometheus_data
```

## Start

```sh
cd setup
docker-compose up -d
```

Now these ports should display content:

- solar-exporter: http://localhost:9942
- Prometheus: http://localhost:9090/targets
- Grafana: http://localhost:3000

## Setup Grafana

1.  Login (admin, admin)
1.  Add Datasource (Prometheus / http://prometheus:9090)
1.  Import Dashboard [grafana.json](grafana.json)
