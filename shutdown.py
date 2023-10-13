# Addition to shutdown.py that instead does a shutdown in time from now, rather than hour of day
import os
from datetime import date, time
import time
import PySimpleGUI as gui

def getRadioButton(values):
    # Return the value of the 
    if values['shutdown']:
        return 'shutdown'
    elif values['hibernate']:
        return 'hibernate'
    else:
        return 'sleep'
    
def countdown(minutes, action):
    try:
        seconds = minutes * 60
        for remaining in range(seconds, 0, -1):
            timeString = time.strftime('%H:%M:%S', time.localtime(remaining))
            gui.popup_no_wait(f"Countdown: {timeString}", title="Time to {action}", non_blocking=True)
            time.sleep(1)
        
        if action == 'shutdown':
            os.system('shutdown /s /t 0')
        elif action == 'hibernate':
            os.system('hibernate /h')
        elif action == 'sleep':
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
    except Exception as error:
        gui.popup_error(f"An unexpected error occurred: {str(error)}")

def main():

    layout = [
        [gui.Text('Countdown Timer')],
        [gui.InputText(key='time_input', size=(10, 1)), gui.Text('minutes')],
        [gui.Radio('Shutdown', 'radio_group', key='shutdown', default=True),
            gui.Radio('Hibernate', 'radio_group', key='hibernate'), 
            gui.Radio('Sleep', 'radio_group', key='sleep')],
        [gui.Button('Start Countdown'), gui.Button('Exit')],
    ]

    window = gui.Window('Shutdown/Hibernate/Sleep Timer', layout)

    while True:
        event, values = window.read()
        #Exit if the user closes the window or clicks exit button
        if event == gui.WINDOW_CLOSED or event == 'Exit':
            break

        #Start countdown if the countdown button is clicked
        if event == 'Start Countdown':
            try:
                countdown_minutes = int(values['time_input'])
                action = getRadioButton(values)
            except ValueError:
                gui.popup_error("Please enter a valid number of minutes.")
            except Exception as error:
                gui.popup_error(f"An unexpected error occurred: {str(error)}")


main()

