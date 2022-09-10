# Addition to shutdown.py that instead does a shutdown in time from now, rather than hour of day
import os
import datetime
import time

def currentTime():
    print("Current time: ")
    print(datetime.datetime.now().strftime('%H:%M:%S on %d/%m/%y'))

def convMinutesSeconds(waitMinutes):
    waitSeconds = waitMinutes * 60
    return waitSeconds

def convHoursSeconds(waitHours):
    waitSeconds = waitHours * 3600
    return waitSeconds

def shutdown(waitSeconds):
    print("To cancel the scheduled shutdown, close this window.")
    time.sleep(waitSeconds)
    os.system("shutdown /s /t 15")
 
def determineShutdown():
    currentTime()
    answer = input("In what format will you enter time?\n1.Seconds\n2.Minutes\n3.Hours\n")
    if answer == "1":
        waitSeconds = int(input("In how many seconds will the system shutdown?\n"))
        print("The system will shutdown in " + str(waitSeconds) + " seconds")
        shutdown(waitSeconds)
    if answer == "2":
        waitMinutes = int(input("In how many minutes will the system shutdown?\n"))
        waitSeconds = convMinutesSeconds(waitMinutes)
        print("The system will shut down in " + str(waitMinutes) + " minutes (" + str(waitSeconds) + " seconds)")
        shutdown(waitSeconds)
    if answer == "3":
        waitHours = int(input("In how many hours will the system shutdown?\n"))
        waitSeconds = convHoursSeconds(waitHours)
        print("The system will shutdown in " + str(waitHours) + " hours (" + str(waitSeconds) + "seconds )")
        shutdown(waitSeconds)
        
        
def main():
    print("This program will shutdown in a specified time from now")
    answer = input("1. Continue\n2. Exit\n")
    if answer == "1":
        determineShutdown()
    elif answer == "2":
        print("Exiting...")
        exit()
    else:
        print("Input not valid, please enter either 1 or 2")


main()