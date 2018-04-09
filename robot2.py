import sys, termios, tty, os, time
from EmulatorGUI import GPIO
a=23
b=24
c=22
d=27
x=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)

def mfl() :
    GPIO.output(a,True)
    GPIO.output(c,True)
    
def mfr() :
    GPIO.output(b,True)
    GPIO.output(d,False)
def mbl() :
    GPIO.output(c,True)
    GPIO.output(a,False)
def mbr() :
    GPIO.output(d,True)
    GPIO.output(b,False)
    
        
def stop() :
    GPIO.output(a,False)
    GPIO.output(b,False)
    GPIO.output(c,False)
    GPIO.output(d,False)
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0
 
while True:
    char = getch()
 
    if (char == "s"):
        print("mbl")
        mbl()
 
    if (char == "z"):
        print("mfl")
        mfl()
        time.sleep(button_delay)
    elif (char == "o") :
        print("mfr")
        mfr()
        time.sleep(button_delay)
    elif (char == "l") :
        print("mbr")
        mbr()
        time.sleep(button_delay)
    elif (char == "n") :
        print("stop")
        stop()
        time.sleep(button_delay)
        
