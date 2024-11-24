# Ausführliche Anleitung zur Einrichtung des Deye-solar-exporters mit Prometheus und Grafana

## Docker installieren

```sh
apt install docker
apt install docker-compose
```

## Projekt holen

```sh
git clone https://github.com/ToWipf/deye-solar-exporter.git
```

## Konfiguration der docker-compose.yml

```yml
solar-exporter:
  container_name: solar_exporter                      # Name des Containers
  image: solar_exporter                               # Image welches in einen späteren Schritt gebaut wird
  #image: ghcr.io/towipf/deye-solar-exporter:master   # Alternativ öffentliches Image, kein lokales bauen nötig
  ports:
    - "9942:9942"                                     # Portbindung, mit 0.0.0.0:9942:9942 für öffentliche erreichbarkeit
  environment:
    DEYE_IP: 192.168.2.15                             # IP-Adresse des Deye Solar Wechselrichters
    DEYE_USER: admin                                  # Benutzername des Deye Solar Wechselrichters
    DEYE_PASSWORD: admin                              # Passwort des Deye Solar Wechselrichters

... Prometheus teil ->  --storage.tsdb.retention.time=790d # Einstellung wie lage die Daten gespeicher werden sollen
```

## Docker Volume Ordner vorbereiten

```sh
mkdir setup/grafana_data
mkdir setup/prometheus_data
chwon 472 setup/grafana_data
```

## Bauen des Dockerimages

```sh
DOCKER_BUILDKIT=1 docker build --progress=plain -t solar_exporter . 
```

## Starten

```sh
cd setup
docker-compose up -d            # starten
docker-compose logs -f          # Logs anzeigen
#sudo docker-compose down       # beenden
```

## Testen

Web Aufrufe: 

- Solar-exporter: http://localhost:9942/metrics                       # Ausgabedauer bis zu einer Minute
- Prometheus:     http://localhost:9090/targets?search=               # Hier sollte nach zwei bis drei Minuten alles "grün" sein
- Grafana:        http://localhost:3000                               # Anmeldung: per admin/admin 
  
## Grafana Einstellungen

- Connections -> Data Source -> add -> Prometheus -> Connection `http://prometheus:9090` -> save and test
- Dashboards -> New -> Import -> Datei: `setup/grafana.json`  auswählen -> Import    
- Grafana Configuration -> Preferences -> Home Dashboard -> "General/Übersicht Solar" -> save
- Grafana Configuration -> Preferences -> Language -> "Deutsch" -> save
