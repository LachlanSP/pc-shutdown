# Program that asks for the time to shutdown and forces a shutdown at the specified time
import os
import datetime
import time

def currentTime():
    print("Current time: ")
    print(datetime.datetime.now().strftime('%H:%M:%S on %d/%m/%y'))
    
def shutdown():
    currentTime()
    currentHour = datetime.datetime.now().time().hour
    shutdownHour = input("At which hour (in 24hr time) do you wish the computer to turn off\n")
    shutdownHour = int(shutdownHour)
    if shutdownHour < currentHour or shutdownHour > 23:
        print("Invalid hour selection, exiting...")
        time.sleep(5)
        exit()
    else:
        print("Valid hour selection. The system will shutdown during the " + str(shutdownHour) + " hour")
        hourDelta = shutdownHour - currentHour
        print("Hours until shutdown: " + str(hourDelta))
        print("To cancel the scheduled shutdown, close this window.")
        time.sleep((hourDelta*3600))
        if shutdownHour >= currentHour:
            os.system("shutdown /s /t 15")
    
    


def main():
    print("This program will ask for a time to shutdown your computer")
    answer = input("1. Continue\n2. Exit\n")
    if answer == "1":
        shutdown()
    elif answer == "2":
        print("Exiting...")
        exit()
    else:
        print("Input not valid, please enter either 1 or 2")
    
main()