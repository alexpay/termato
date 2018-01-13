#Python CLI Timer by Alex Pay

#imports
import time
import math
import sys
import os
import curses
stdscr = curses.initscr()
class colors:
    green = '\033[92m'
    red = '\033[93m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def sprint(t):
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

def rest(rt):
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

def run():
    while True:
        sprint(25)
        rest(5)
    
os.system('setterm -cursor off')
curses.noecho()

run()
