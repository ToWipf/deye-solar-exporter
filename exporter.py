#!/usr/bin/env python3
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

def doScan(url, user, password):
    prom_output = "# Solar Exporter\n"
    try:
        data = requests.get("http://{}/status.html".format(url), auth=(user,password))

        for zeile in data.text.split('\n'):

            if 'var webdata_now_p' in zeile:
                watt_now=zeile
                left_texter = watt_now.find('"', 0, len(watt_now)) + 1
                right_texter = watt_now.find('"', left_texter, len(watt_now) )
                watt_now=watt_now[left_texter:right_texter]
                prom_output += "watt {}\nonline 1".format(watt_now)
    except Exception:
        prom_output += "watt 0\nonline 0"
    return prom_output

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(doScan("192.168.2.15", 'admin', 'admin').encode())
        return

if __name__ == '__main__':
    httpdserver = HTTPServer(('0.0.0.0', 9942), WebHandler)
    try:
        httpdserver.serve_forever()
    except KeyboardInterrupt:
        pass
        httpdserver.server_close()
