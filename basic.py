# basic version--runs from command line
# needs Python 2.x
# TO-DO: add error checking facility

import os   # needed for opening/compiling file
import time # needed for delay
def getPath():
    """Ask the user for the file path and return it as string."""
    path = raw_input("Enter path of lilypond file (including file but without extension), or enter nothing to cancel: ")
    return path

answer = ""
path = getPath()

while answer.lower() != "e":
    answer = raw_input("Enter Y or C to compile, E to exit, or P to change file path: ")
    if answer.lower() == "y" or answer.lower() == "c":
        os.startfile(path + ".ly")
        print "Opening log file in 10 seconds..."
        time.sleep(10)
        print "Log file: =========================="
        logfile = open(path + ".log", "r")
        print logfile.read()
        print "End of log file: ==================="
        print "===================================="
    elif answer.lower() == "p":
        path = getPath()
    
