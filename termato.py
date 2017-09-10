#Python CLI Timer - using the click module

#imports
import click
import time
import math
import sys

#click
@click.command()
@click.option('-t', default=25, help='Time in minutes.')


def timer(t):
    start = time.monotonic()
    duration = (t * 60)
    for x in range(0, duration + 1):
        while time.monotonic() - start < x:
                pass

        t = (duration - x)
        ts = ((t/60)%1)*60
        s = int(round(ts))
        sys.stdout.write("\033[K")
        print ('Pomodoro Sprint:','{0:02}:{1:02}'.format(t//60 , s), end="\r")
    
    print("\n\nPomodoro Finished!\n")

if __name__ == '__main__':
    timer()
        
