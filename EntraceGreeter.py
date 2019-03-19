import pygame, pyglet
from time import sleep
from Phidget22.Devices.DigitalInput import *
from DigitalInput import onAttachHandler, onDetachHandler, onErrorHandler, onStateChangeHandler

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

display_width = 1920
display_height = 1080
display_width = 1440
display_height = 900

black = (0,0,0)
white = (255,255,255)

x =  (display_width * 1)
y = (display_height * 1)

def please_wait():
	pygame.mixer.pause()
	screen = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('Entrance Greeter')
	image = pygame.image.load('PleaseWait.png')
	image = pygame.transform.scale(image, (display_width, int(display_height*.95)))
	rect = image.get_rect()
	rect = rect.move((x, y))
	screen.fill((255,255,255))
	screen.blit(image, (0,0)) 
	pygame.display.update()
	pygame.time.wait(3000)
	pygame.mixer.unpause()
	sound = pygame.mixer.Sound("Welcome To Everwash.wav")
	sound.play()

def pull_forward():
	pygame.mixer.pause()
	screen = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('Entrance Greeter')
	image = pygame.image.load('PullForward.jpg')
	image = pygame.transform.scale(image, (display_width, int(display_height*.95)))
	rect = image.get_rect()
	rect = rect.move((x, y))
	screen.fill((255,255,255))
	screen.blit(image, (0,0)) 
	pygame.display.update()
	sound = pygame.mixer.Sound("Please Pull Forward.wav")
	sound.play()

def hit_neutral():
	pygame.mixer.pause()
	screen = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('Entrance Greeter')
	image = pygame.image.load('Neutral Right 90.jpg')
	image = pygame.transform.scale(image, (display_width, int(display_height*.95)))
	rect = image.get_rect()
	rect = rect.move((x, y))
	screen.fill((255,255,255))
	screen.blit(image, (0,0)) 
	pygame.display.update()
	sound = pygame.mixer.Sound("Shift Neutral 2.wav")
	sound.play()

def wash_package(pack_type):
	pygame.mixer.pause()
	pack_type_pics = {
		"wash": "Wash Right 90.jpg",
		"like": "Like Right 90.jpg",
		"love": "Love Right 90.jpg"
	}
	pack_type_wav = {
		"wash": "YHS Wash 2.wav",
		"like": "YHS Like-2.wav",
		"love": "YHS Love 2.wav"
	}
	screen = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('Entrance Greeter')
	image = pygame.image.load(pack_type_pics[pack_type])
	image = pygame.transform.scale(image, (display_width, int(display_height*.95)))
	rect = image.get_rect()
	rect = rect.move((x, y))
	screen.fill((255,255,255))
	screen.blit(image, (0,0)) 
	pygame.display.update()
	sound = pygame.mixer.Sound(pack_type_wav[pack_type])
	sound.play()

def thank_you():
	pygame.mixer.pause()
	screen = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('Entrance Greeter')
	image = pygame.image.load('Welcome Thank You Right 90.jpg')
	image = pygame.transform.scale(image, (display_width, int(display_height*.95)))
	rect = image.get_rect()
	rect = rect.move((x, y))
	screen.fill((255,255,255))
	screen.blit(image, (0,0)) 
	pygame.display.update()
	pygame.time.wait(3000)
	sound = pygame.mixer.Sound("Thank You 2.wav")
	sound.play()

# Comment out for now during Pygame Testing
# channels = [DigitalInput() for x in range(0, 8)]

# for index, channel in enumerate(channels):
# 	channels[index].setDeviceSerialNumber(507003)
# 	channels[index].setChannel(index)

# 	# Might not use this; a little too much activity
# 	# ch.setOnAttachHandler(onAttachHandler)
# 	# ch.setOnDetachHandler(onDetachHandler)
# 	# ch.setOnErrorHandler(onErrorHandler)
# 	# ch.setOnStateChangeHandler(onStateChangeHandler)

# 	channels[index].openWaitForAttachment(5000)
# Comment out for now during Pygame Testing

# Start with Please Wait
please_wait()

while True:
	# for index, channel in enumerate(channels):
	# 	if channel.getState() == 1:
	# 		if index == 0:
	# 			please_wait()
	# 		elif index == 2:
	# 			pull_forward()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				pull_forward()
			elif event.key == pygame.K_2:
				hit_neutral()
			elif event.key == pygame.K_3:
				wash_package("wash")
				thank_you()
				please_wait()
			elif event.key == pygame.K_4:
				wash_package("like")
				thank_you()
				please_wait()
			elif event.key == pygame.K_5:
				wash_package("love")
				thank_you()
				please_wait()

