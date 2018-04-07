import sys, termios, tty, os, time
import RPi.GPIO as GPIO
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


def foward() :
    GPIO.output(a,True)
    GPIO.output(b,True)
    GPIO.output(c,False)
    GPIO.output(d,False)
def back() :
    GPIO.output(a,False)
    GPIO.output(b,False)
    GPIO.output(c,True)
    GPIO.output(d,True)
def right() :
    GPIO.output(a,True)
    GPIO.output(b,False)
    GPIO.output(c,False)
    GPIO.output(d,True)
def left() :
    GPIO.output(a,False)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,False)
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
 
    if (char == "p"):
        print("Stop!")
        exit(0)
 
    if (char == "d"):
        print("Left pressed")
        left()
        time.sleep(button_delay)
 
    elif (char == "q"):
        print("Right pressed")
        right()
        time.sleep(button_delay)
 
    elif (char == "z"):
        print("Foward pressed")
        foward()
        time.sleep(button_delay)
 
    elif (char == "s"):
        print("Down pressed")
        back()
        time.sleep(button_delay)
 
    elif (char == " "):
        print("pause")
        stop()
        time.sleep(button_delay)
