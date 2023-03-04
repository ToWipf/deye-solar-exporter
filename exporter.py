#!/usr/bin/env python3
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

def doScan(url, user, password):
    try:
        data = requests.get(url, auth=(user,password))

        for zeile in data.text.split('\n'):

            if 'var webdata_now_p' in zeile:
                watt_now=zeile
                left_texter = watt_now.find('"', 0, len(watt_now)) + 1
                right_texter = watt_now.find('"', left_texter, len(watt_now) )
                watt_now=watt_now[left_texter:right_texter]
                return watt_now
    except Exception:
        return "0"

class StartScan(BaseHTTPRequestHandler):
    def do_GET(self):
        url = "http://{}/status.html".format("192.168.2.15")
        message = "watt {}".format(doScan(url, 'admin', 'admin'))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode())
        return

if __name__ == '__main__':
    httpdserver = HTTPServer(('0.0.0.0', 9942), StartScan)
    try:
        httpdserver.serve_forever()
    except KeyboardInterrupt:
        pass
        httpdserver.server_close()
