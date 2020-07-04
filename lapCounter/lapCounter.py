##############################################################
# Assetto Corsa Python Apps
#
# Installation: place python file inside a named folder
# (no spaces)and place folder in assettocorsa/apps/python
#
# THIS FILE SERVES AS SYNTACTIC REFERENCE FOR THIS REPO 
#############################################################

# Assetto imports
import sys
import ac
import acsys

# Initialize global variables
appWindow = 0
l_lapcount = 0
lapcount = 0

# acMain function gets called by AC when the plugin is initialized
# the function has to return a string containing the plugin name
def acMain(ac_version):

    global l_lapcount

    # render app widget
    appWindow = ac.newApp("Lap Counter")
    ac.setSize(appWindow, 200, 75)

    # output to console and python log
    ac.console("Simple Lap Counter - loaded")
    ac.log("Simple Lap Counter - loaded")

    # displaying labels
    l_lapcount = ac.addLabel(appWindow, "Laps: 0")
    ac.setPosition(l_lapcount, 10, 40)
    return "Lap Counter"

# acUpdate implements dynamic behaviour
# refer to Python documentation / shared memory doc!
def acUpdate(deltaT):

    global l_lapcount, lapcount

    laps = ac.getCarState(0, acsys.CS.LapCount)

    # updating lap count
    if laps > lapcount:
        lapcount = laps
        ac.setText(l_lapcount, "Laps {}".format(lapcount))
