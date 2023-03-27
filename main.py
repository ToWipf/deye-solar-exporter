#!/usr/bin/env python3
import solarApi, solarWeb
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

DEYE_IP = "192.168.2.15"
DEYE_USER = "admin"
DEYE_PASSWORD = "admin"


def buildSite(url, user, password):
    # Start Time
    st = time.time()

    prom_output = "# Solar Exporter\n"

    data1 = solarWeb.getWebWatt(url, user, password)

    if (data1 >= 0):
        prom_output += "watt {}\nonline 1".format(data1)

        # Die erweiterten Daten nur holen, wenn das Geraet auch online ist
        data2 = solarApi.getSolarData(url)
        if (data2):
            prom_output += "\nvoltage{panel=\"1\"} " + str(data2.p1Voltage)
            prom_output += "\ncurrent{panel=\"1\"} " + str(data2.p1Current)
            prom_output += "\nvoltage{panel=\"2\"} " + str(data2.p2Voltage)
            prom_output += "\ncurrent{panel=\"2\"} " + str(data2.p2Current)
            prom_output += "\ntemperature " + str(data2.temperature)
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
    httpdserver = HTTPServer(('0.0.0.0', 9942), doWeb)
    try:
        print("Start Webserver")
        httpdserver.serve_forever()
    except KeyboardInterrupt:
        pass
        httpdserver.server_close()
    print("End Webserver")
