from machine import Pin
import time

#Pin declarrieren

#Ausgänge

Relais1 = Pin(0, Pin.OUT)
Relais2 = Pin(1, Pin.OUT)
Relais3 = Pin(2, Pin.OUT)
Relais4 = Pin(3, Pin.OUT)
Relais5 = Pin(4, Pin.OUT)
Relais6 = Pin(5, Pin.OUT)
Relais7 = Pin(6, Pin.OUT)
Relais8 = Pin(7, Pin.OUT)
Relais9 = Pin(8, Pin.OUT)
Relais10 = Pin(9, Pin.OUT)
LedP = Pin(25, Pin.OUT)

#Eingänge

Button1 = Pin(10, Pin.IN, Pin.PULL_UP)
Button2 = Pin(11, Pin.IN, Pin.PULL_UP)
Button3 = Pin(12, Pin.IN, Pin.PULL_UP)
Button4 = Pin(13, Pin.IN, Pin.PULL_UP)
Button5 = Pin(14, Pin.IN, Pin.PULL_UP)
Button6 = Pin(15, Pin.IN, Pin.PULL_UP)
Button7 = Pin(16, Pin.IN, Pin.PULL_UP)
Button8 = Pin(17, Pin.IN, Pin.PULL_UP)
Button9 = Pin(18, Pin.IN, Pin.PULL_UP)
Button10 = Pin(19, Pin.IN, Pin.PULL_UP)
Button11 = Pin(20, Pin.IN, Pin.PULL_UP)
Button12 = Pin(21, Pin.IN, Pin.PULL_UP)

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0



def alle_an():
    Relais1.value(1)
    Relais2.value(1)
    Relais3.value(1)
    Relais4.value(1)
    Relais5.value(1)
    Relais6.value(1)
    Relais7.value(1)
    Relais8.value(1)
    Relais9.value(1)
    Relais10.value(1)
    
def alle_aus():
    Relais1.value(0)
    Relais2.value(0)
    Relais3.value(0)
    Relais4.value(0)
    Relais5.value(0)
    Relais6.value(0)
    Relais7.value(0)
    Relais8.value(0)
    Relais9.value(0)
    Relais10.value(0)
    
LedP.value(1)   
    
#Programm
while True:
    
        
    
    if Button1.value() == 0:
        counter1 = counter1 + 1
        print("1")
        time.sleep(0.2)
    
    elif Button2.value() == 0:
        counter2 = counter2 + 1
        print("2")
        time.sleep(0.2)
    
    elif Button3.value() == 0:
        counter3 = counter3 + 1
        print("3")
        time.sleep(0.2)
        
    elif Button4.value() == 0:
        counter4 = counter4 + 1
        print("4")
        time.sleep(0.2)
        
    elif Button5.value() == 0:
        counter5 = counter5 + 1
        print("5")
        time.sleep(0.2)
        
    elif Button6.value() == 0:
        counter6 = counter6 + 1
        print("6")
        time.sleep(0.2)
        
    elif Button7.value() == 0:
        counter7 = counter7 + 1
        print("7")
        time.sleep(0.2)
        
    elif Button8.value() == 0:
        counter8 = counter8 + 1
        print("8")
        time.sleep(0.2)
        
    elif Button9.value() == 0:
        counter9 = counter9 + 1
        print("9")
        time.sleep(0.2)
        
    elif Button10.value() == 0:
        counter10 = counter10 + 1
        print("10")
        time.sleep(0.2)
        
    elif Button11.value() == 0:
        print("11")
        alle_an()
    
    elif Button12.value() == 0:
        print("12")
        alle_aus()
        counter1 = 0
        counter2 = 0
        counter3 = 0
        counter4 = 0
        counter5 = 0
        counter6 = 0
        counter7 = 0
        counter8 = 0
        counter9 = 0
        counter10 = 0
        time.sleep(0.2)
        
        
        
        
    if counter1 == 1:
        Relais1.value(1)
        
    
    elif counter1 != 1:
        Relais1.value(0)
        counter1 = 0
        
        
    if counter2 == 1:
        Relais2.value(1)
        
        
    elif counter2 != 1:
        Relais2.value(0)
        counter2 = 0
        
        
    if counter3 == 1:
        Relais3.value(1)
        
    
    elif counter3 != 1:
        Relais3.value(0)
        counter3 = 0
        
        
    if counter4 == 1:
        Relais4.value(1)
        
        
    elif counter4 != 1:
        Relais4.value(0)
        counter4 = 0
        
        
    if counter5 == 1:
        Relais5.value(1)
       
        
    elif counter5 != 1:
        Relais5.value(0)
        counter5 = 0
        
        
    if counter6 == 1:
        Relais6.value(1)
        
        
    elif counter6 != 1:
        Relais6.value(0)
        counter6 = 0
        
    if counter7 == 1:
        Relais7.value(1)
        
    elif counter7 != 1:
        Relais7.value(0)
        counter7 = 0
        
    if counter8 == 1:
        Relais8.value(1)
        
    elif counter8!= 1:
        Relais8.value(0)
        counter8 = 0
        
    if counter9 == 1:
        Relais9.value(1)
        
    elif counter9 != 1:
        Relais9.value(0)
        counter9 = 0
        
    if counter10 == 1:
        Relais10.value(1)
        
    elif counter10 != 1:
        Relais10.value(0)
        counter10 = 0
       
        
    
        
        
    
   
        
    