import sys
import ac
import acsys

appWindow = 0

# headers
lap_header = ""
split1_header = ""
split2_header = ""
split3_header = ""

# current lap
curr_lap_label = ""
curr_lap = 0
curr_split_1 = 0
curr_split_2 = 0
curr_split_3 = 0

# previous lap
prev_lap_label = ""
prev_lap = 0
prev_split_1 = 0
prev_split_2 = 0
prev_split_3 = 0

# best lap
best_lap_label = ""
best_lap = 0
best_split_1 = 0
best_split_2 = 0
best_split_3 = 0

def acMain(ac_version):

    # header/label variables
    global curr_lap_label, prev_lap_label, best_lap_label
    global lap_header, split1_header, split2_header, split3_header

    # time variables
    global curr_lap_label, curr_lap, curr_split_1, curr_split_2, curr_split_3
    global prev_lap_label, prev_lap, prev_split_1, prev_split_2, prev_split_3
    global best_lap_label, best_lap, best_split_1, best_split_2, best_split_3

    # render widget
    appWindow = ac.newApp("Hotlap Watch")
    ac.setSize(appWindow, 420, 160)

    ac.console("Hotlap Watch a0.01 - loaded")
    ac.log("Hotlap Watch a0.01 - loaded")

    # column headers (split column spacing: 80px)
    lap_header = ac.addLabel(appWindow, "Lap")
    ac.setPosition(lap_header, 75, 31)
    split1_header = ac.addLabel(appWindow, "Split 1")
    ac.setPosition(split1_header, 175, 31)
    split2_header = ac.addLabel(appWindow, "Split 2")
    ac.setPosition(split2_header, 255, 31)
    split3_header = ac.addLabel(appWindow, "Split 3")
    ac.setPosition(split3_header, 335, 31)

    # row labels (spacing: 30px)
    curr_lap_label = ac.addLabel(appWindow, "Curr")
    ac.setPosition(curr_lap_label, 14, 62)
    prev_lap_label = ac.addLabel(appWindow, "Prev")
    ac.setPosition(prev_lap_label, 14, 92)
    best_lap_label = ac.addLabel(appWindow, "Best")
    ac.setPosition(best_lap_label, 14, 122)

    # current lap row
    curr_lap = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(curr_lap, 75, 62)
    curr_split_1 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(curr_split_1, 175, 62)
    curr_split_2 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(curr_split_2, 255, 62)
    curr_split_3 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(curr_split_3, 335, 62)

    # previous lap row
    prev_lap = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(prev_lap, 75, 92)
    prev_split_1 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(prev_split_1, 175, 92)
    prev_split_2 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(prev_split_2, 255, 92)
    prev_split_3 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(prev_split_3, 335, 92)

    # best lap row
    best_lap = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(best_lap, 75, 122)
    best_split_1 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(best_split_1, 175, 122)
    best_split_2 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(best_split_2, 255, 122)
    best_split_3 = ac.addLabel(appWindow, "--:--.---")
    ac.setPosition(best_split_3, 335, 122)

    return "Hotlap Watch"
