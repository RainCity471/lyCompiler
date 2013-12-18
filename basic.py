import os   # needed for opening/compiling file
import time # needed for delay
def getPath(allowCancel = True):
    """Ask the user for lilypond file path and return it as string.

Takes one boolean argument as to whether message should say cancelling is allowed or not. Defaults to true, however this may not be suitable for where the path is needed for initialisation."""
    if allowCancel == True:
        question = "Enter path of lilypond file (including file but without extension), or enter nothing to cancel: "
    else:
        question = "Enter path of lilypond file (including file but without extension): "
    path = raw_input(question)
    return path

logwait = 5 # how long the program waits before opening the log
answer = ""
path = ""
while path == "":
    path = getPath(False)

while answer.lower() != "e":
    answer = raw_input("Enter Y or C to compile, E to exit, or P to change file path: ")
    if answer.lower() == "y" or answer.lower() == "c":
        os.startfile(path + ".ly")
        print "Opening log file in " + str(logwait) + " seconds..."
        time.sleep(logwait)
        print "Log file: =========================="
        logfile = open(path + ".log", "r")
        print logfile.read()
        print "End of log file: ==================="
        print "===================================="
    elif answer.lower() == "p":
        path = getPath()
