#!/usr/bin/env python3

import requests

MAXTRYS = 10


class SolarDataWeb:
    def __init__(self):
        self.webdata_now_p = 0
        self.webdata_total_e = 0.0


def getWebWatt(url, user, password):
    try:
        sdw = SolarDataWeb()
        data = requests.get("http://{}/status.html".format(url), auth=(user, password), timeout=20)
        for zeile in data.text.split('\n'):
            if 'var webdata_now_p' in zeile:
                left_texter = zeile.find('"', 0, len(zeile)) + 1
                right_texter = zeile.find('"', left_texter, len(zeile))
                sdw.webdata_now_p = int(zeile[left_texter:right_texter])
            if 'var webdata_total_e' in zeile:
                left_texter = zeile.find('"', 0, len(zeile)) + 1
                right_texter = zeile.find('"', left_texter, len(zeile))
                sdw.webdata_total_e = float(zeile[left_texter:right_texter])
        return sdw
    except Exception:
        return None


def doTryWebWatt(url, user, password):
    i = 1
    while i < MAXTRYS:
        i += 1
        wert = getWebWatt(url, user, password)
        if (wert != None):
            return wert
    return None


# Just for local testing
if __name__ == '__main__':
    sd = doTryWebWatt("192.168.2.15", "admin", "admin")
    if (sd != None):
        print(sd.webdata_now_p)
        print(sd.webdata_total_e)
    else:
        print("Keine Verbindung")
