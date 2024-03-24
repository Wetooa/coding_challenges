from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# shit this is lit use this learn this OMG
def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) # use this since its windows lol learned this during pong making
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(600, 400)[0] == 0: 
        click(600, 420)
    if pyautogui.pixel(680, 400)[0] == 0: 
        click(680, 420)
    if pyautogui.pixel(770, 400)[0] == 0: 
        click(770, 420)
    if pyautogui.pixel(850, 400)[0] == 0: 
        click(850, 420)
        