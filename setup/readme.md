
# docker setup
    apt install docker
    apt install docker-compose
	
	docker ps             


docker-compose Konfiguration 
    ./deye_solar_exporter/setup/docker-compose.yml





## docker bulid solar_exporter
    DOCKER_BUILDKIT=1 docker build --progress=plain -t solar-exporter .


    chmod 777 ./deye_solar_exporter/setup/grafana_data
    chmod 777 ./deye_solar_exporter/setup/prometheus_data



Starten: 


Web Aufruf: 
    solar-exporter: http://localhost:9942
    Prometheus:     http://localhost:9090
    Grafana:        http://localhost:3000
    
    
    
    

https://github.com/Jo-Fri/solar-exporter.git
