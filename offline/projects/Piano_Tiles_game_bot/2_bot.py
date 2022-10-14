import pyautogui,time
from keyboard import is_pressed,wait
import win32api,win32con

# Test the bot in this link:
# https://www.crazygames.com/game/dont-tap-the-white-tile-piano-tiles

def click(x,y):
    pyautogui.click(x,y)
    # or
    # win32api.SetCursorPos((x,y))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # time.sleep(0.01)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


wait('esc')
print('start')

while True:
    if pyautogui.pixel(307,350)[0] == 0:
        click(307,350)
    if pyautogui.pixel(442,350)[0] == 0:
        click(442,350)
    if pyautogui.pixel(572,350)[0] == 0:
        click(572,350)
    if pyautogui.pixel(700,350)[0] == 0:
        click(700,350)
    
    if is_pressed('q'):
        print('waiting')
        wait('s')
        print('continue')
    if is_pressed('esc'):
        break