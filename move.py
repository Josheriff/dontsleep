import pyautogui
import time
from random import randint

n = 1
while True:
    x = randint(150, 200)
    y = randint(150, 250)
    print(f'MOVING to {x}:{y}')
    pyautogui.moveTo(x,y)
    n+=1
    time.sleep(20)