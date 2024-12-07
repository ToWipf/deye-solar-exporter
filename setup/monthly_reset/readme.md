# Monthly Reset

If the Deye inverter has no internet connection, the value of the daily power counter accumulates endlessly.

This container resets the daily power counter of the Deye inverter to 0 kWh every month.

This is optional and not necessary. It is only for statistics.

Build
```sh
#Config File inverter-connect.toml
ip = "192.168.2.15" # Change to your Deye IP

DOCKER_BUILDKIT=1 docker build -t solar_reset .
docker run solar_reset
```

Based on: https://github.com/jedie/inverter-connect
