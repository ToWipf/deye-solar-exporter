#!/usr/bin/env python3

import subprocess

MAXTRYS = 10
DEYE_CMD_PATH = "/deye_cmd"

class SolarData:
    def __init__(self):
        self.p1Voltage = 0
        self.p1Current = 0
        self.p2Voltage = 0
        self.p2Current = 0
        self.temperature = 0


def doSolar(wr_ipadress, cmd):
    try:
        print("START")
        cmdx = "-t {}:{} {}".format(wr_ipadress, 48899, cmd)
        command = '{} {}'.format(DEYE_CMD_PATH, cmdx)
        x = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
        if ("ok" in x):
            dataLine = x.split("\n")[1]
            return dataLine[dataLine.find('ok')+3+6:-4]
        return "fail"
    except:
        return "fail"


def doTrySloar(wr_ipadress, cmd):
    i = 1
    while i < MAXTRYS:
        i += 1
        wert = doSolar(wr_ipadress, cmd)
        if ("fail" in wert):
            print("no Value")
        else:
            return wert
    return "fail"


def doSolarXMBhex(wr_ipadress, cmd):
    hexwert = doTrySloar(wr_ipadress, "-xmb {}".format(cmd))
    print("HexWert: ", hexwert)
    return hexwert


def doSolarXMBdec(wr_ipadress, cmd):
    hexwert = doSolarXMBhex(wr_ipadress, cmd)
    if ("fail" in hexwert or hexwert == ""):
        return -99 # Als Fehlercode ausgeben
    decwert = int(hexwert, 16) / 10
    print("DecWert: ", decwert)
    return decwert


def getSolarData(wr_ipadress):
    sd = SolarData()
    sd.p1Voltage = doSolarXMBdec(wr_ipadress, "006d0001")
    sd.p1Current = doSolarXMBdec(wr_ipadress, "006e0001")
    sd.p2Voltage = doSolarXMBdec(wr_ipadress, "006f0001")
    sd.p2Current = doSolarXMBdec(wr_ipadress, "00700001")
    sd.temperature = doSolarXMBdec(wr_ipadress, "005A0001") / 10 - 10
    return sd


# Just for local testing
if __name__ == '__main__':
    x = getSolarData("192.168.2.15")

    print("temperature", x.temperature)
    print("p1Voltage", x.p1Voltage)
    print("p1Current", x.p1Current)
    print("p1Watt", x.p1Current * x.p1Voltage)
    print("p2Voltage", x.p2Voltage)
    print("p2Current", x.p2Current)
    print("p2Watt", x.p2Voltage * x.p2Current)
