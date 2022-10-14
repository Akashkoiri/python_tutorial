import pyautogui,time
from keyboard import is_pressed,wait
import win32api,win32con

# Test the bot in this link:
# https://www.crazygames.com/game/dont-tap-the-white-tile-piano-tiles

# click function
# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# check the color
def color(x,y):
    colour = pyautogui.pixel(x,y)

    # if colour != (255,255,252) and colour != (0,0,0):
    #     click(x,y)

    if colour == (0,0,0):
        pyautogui.click(x,y)

# coordinates
# 600,326
# 700,326
# 800,326
# 900,326

# coordinates
# 400,430
# 470,430
# 550,430
# 620,430

wait('esc')
print('start')

while True:
    color(307,350)
    # time.sleep(0.1)
    color(442,350)
    # time.sleep(0.1)
    color(572,350)
    # time.sleep(0.1)
    color(700,350)
    # time.sleep(0.1)

    if is_pressed('esc'):
        break



