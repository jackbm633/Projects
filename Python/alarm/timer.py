from threading import Timer
import time
import pygame
import argparse
import sys

parser = argparse.ArgumentParser(description="A simple timer written in Python")
parser.add_argument("--seconds", help="Set the time in seconds", nargs="?", type=int)
parser.add_argument("--milliseconds", help="Set the time in milliseconds", nargs="?", type=int)
parser.add_argument("--minutes", help="Set the time in minutes", nargs="?", type=int)
parser.add_argument("--hours", help="Set the time in hours", nargs="?", type=int)

args = parser.parse_args()

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("alarm.ogg")

usertime = 0
if args.seconds >= 0:
	usertime += args.seconds
	
if args.milliseconds >= 0:
	usertime += (args.milliseconds / 1000)
if args.minutes >= 0:
	usertime += (args.minutes * 60)
if args.hours >= 0:
	usertime += (args.hours * 3600)
else:
	print "Exiting: No time input"
	exit(0)

truehours = usertime / 3600
trueminutes = (usertime - truehours * 3600) / 60
trueseconds = (usertime - (truehours * 3600) - (trueminutes * 60)) / 1

print "usertimer set for {0} hours, {1} minutes, and {2} seconds".format(truehours, trueminutes, trueseconds)



def alarmsound():
	### Alarm window code
	
	# Initialises the alarm window
	window = pygame.display.set_mode((250, 50))
	pygame.display.set_caption("Alarm Window")
	
	# Fills the alarm window background
	background = pygame.Surface(window.get_size())
	background = background.convert()
	background.fill((250, 250, 250))
	
	# Displays text in alarm window
	font = pygame.font.Font(None, 24)
	text = font.render("Press SPACE to snooze alarm.", 1, (10,10,10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)
	
	# Blits everything to the screen
	window.blit(background, (0, 0))
	pygame.display.flip()
	
	sound.play()
	print "Press SPACE bar to snooze the alarm"
	sound_on = True
	while sound_on:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					sound_on = False
				else:
					sound.play()
			
t = Timer(usertime, alarmsound)
usertimecopy = usertime

t.start()

for i in range(usertimecopy):
	time.sleep(1)
	truehours = usertimecopy / 3600
	trueminutes = (usertimecopy - truehours * 3600) / 60
	trueseconds = (usertimecopy - (truehours * 3600) - (trueminutes * 60)) / 1

	timestring = "Time Remaining: {0} hours, {1} minutes, {2} seconds.".format(truehours, trueminutes, trueseconds)
	sys.stdout.write(str(timestring)+'{0}\r'.format(" " * len(timestring)))
	sys.stdout.flush()
	usertimecopy -= 1
	
	
