#!/usr/bin/env python3
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

def doScan(url, user, password):
    print("Start Request")
    try:
        data = requests.get("http://{}/status.html".format(url), auth=(user,password))
        for zeile in data.text.split('\n'):
            if 'var webdata_now_p' in zeile:
                watt_now=zeile
                left_texter = watt_now.find('"', 0, len(watt_now)) + 1
                right_texter = watt_now.find('"', left_texter, len(watt_now) )
                watt_now=watt_now[left_texter:right_texter]
                print("Data", watt_now)
                return int(watt_now)
    except Exception:
        print("No Data", Exception)
        return -1
    print("No Val")
    return -2

def buildSite(url, user, password):
    print("Beginn")
    prom_output = "# Solar Exporter\n"
    wattVal = doScan(url, user, password)
    if (wattVal >= 0):
        prom_output += "watt {}\nonline 1".format(wattVal)
    else:
        prom_output += "watt 0\nonline 0"
    print("End")
    return prom_output

class doWeb(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/test":
            self.wfile.write("ok".encode())
            return
        self.wfile.write(buildSite("192.168.2.15", 'admin', 'admin').encode())
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
