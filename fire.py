from pyautogui import *
import serial
from os import *
from threading import Thread
from time import *
from firebase import firebase
firebase=firebase.FirebaseApplication('https://smart-home-2330c.firebaseio.com/', None)

finish=False
##
##while True:
##    t=ser3.readline().strip().decode('utf-8')
##    t=t.replace("*",'')
##    t=t.replace("#",'')
##    print(t)
##    if t=="decode team":
##        print("hello")
##        break
##    alert('Access Denied try again')
#startfile("http://www.daniweb.com/")

p=firebase.get('/tell',None)
while True:
    t=firebase.get('/tell',None)
    try:
        if(t==p):
            continue
        else:
            p=t
            t=t.replace("*",'')
            t=t.replace("#",'')
            print(t)
            words=t.split();
            print(words)

        ##    if t.lower()=="find":
        ##        x,y=locateCenterOnScreen('foo.png')
        ##        print(x,y)
            if t.lower()=="left click" or t.lower()=="click":
                click()
            if t.lower()=="double click":
                doubleClick()
            if t.lower()=="right click":
                rightClick()
            if t.lower()=="screenshot":
                screenshot("foo.png")
            if t.lower()=="scroll up":
                scroll(300)
            if t.lower()=="scroll down":
                scroll(-300)
            if t.lower()=="ok":
                typewrite("\n")
            if(len(words)>1):
                if words[0]=="open":
                    tw1=words[1]
                    if tw1=="presentation" :
                        print("here")
                        #startfile("F:\\Team 58.pptx")
                        startfile("Review.pptx")
                        sleep(8);
                        typewrite("\n",interval=0.001)
                        finish2=False
                        while not finish2:
                            t=firebase.get('/tell',None)
                            print(t)
                            if(p==t):
                                continue
                            p=t
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
                            if t=="next" or t=="next slide":
                                typewrite("\n",interval=0.001)
                            elif t=="back":
                                typewrite("\b",interval=0.001)
                            elif t=="end presentation" or t=="and presentation":
                                hotkey("alt","f4")
                                typewrite("\n")
                            elif t=="close presentation" or t=="close":
                                hotkey("alt","f4")
                                typewrite("\n")
                                finish2=True
                    elif tw1=="Chrome":
                        startfile("http://www.google.com/")
                        
                    else:
                        startfile(tw1)
            if t=="start typing":
                while not finish:
                    t=firebase.get('/tell',None)
                    if(p==t):
                        continue
                    p=t
                    t=t.replace("*",'')
                    t=t.replace("#",'')
                    t.replace("space"," ")
                    print(t)
                    if(t=="stop typing"):
                        finish=True
                    else:
                        tem1=t
                        if(tem1=="backspace"):
                            press("backspace")
                            continue
                        tem1=tem1.replace("fullstop",".")
                        tem1=tem1.replace("comma",",")
                        tem1=tem1.replace("question mark","?")
                        tem1=tem1.replace("tab","   ")
                        typewrite(tem1,interval=0.001)
                        typewrite("\n")
            if t=="close":
                hotkey("alt","f4")
                typewrite("\n")
                system("TASKKILL /F /IM "+tw1+".exe")
            if t=="go to sleep baby":
                break
    
                
            finish=False
    except:
        print("issue occured at "+t)

hotkey("alt","c")

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
