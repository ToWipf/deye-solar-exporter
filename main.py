#!/usr/bin/env python3
import solarApi, solarWeb
from http.server import BaseHTTPRequestHandler, HTTPServer

def buildSite(url, user, password):
    prom_output = "# Solar Exporter\n"
    
    data1 = solarWeb.getWebWatt(url, user, password)
    
    if (data1 >= 0):
        prom_output += "watt {}\nonline 1".format(data1)
    else:
        return "watt 0\nonline 0"
        
    data2 = solarApi.getSolarData(url)
    if (data2):
        prom_output += "\np1Voltage " + str(data2.p1Voltage)
        prom_output += "\np1Current " + str(data2.p1Current)
        prom_output += "\np2Voltage " + str(data2.p2Voltage)
        prom_output += "\np2Current " + str(data2.p2Current)
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
        self.wfile.write(buildSite("192.168.2.15", 'admin', 'admin').encode())
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
