from threading import Timer
import pygame
import argparse

parser = argparse.ArgumentParser(description="A simple timer written in Python")
parser.add_argument("--seconds", help="Set the time in seconds", nargs="?", type=int)
parser.add_argument("--milliseconds", help="Set the time in milliseconds", nargs="?", type=int)
parser.add_argument("--minutes", help="Set the time in minutes", nargs="?", type=int)
parser.add_argument("--hours", help="Set the time in hours", nargs="?", type=int)

args = parser.parse_args()


time = 0
if args.seconds >= 0:
	time += args.seconds
	
if args.milliseconds >= 0:
	time += (args.milliseconds / 1000)
if args.minutes >= 0:
	time += (args.minutes * 60)
if args.hours >= 0:
	time += (args.hours * 3600)

truehours = time / 3600
trueminutes = (time - truehours * 3600) / 60
trueseconds = (time - (truehours * 3600) - (trueminutes * 60)) / 1

print "Timer set for {0} hours, {1} minutes, and {2} seconds".format(truehours, trueminutes, trueseconds)

pygame.mixer.init()
pygame.display.set_mode((1, 1))
pygame.mixer.music.load("alarm.ogg")
def alarmsound():
	
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
		while True:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_SPACE:
						pygame.mixer.music.stop()
			
t = Timer(time, alarmsound)
t.start()
print t
