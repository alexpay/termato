#Python CLI Timer by Alex Pay


import time
import math
import sys
import os
import curses
from multiprocessing import Process


stdscr = curses.initscr()

paused = False

class colors:
    green = '\033[92m'
    red = '\033[93m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def quit(msg):
    sys.stdout.write("\033[K")
    print(msg,"\r")
    os.system('setterm -cursor on')
    exit()


def sprint(t):
    try:
        start = time.monotonic()
        duration = (t * 60)
        for x in range(0, duration + 1):
            while time.monotonic() - start < x:
                pass    
            t = (duration - x)
            ts = ((t/60)%1)*60
            s = int(round(ts))
            sys.stdout.write("\033[K")
            print (colors.red, 'Pomodoro Sprint:','{0:02}:{1:02}'.format(t//60 , s), colors.end, end="\r")
    

    except KeyboardInterrupt:
        quit("Keyboard Interrupt detected... quitting.")   


def rest(rt):
    try:
        start = time.monotonic()
        duration = (rt * 60)
        for x in range(0, duration + 1):
            while time.monotonic() - start < x:
                pass
            rt = (duration - x)
            rts = ((rt/60)%1)*60
            rs = int(round(rts))
            sys.stdout.write("\033[K")
            print (colors.green, 'Take a Break!:','{0:02}:{1:02}'.format(rt//60 , rs), colors.end, end="\r")
    except KeyboardInterrupt:
        quit("Keyboard Interrupt detected... quitting.")   


def run():
    while True:
        sprint(5)
        rest(5)
    

def inputhandler():
    time.sleep(10)
    paused=True
        

curses.noecho()
os.system('setterm -cursor off')

if __name__ == '__main__':
    Process(target=run).start()
    Process(target=inputhandler).start()
