import pyautogui
import math
import serial
from os import *
from threading import Thread
from time import *
ser=serial.Serial("com10",9600)
#type ka dekho
#buttons add krna h
#blue se joystick
'''
while True:
    t=ser3.readline().strip().decode('utf-8')
    t=t.replace("*",'')
    t=t.replace("#",'')
    print(t)
    if t=="decode team":
        break
    alert('Access Denied try again')
'''
        

pyautogui.hotkey("alt","c")
pyautogui.hotkey("alt","f4")
i=0
while True:

    #t= ser.readline().decode('ascii')
    t=ser.readline().strip().decode('UTF-8')
    #s=t.split()
    print(t)
    #print(s[3])
    try:
        #x=int(math.floor(float(s[1])))
        #y=int(math.floor(float(s[3])))
        #print(x,y)
        if(t=="down"):
            pyautogui.moveRel(0,15)
        elif(t=="up"):
            print("h2")
            pyautogui.moveRel(0,-15)
        elif(t=="left"):
            pyautogui.moveRel(-15,0)
        elif(t=="right"):
            print("h4")
            pyautogui.moveRel(15,0)
    except:
        print(0)

        
ser.close() 
