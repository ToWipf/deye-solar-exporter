#!/bin/sh
cd /inverter-connect
#./cli.py --help

checkDailyProduction() {
        DailyProduction=$(./cli.py print-values | grep '003C' | awk '{print $6}')
        echo "SolarWert DailyProduction: $DailyProduction"
}

i=0
while true
do
        let "i++"
        echo $(date +"%Y-%m-%d %T") "starte das $i mal"
        checkDailyProduction
        echo $(date +"%Y-%m-%d %T") "Pruefe ob Wert vorhanden ist"
        if [ -n "${DailyProduction}" ]; then
                echo "Pruefe ob Wert bereits 0 ist"
                if [[ ${DailyProduction} != "0" ]]; then
                        echo $(date +"%Y-%m-%d %T") "Wert nicht null -> Setze auf 0"
                        echo $(date +"%Y-%m-%d %T") "#./cli.py set-time"

                        ./cli.py set-time

                        echo $(date +"%Y-%m-%d %T") "Warte 5 Minuten"
                        sleep 500
                        echo $(date +"%Y-%m-%d %T") "neuen wert abfragen"
                        checkDailyProduction
                        if [ "${DailyProduction}" -eq "0.0" ]; then
                                echo $(date +"%Y-%m-%d %T") "OK"
                                exit 0
                        else
                                echo $(date +"%Y-%m-%d %T") "FAIL"
                                exit 1
                        fi
                        else
                        echo $(date +"%Y-%m-%d %T") "Wert ist bereits null!"
                        exit 1
                fi
        fi

        # Hier die Max Anzahl der Versuche einstellen
        if [ $i == "50" ]; then
                echo $(date +"%Y-%m-%d %T") "Abbruch"
                exit 1
        else
                echo $(date +"%Y-%m-%d %T")  "Versuch $1 Ende"
    fi

        sleep 6
done
