import pyautogui as pg
import time

personas = []

archivo = open('C:\\Users\\marioR\\Desktop\\lista1.txt')
num = 1

nlinea = 1

for linea in archivo:
    word=linea.split()
    if(len(word)) == 0: continue
    if nlinea == num:
        donde = word[0].find('\"')
        new = word[0]
        palabra = new[donde + 1:]
        palabra = palabra[:len(palabra) - 1]
        personas.append(palabra)
        print(palabra)
        num = num + 1

    nlinea = nlinea + 1

time.sleep(5)

for persona in personas:
    pg.hotkey('altright', '2')
    pg.write(persona)
    pg.press('tab')
    pg.press('enter')
    time.sleep(30)

    pg.press('enter')
