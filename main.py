from statistics import quantiles
import pyautogui
import keyboard
import threading
import time
import PySimpleGUI as sg
sg.ChangeLookAndFeel('Dark')

def run(stop, click_time):
    while True:
        if stop():
            break
        time.sleep(.15)
        pyautogui.drag(1, 0, click_time, button='left')
        pyautogui.drag(-1, 0, click_time, button='left')

def GUI():
    layout = [
        [sg.Text('enter key that you want to start the program')],
        [sg.InputText(key='-START-')],
        [sg.Text('enter key that you want to stop the program')],
        [sg.InputText(key='-STOP-')],
        [sg.Text('enter how long you want the mouse to be pressed for in seconds')],
        [sg.InputText(key='-TIME-')],
        [sg.Submit()],
        [sg.Cancel()],
    ]
    window = sg.Window('Mouse Drag', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        if event == 'Submit':
            keyboard.wait(values['-START-'])
            stop_threads = False
            t1 = threading.Thread(target = run, args =(lambda : stop_threads,  int(values['-TIME-'])))
            t1.start()
            keyboard.wait(values['-STOP-'])
            break
    stop_threads = True
    t1.join()
    print('thread killed')
    window.close()

def main():
    GUI()

if __name__ == '__main__':
    main()