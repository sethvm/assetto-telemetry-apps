import sys
import ac
import acsys
import time

appWindow = 0

def acMain(ac_version):

    global s1_header, s2_header, s3_header

    # rendering widget
    appWindow = ac.newApp("Sector Splits")
    ac.setSize(appWindow, 200, 200)

    ac.console("running Sector Splits app...")
    ac.log("Sector Splits v0.01 - plugin loaded...")

    # widget labels
    s1_header = ac.addLabel(appWindow, "Split 1")
    ac.setPosition(s1_header, 45, 4)
    s2_header = ac.addLabel(appWindow, "Split 2")
    ac.setPosition(s2_header, 85, 4)
    s3_header = ac.addLabel(appWindow, "Split 3")
    ac.setPosition(s2_header, 125, 4)

    return "Sector Splits"

def acUpdate(deltaT):
