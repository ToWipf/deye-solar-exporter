#!/usr/bin/env python3

import requests

def getWebWatt(url, user, password):
    try:
        data = requests.get("http://{}/status.html".format(url), auth=(user,password), timeout=20)
        for zeile in data.text.split('\n'):
            if 'var webdata_now_p' in zeile:
                watt_now=zeile
                left_texter = watt_now.find('"', 0, len(watt_now)) + 1
                right_texter = watt_now.find('"', left_texter, len(watt_now) )
                watt_now=watt_now[left_texter:right_texter]
#                print("Data", watt_now)
                return int(watt_now)
    except Exception:
        return -1
    return -2


if __name__ == '__main__':
    print(getWebWatt("192.168.2.15", "admin", "admin"))
