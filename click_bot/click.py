import pyautogui
import time
from pynput.mouse import Button, Controller

time.sleep(5)
mouse = Controller()

for i in range(100):#you can set how much times you have to click in range(no. of times to click) 
  time.sleep(0.1)     
  print(i)
  mouse.click(Button.left)
