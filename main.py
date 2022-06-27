from statistics import quantiles
import pyautogui
import keyboard
import threading
import time

mouse_down = pyautogui.mouseDown(button='left') 
mouse_up = pyautogui.mouseUp(button='left')

def run(stop):
    while True:
        if stop():
            break
        time.sleep(.15)
        pyautogui.drag(1, 0, .25, button='left')
        pyautogui.drag(-1, 0, .25, button='left')


def main():
    time.sleep(10)
    stop_threads = False
    t1 = threading.Thread(target = run, args =(lambda : stop_threads, ))
    t1.start()
    keyboard.wait("q")
    stop_threads = True
    t1.join()
    print('thread killed')

if __name__ == '__main__':
    main()