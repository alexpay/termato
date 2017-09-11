#Python CLI Timer - using the click module

#imports
import click
import time
import math
import sys
from getch import getch

#click
@click.command()
@click.option('-t', default=25, help='Time in minutes.')

def timer(t):
	enabled = False
	start = time.monotonic()
	duration = (t * 60)
	key = getch()
	for x in range(0, duration + 1):
		while time.monotonic() - start < x:
			if key == 's':
				enabled = True
			if key == 'p':
				enabled = False
			if enabled == True:
				t = (duration - x)
				ts = ((t/60)%1)*60
				s = int(round(ts))
				sys.stdout.write("\033[K")
				print ('Pomodoro Sprint:','{0:02}:{1:02}'.format(t//60 , s), end="\r")
			else:
				continue

	print("\n\nPomodoro Finished!\n")

if __name__ == '__main__':
	timer()
        
