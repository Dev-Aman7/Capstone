import pyautogui
import math
import serial
from os import *
from threading import Thread
from time import *
ser=serial.Serial("com28",9600)
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
        
pyautogui.alert('WELCOME User')
pyautogui.hotkey("alt","c")
pyautogui.hotkey("alt","f4")
i=0
while True:

    #t= ser.readline().decode('ascii')
    t=ser.readline().strip().decode('UTF-8')
    s=t.split()
    print(s)
    #print(s[3])
    try:
        x=int(math.floor(float(s[1])))
        y=int(math.floor(float(s[3])))
        print(x,y)
        if(x>-15 and x<15 and y<15 and y>-15):
            continue
        if(s[0]=='p' and s[2]=='p'):
            print("h1")
            pyautogui.moveRel(x,y)
        elif(s[0]=='p' and s[2]=='n'):
            print("h2")
            pyautogui.moveRel(x,-y)
        elif(s[0]=='n' and s[2]=='p'):
            print("h3")
            pyautogui.moveRel(-x,y)
        elif(s[0]=='n' and s[2]=='n'):
            print("h4")
            pyautogui.moveRel(-x,-y)
    except:
        print(0)

        
ser.close() 
