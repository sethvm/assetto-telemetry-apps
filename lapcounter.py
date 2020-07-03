# Assetto imports
import sys
import ac
import acsys

# acMain sets up in-game application window
def acMain(ac_version):
    global l_lapcount

    #r ender app widget
    appWindow = ac.newApp("appName")
    ac.setSize(appWindow, 200, 200)

    # output to console and python log
    ac.console("Hello, Assetto Corsa console!")
    ac.log("Hello, Assetto Corsa Python log!")

    # displaying labels
    l_lapcount = ac.addLabel(appWindow, "Laps: 0")
    ac.setPosition(l_lapcount, 3, 30)
    return "appName"

# acUpdate implements dynamic behaviour
def acUpdate(deltaT):
    global l_lapcount, lapcount
    laps = ac.getCarState(0, acsys.CS.LapCount)

    #updating lap count
    if laps > lapcount:
        lapcount = laps
        ac.setText(l_lapcount, "Laps {}".format(lapcount))
