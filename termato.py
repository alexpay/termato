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
    t *= 60
    while (t >= 0):
        try:
            ts = ((t/60)%1)*60
            s = int(round(ts))
            sys.stdout.write("\033[K")
            print ('Pomodoro Sprint:','{0:02}:{1:02}'.format(t//60 , s), end="\r")
            time.sleep(1)
            t-=1
        except KeyboardInterrupt:
            break
    print("\n\nTermodoro Finished!\n")

if __name__ == '__main__':
    timer()
        
