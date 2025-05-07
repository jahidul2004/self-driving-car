import pygame
pygame.init()

# Setup the window
window = pygame.display.set_mode((1200,400))


#Load the track
track = pygame.image.load("assets/track1.png")

#Condition
drive = True;
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False;
    window.blit(track, (0,0))
    pygame.display.update()
