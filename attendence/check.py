import pyautogui 
import time 
from win10toast import ToastNotifier
#import keyboard 
#import random
#import win32api, win32con

#, region=(150,175,350,600), grayscale=True, confidence=0.8
i=0
while 1:
    if pyautogui.locateOnScreen('glogo.png', confidence=0.6) != None:
        print("I can see it")
        print(i)
        i+=1
        time.sleep(1)
        toaster = ToastNotifier()
        toaster.show_toast("Sample Notification","Python is awesome!!!")
        break
    else:
        print("I am unable to see it")
        print(i)
        i+=1
        time.sleep(1)