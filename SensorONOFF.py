import numpy as np
import datetime
import time

def sensor(events):
    for _ in range (events):

        Min=np.random.randint(60)
        
        if(Min<10):
            minuto="0"+str(Min)
        else:
            minuto=str(Min)
        
        
        fecha=str(datetime.datetime.now().strftime("%A,%d,%B %Y %I:")+minuto+str(datetime.datetime.now().strftime(":%S %p")))
        
        yield(np.random.randint(2),fecha) #yield es para regresar un valor pero sin que termine la función
        time.sleep(1)
        
mList=list(sensor(5))
print(mList)
    