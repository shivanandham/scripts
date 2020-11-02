import pyautogui, time
time.sleep(5)
f = open("YourTextHere.txt", 'r')
for i in f:
    if len(i)>3:
        pyautogui.typewrite(i)
        time.sleep(0.3)
pyautogui.press("enter")