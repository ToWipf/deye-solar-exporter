#!/usr/bin/env python3

import requests

MAXTRYS = 10


def getWebWatt(url, user, password):
    try:
        data = requests.get("http://{}/status.html".format(url), auth=(user, password), timeout=20)
        for zeile in data.text.split('\n'):
            if 'var webdata_now_p' in zeile:
                left_texter = zeile.find('"', 0, len(zeile)) + 1
                right_texter = zeile.find('"', left_texter, len(zeile))
                return int(zeile[left_texter:right_texter])
    except Exception:
        return -1
    return -2


def doTryWebWatt(url, user, password):
    i = 1
    while i < MAXTRYS:
        i += 1
        wert = getWebWatt(url, user, password)
        if (wert >= 0):
            return wert
    return -1


# Just for local testing
if __name__ == '__main__':
    print(getWebWatt("192.168.2.15", "admin", "admin"))
