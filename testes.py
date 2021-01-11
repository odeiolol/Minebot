import pyautogui
import time
import pydirectinput
time.sleep(1)

for i in range(1907):
    finder=pyautogui.locateOnScreen('Screenshot_1.png', 
    confidence=0.3)

    
    if finder != None:
        w=finder[2]/2
        h=finder[3]/2

        x=finder[0]
        y=finder[1]

        altura=x+w
        largura=h+y
        a=int(altura)
        l=int(largura)

        pydirectinput.moveTo(a,l)

    finder=pyautogui.locateOnScreen('Screenshot_2.png', 
    confidence=0.3)


    if finder != None:
        w=finder[2]/2
        h=finder[3]/2

        x=finder[0]
        y=finder[1]

        altura=x+w
        largura=h+y
        a=int(altura)
        l=int(largura)

        pydirectinput.moveTo(a,l)


