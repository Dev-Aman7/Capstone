from pyautogui import *
import serial
from os import *
from threading import Thread
from time import *
sleep(4)
ser3=serial.Serial("com21",9600)
finish=False
       
alert('WELCOME User')
while True:
    t=ser3.readline().strip().decode('utf-8')
    t=t.replace("*",'')
    t=t.replace("#",'')
    print(t)
    words=t.split();
    print(words)
    if t=="left click" or t=="click":
        click()
    if t=="double click":
        doubleClick()
    if t=="right click":
        rightClick()
    if(len(words)>1):
        if words[0]=="open":
            tw1=words[1]
            if tw1=="presentation" :
                startfile("F:\\perspect-1.pptx")
                sleep(8);
                typewrite("\n",interval=0.001)
                finish2=False
                while not finish2:
                    t=ser3.readline().strip().decode('utf-8')
                    t=t.replace("*",'')
                    t=t.replace("#",'')
                    if t=="left click":
                        click()
                    if t=="double click":
                        doubleClick()
                    if t=="right click":
                        rightClick()
                    if(t=="start presentation"):
                        hotkey("fn","f5")
                    if t=="next":
                        typewrite("\n",interval=0.001)
                    elif t=="back":
                        typewrite("\b",interval=0.001)
                    elif t=="end presentation":
                        hotkey("alt","f4")
                    elif t=="close presentation":
                        hotkey("alt","f4")
                        finish2=True
                
            else:
                startfile(tw1)
    if t=="start typing":
        while not finish:
            t=ser3.readline().strip().decode('utf-8')
            t=t.replace("*",'')
            t=t.replace("#",'')
            print(t)
            if(t=="stop typing"):
                finish=True
            else:
                tem1=t
                tem1=tem1.replace("fullstop",".")
                tem1=tem1.replace("comma",",")
                tem1=tem1.replace("question mark","?")
                tem1=tem1.replace("tab","   ")
                typewrite(tem1+"\n",interval=0.001) 
    if t=="close":
        system("TASKKILL /F /IM "+tw1+".exe")
    if t=="go to sleep baby":
        break        
        
    finish=False

hotkey("alt","c")
hotkey("alt","f4")
ser.close()
'''
# useful for entering text, newline is Enter
r=sr.Recognizer()
r.energy_threshold=4000
r.threshold=0.2
r.dynamic_energy_threshold=True

print(size())
#ser=serial.Serial("com300",9600)
#ser2=serial.Serial("com4",9600)

tem_ac=0
tem_mag=0
go=1
flag=True
mouseDown()
mouseUp()
mouseDown()
mouseUp()
while True:
    t4=ser2.readline().strip().decode('utf-8')
    print(t4)
    if(t4=="*right click#"):
        click(button='right')
    if(t4=="*left click#"):
        click(button='left')
    if(t4=="*drag#"):
        mouseDown()
    if(t4=="*release#"):
        mouseUp()
    if(t4=="*scroll up#"):
        scroll(10)
    if(t4=="*scroll down#"):
        scroll(-10)                  
                     
'''
