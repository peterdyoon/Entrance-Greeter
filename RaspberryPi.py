import pygame, datetime, sys
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

while True:
    sleep(.25)
    print("1: {} 2: {} 3: {} 4: {}".format(GPIO.input(22), GPIO.input(23), GPIO.input(24), GPIO.input(25)))
    


phidget_id = int(sys.argv[1])
orientation = sys.argv[2]
custom_setting = sys.argv[3]

pygame.init()
pygame.mixer.init()

display_width = 1920
display_height = 1080
# display_width = 1440
# display_height = 900

screen = pygame.display.set_mode((display_width,display_height), pygame.NOFRAME)
pygame.display.set_caption('Entrance Greeter')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

x =  (display_width * 1)
y = (display_height * 1)

def show_image(stage):
	image = pygame.image.load('Images/{}/{}.png'.format(orientation, stage))
	image = pygame.transform.scale(image, (display_width, int(display_height)))
	rect = image.get_rect()
	rect = rect.move((x, y))
	screen.blit(image, (0,0))
	pygame.display.update()

def play_sound(stage):
	pygame.mixer.stop()
	sound = pygame.mixer.Sound("Sounds/{}.wav".format(stage))
	sound.play()

if custom_setting == "Neutral":
	while True:
		for event in pygame.event.get():
			show_image("neutral")

# Comment out for now during Pygame Testing
channels = [DigitalInput() for x in range(0, 4)]

for index, channel in enumerate(channels):
	channels[index].setDeviceSerialNumber(phidget_id)
	channels[index].setChannel(index)

	# Might not use this; a little too much activity
	# ch.setOnAttachHandler(onAttachHandler)
	# ch.setOnDetachHandler(onDetachHandler)
	# ch.setOnErrorHandler(onErrorHandler)
	# ch.setOnStateChangeHandler(onStateChangeHandler)

	channels[index].openWaitForAttachment(5000)
# Comment out for now during Pygame Testing

# Start with Pull Forward
show_image("pull_forward")

# Flag for when to play Thank You message
sleep_tracker_start_time = datetime.datetime.now()
first_time_neutral = True
first_time_package = False
first_time_thankyou = False
first_time_wait = False


### Prod Phidget
while True:
	for event in pygame.event.get():
		# print event
		continue
	# for index, channel in enumerate(channels):
	# print index, channel, channel.getState()
	# if channel.getState() == 1:
	screen.fill(white)
	if first_time_neutral and GPIO.input(22) == 0:
		print "Neutral Index: {}".format(index)
		show_image("neutral")
		play_sound("neutral")
		sleep_tracker_start_time = datetime.datetime.now()
		first_time_neutral = False
		first_time_package = True
	elif first_time_package and GPIO.input(23) == 0:
		print "Love Index: {}".format(index)
		show_image("wash_love")
		play_sound("wash_love")
		sleep_tracker_start_time = datetime.datetime.now()
		first_time_package = False
		first_time_thankyou = True
	elif first_time_package and GPIO.input(24) == 0:
		print "Like Index: {}".format(index)
		show_image("wash_like")
		play_sound("wash_like")
		sleep_tracker_start_time = datetime.datetime.now()
		first_time_package = False
		first_time_thankyou = True
	elif first_time_package and GPIO.input(25) == 0:
		print "Wash Index: {}".format(index)
		show_image("wash_basic")
		play_sound("wash_basic")
		sleep_tracker_start_time = datetime.datetime.now()
		first_time_package = False
		first_time_thankyou = True
	# elif first_time_thankyou == True and index == 4:
	elif first_time_thankyou == True:
		# print "Thank You Index: {}".format(index)
		# show_image("thank_you")
		# play_sound("thank_you")
		# sleep_tracker_start_time = datetime.datetime.now()
		# first_time_thankyou = False

		temp_time = datetime.datetime.now()
		if (temp_time - sleep_tracker_start_time).seconds > 5:
			print "Thank You Index: {}".format(index)
			show_image("thank_you")
			play_sound("thank_you")
			sleep_tracker_start_time = datetime.datetime.now()
			first_time_thankyou = False
	# elif first_time_thankyou:
	# 	wash_delay = 4.0
	# 	accuracy_index = 100
	# 	for interval in range(0, int(wash_delay) * accuracy_index):
	# 		print "Interval: {}".format(interval)
	# 		if interval > wash_delay * accuracy_index - 1:
	# 			print "Thank You Index: {}".format(index)
	# 			show_image("thank_you")
	# 			play_sound("thank_you")
	# 			sleep_tracker_start_time = datetime.datetime.now()
	# 			first_time_thankyou = False
	# 		else:
	# 			sleep(wash_delay/(wash_delay*accuracy_index))
	elif GPIO.input(22) == 1:
		temp_time = datetime.datetime.now()
		if (temp_time - sleep_tracker_start_time).seconds > 90:
			show_image("please_wait")
		else:
			show_image("pull_forward")
		first_time_neutral = True
		first_time_package = False
		first_time_thankyou = False
		first_time_wait = False
		# elif first_time_wait and index == 4:
		# 	print "Please Wait Index: {}".format(index)
		# 	show_image("please_wait")
		# 	play_sound("please_wait")
		# 	sleep_tracker_start_time = datetime.datetime.now()
		# 	first_time_wait = False
		# 	first_time_neutral = True

	# temp_time = datetime.datetime.now()
	# print temp_time - sleep_tracker_start_time
	# if (temp_time - sleep_tracker_start_time).seconds > 10:
	# 	sleep_tracker_start_time = datetime.datetime.now()
	# 	show_image("please_wait")
	# 	first_time_neutral = True
	# 	first_time_package = False
	# 	first_time_thankyou = False
	# 	first_time_wait = False
### Prod Phidget


# ### Dev Phidget
# while True:
# 	for index, channel in enumerate(channels):
# 		if channel.getState() == 1 or interrupt:
# 			# screen.fill(white)
# 			if interrupt == 0 or index == 0:
# 				show_image("pull_forward")
# 				play_sound("pull_forward")
# 				interrupt = None
# 				sleep_tracker_start_time = datetime.datetime.now()
# 			elif interrupt == 1 or index == 1:
# 				show_image("neutral")
# 				play_sound("neutral")
# 				interrupt = None
# 				sleep_tracker_start_time = datetime.datetime.now()
# 			elif interrupt == 2 or index == 2:
# 				show_image("wash_basic")
# 				play_sound("wash_basic")
# 				need_thank_you = True
# 				interrupt = None
# 				sleep_tracker_start_time = datetime.datetime.now()
# 			elif interrupt == 3 or index == 3:
# 				show_image("wash_like")
# 				play_sound("wash_like")
# 				need_thank_you = True
# 				interrupt = None
# 				sleep_tracker_start_time = datetime.datetime.now()
# 			elif interrupt == 4 or index == 4:
# 				show_image("wash_love")
# 				play_sound("wash_love")
# 				need_thank_you = True
# 				interrupt = None
# 				sleep_tracker_start_time = datetime.datetime.now()

# 	if need_thank_you == True:
# 		wash_delay = 4.0
# 		accuracy_index = 100
# 		for interval in range(0, int(wash_delay) * accuracy_index):
# 			for index, channel in enumerate(channels):
# 				if channel.getState() == 1:
# 					interrupt = index
# 					need_thank_you = False
# 			if interrupt:
# 				continue
# 			elif interval == wash_delay * accuracy_index - 1:
# 				need_thank_you = False
# 				show_image("thank_you")
# 				play_sound("thank_you")
# 			else:
# 				sleep(wash_delay/(wash_delay*accuracy_index))

# 	temp_time = datetime.datetime.now()
# 	if (temp_time - sleep_tracker_start_time).seconds > 50:
# 		sleep_tracker_start_time = datetime.datetime.now()
# 		show_image("please_wait")
# 		# play_sound("welcome_to_everwash")
# 		interrupt = None
# ### Dev Phidget

### Pygame Testing
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.KEYDOWN or interrupt:
# 			screen.fill(white)
# 			if interrupt == pygame.K_1 or event.key == pygame.K_1:
# 				show_image("pull_forward")
# 				play_sound("pull_forward")
# 				interrupt = 0
# 				sleep_tracker_start_time = datetime.datetime.now()
# 			elif interrupt == pygame.K_2 or event.key == pygame.K_2:
# 				show_image("neutral")
# 				play_sound("neutral")
# 				interrupt = 0
# 				sleep_tracker_start_time = datetime.datetime.now()
# 			elif interrupt == pygame.K_3 or event.key == pygame.K_3:
# 				show_image("wash_basic")
# 				play_sound("wash_basic")
# 				need_thank_you = True
# 				interrupt = 0
# 				sleep_tracker_start_time = datetime.datetime.now()
# 			elif interrupt == pygame.K_4 or event.key == pygame.K_4:
# 				show_image("wash_like")
# 				play_sound("wash_like")
# 				need_thank_you = True
# 				interrupt = 0
# 				sleep_tracker_start_time = datetime.datetime.now()
# 			elif interrupt == pygame.K_5 or event.key == pygame.K_5:
# 				show_image("wash_love")
# 				play_sound("wash_love")
# 				need_thank_you = True
# 				interrupt = 0
# 				sleep_tracker_start_time = datetime.datetime.now()

# 	if need_thank_you == True:
# 		wash_delay = 4.0
# 		accuracy_index = 100
# 		for interval in range(0, int(wash_delay) * accuracy_index):
# 			for event in pygame.event.get():
# 				if event.type == pygame.KEYDOWN:
# 					interrupt = event.key
# 					need_thank_you = False
# 			if interrupt:
# 				continue
# 			elif interval == wash_delay * accuracy_index - 1:
# 				need_thank_you = False
# 				show_image("thank_you")
# 				play_sound("thank_you")
# 			else:
# 				sleep(wash_delay/(wash_delay*accuracy_index))

# 	temp_time = datetime.datetime.now()
# 	if (temp_time - sleep_tracker_start_time).seconds > 10:
# 		sleep_tracker_start_time = datetime.datetime.now()
# 		show_image("please_wait")
# 		# play_sound("welcome_to_everwash")
# 		interrupt = 0
### Pygame Testing

