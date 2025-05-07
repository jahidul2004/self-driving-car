import pygame
pygame.init()

# Setup the window
window = pygame.display.set_mode((1200,400))


#Load the track
track = pygame.image.load("assets/track1.png")

#Condition
while True:
    window.blit(track, (0,0))
    pygame.display.update()
