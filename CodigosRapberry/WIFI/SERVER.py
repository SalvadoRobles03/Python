from flask import Flask, Response,request
from pyautogui import *
import requests

app = Flask(__name__)

def printf(Y1,Y2,X1,X2,X3,X4):
    print("Y1: ",Y1,"Y2: ",Y2,"X1: ",X1,"X2: ",X2,"X3: ",X3,"X4: ",X4)

def Hold (hold_time,X):
    import time, pyautogui
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.press(X)

y1=0
y2=0
x1=0
x2=0
x3=0
x4=0

XR,YR=size()

@app.route('/')
def root():
    moveTo(1040, 564, duration=0.1, tween=easeInOutQuad)
    return "<h1>WELCOME</h1>"

@app.route('/ARRIBA')
def A():
    keyDown('up')
    keyUp('up')
    return "<h1>ARRIBA</h1>" 
 
@app.route('/ABAJO')
def AB():
    keyDown('down')
    keyUp('down')
    return "<h1>ABAJO</h1>" 

@app.route('/IZQUIERDA')
def I():
    keyDown('left')
    keyUp('left')
    return "<h1>IZQUIERDA</h1>" 

@app.route('/DERECHA')
def D():
    keyDown('right')
    keyUp('right')
    return "<h1>DERECHA</h1>" 

@app.route('/CLICK')
def C():
    click()
    return "<h1>CLICK</h1>"

@app.route('/CLICKD')
def CD():
    click(button='right')
    sleep(1)
    return "<h1>CLICK DERECHO</h1>"

@app.route('/EXECUTE',methods=['POST', 'GET'])
def EXECUTE():
    global y1
    global y2
    global x1
    global x2
    global x3
    global x4
    Y1=request.data[0]
    Y2=request.data[1]
    X1=request.data[2]
    X2=request.data[3]
    X3=request.data[4]
    X4=request.data[5]
    
    if(X1<=10 and Y2 <=10):
        scroll(1000)
    elif(X1<=20 and X1 >=10 and Y1 <=10):
        scroll(-1000)
    
    if(x2<=10 and y2>=20):
        if(X1<=20 and X1 >=10 and Y1 <=10):
            moveTo(XR-10,0)
            sleep(0.1)
            click()
    
    if(x2>=15 and y1>=20):
        if(X2<=10 and Y2>=20):
            moveTo(XR-105,0)
            sleep(0.1)
            click()
    
    if(X3<=5 and X4 <=5):
        moveTo(120,YR-5)
        click()
        
    if(X3<20 and X3>=18 and X4 <20 and X4>=18 and Y2>=9 and Y2<=12):
        keyDown('enter')
        keyUp('enter')
            
    y1=Y1
    y2=Y2
    x1=X1
    x2=X2
    x3=X3
    x4=X4
        
    
    return Response ('MOVIENDO')



if __name__ == '__main__':
   app.run( host='192.168.0.106', port=5001 )

#if(Y1<=30 and Y2 >=15):
     #   X=(Y1*XR)/30
    #elif (Y2<=30 and Y1>=15):
     #   X=(Y2*XR)/30
    
        
    #if(X1<=20 and X3 <=20 and Y2 <=10):
     #   Y=(X1*YR)/20
      #  Y=YR-Y
    #elif (X2<=20 and X1 <=20 and X3 <=20 and X4 >=20):
     #   Y=(X3*YR)/20
      #  Y=YR-Y
    #elif (X4<=20 and X1 >=20 and X2 <=20 and X3 <=20):
     #   Y=(X2*YR)/20
      #  Y=YR-Y
    #elif (X4<=20 and X1 >=20 and X2 >=20 and X3 >=20):
     #   Y=(X4*YR)/20
      #  Y=YR-Y


