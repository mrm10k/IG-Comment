import pyautogui as pg
import time

time.sleep(3)

for i in range(746):
    pg.write(f'lista.push(obj[{i}].innerText);')
    pg.press('enter')
    time.sleep(0.5)