# import pygame
# pygame.init()

# display_width = 1440
# display_height = 900

# black = (0,0,0)
# white = (255,255,255)

# x =  (display_width * 0.45)
# y = (display_height * 0.8)

# screen = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('Entrance Greeter')
# image  = pygame.image.load('PleaseWait.png')
# screen.fill((255,255,255))
# screen.blit(image, (0,0)) 
# pygame.display.update()

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_1:
# 				print event.key


###############

# import math
# import pygame
# import array

# pygame.mixer.init()

# rawArr=[]
# for i in range(41000):
#     freq1=int(math.sin(i/220.0*math.pi*2)*32767.0)
#     if i>40900: freq1=int(freq1*(41000-i)/100.0) #Solution - see Final Solution
#     rawArr.append(freq1)

# sndArr=array.array('h',rawArr)

# snd=pygame.mixer.Sound(sndArr)

# snd.play()

###########

import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("thunder2.wav")
sound.play()
print(pygame.mixer.get_busy())
while pygame.mixer.get_busy():
    print(pygame.mixer.get_busy())
    pygame.time.delay(1000)
print(pygame.mixer.get_busy())

#############

# pygame.init()

# display_width = 800
# display_height = 600

# black = (0,0,0)
# white = (255,255,255)

# clock = pygame.time.Clock()
# crashed = False
# carImg = pygame.image.load('state_0.png')

# x =  (display_width * 0)
# y = (display_height * 0)

# while True:
#     gameDisplay = pygame.display.set_mode((display_width,display_height))
#     pygame.display.set_caption('Entrance Greeter')
#     gameDisplay.fill(white)
#     gameDisplay.blit(carImg, (x,y))
#     pygame.display.update()

##############

# import pygame


# pygame.init()


# display_width = 800
# display_height = 600

# gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('A bit Racey')

# black = (0,0,0)
# white = (255,255,255)

# clock = pygame.time.Clock()
# crashed = False
# carImg = pygame.image.load('state_0.png')

# def car(x,y):
#     gameDisplay.blit(carImg, (x,y))

# x =  (display_width * 0.45)
# y = (display_height * 0.8)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True

#     gameDisplay.fill(white)
#     car(x,y)

        
#     pygame.display.update()
#     clock.tick(60)

# pygame.quit()
# quit()