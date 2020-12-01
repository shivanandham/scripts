import pyautogui, time
time.sleep(5)
f = open("test.txt",'r')
w = open("bench.txt",'a')
for i in f:
    if len(i)>3:
        w.write(i)
pyautogui.press("enter")
print(f.read())
    