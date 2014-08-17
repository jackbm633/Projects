from threading import Timer
import pygame
import argparse

parser = argparse.ArgumentParser(description="A simple timer written in Python")
parser.add_argument("--seconds", help="Set the time in seconds", nargs="?", type=int)
parser.add_argument("--milliseconds", help="Set the time in milliseconds", nargs="?", type=int)
parser.add_argument("--minutes", help="Set the time in minutes", nargs="?", type=int)
parser.add_argument("--hours", help="Set the time in hours", nargs="?", type=int)

args = parser.parse_args()

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("alarm.ogg")

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
			
t = Timer(time, alarmsound)
t.start()
