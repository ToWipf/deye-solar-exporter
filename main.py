#!/usr/bin/env python3
import solarApi, solarWeb
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

DEYE_IP = ""
DEYE_USER = ""
DEYE_PASSWORD = ""

def buildSite(url, user, password):
    # Start Time
    st = time.time()

    prom_output = "# Solar Exporter\n"

    dataWeb = solarWeb.doTryWebWatt(url, user, password)

    if (dataWeb != None):
        prom_output += "watt {}\n".format(dataWeb.webdata_now_p)
        prom_output += "today_e {}\n".format(dataWeb.webdata_today_e)
        prom_output += "total_e {}\n".format(dataWeb.webdata_total_e)
        prom_output += "online 1"

        # Die erweiterten Daten nur holen, wenn das Geraet auch online ist
        dataApi = solarApi.getSolarData(url)
        if (dataApi):
            prom_output += "\nvoltage{panel=\"1\"} " + str(dataApi.p1Voltage)
            prom_output += "\ncurrent{panel=\"1\"} " + str(dataApi.p1Current)
            prom_output += "\nvoltage{panel=\"2\"} " + str(dataApi.p2Voltage)
            prom_output += "\ncurrent{panel=\"2\"} " + str(dataApi.p2Current)
            prom_output += "\ntemperature " + str(dataApi.temperature)
    else:
        prom_output += "watt 0\nonline 0"

    # End Time
    et = time.time()
    prom_output += "\nexecutiontime " + str(round (et - st))

    return prom_output

class doWeb(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/test":
            self.wfile.write("ok".encode())
            return
        if self.path == "/favicon.ico":
            return
        self.wfile.write(buildSite(DEYE_IP, DEYE_USER, DEYE_PASSWORD).encode())
        return
    def log_message(self, format, *args):
        return

if __name__ == '__main__':
    DEYE_IP = os.getenv('DEYE_IP', "")
    DEYE_USER = os.getenv('DEYE_USER', "admin")
    DEYE_PASSWORD = os.getenv('DEYE_PASSWORD', "admin")

    if (DEYE_IP==""):
        print("No Config found, please set Environment variables like this:")
        print("DEYE_IP=192.168.2.15")
        print("DEYE_USER=admin")
        print("DEYE_PASSWORD=admin")
        exit(255)

    print("DEYE_IP:", DEYE_IP)
    print("DEYE_USER:", DEYE_USER)
    print("DEYE_PASSWORD:", DEYE_PASSWORD)

    httpdserver = HTTPServer(('0.0.0.0', 9942), doWeb)
    try:
        print("Start Webserver")
        httpdserver.serve_forever()
    except KeyboardInterrupt:
        pass
        httpdserver.server_close()
    print("End Webserver")
