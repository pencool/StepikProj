import keyboard
import mouse
import time

isClicking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Off')
    else:
        isClicking = True
        print('On')


keyboard.add_hotkey('z', set_clicker)


while True:
    if mouse.is_pressed('right'):
        mouse.double_click(button='left')
        time.sleep(0.01)
