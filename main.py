import pygame
pygame.init()

# Setup the window
window = pygame.display.set_mode((1200,400))


#Load the track
track = pygame.image.load("assets/track1.png")

#Load the car
car = pygame.image.load("assets/car.png")
car = pygame.transform.scale(car,(40,80))

#Car positions
car_x = 146
car_y = 260

#Condition
drive = True;
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False;
    window.blit(track, (0,0))
    window.blit(car,(car_x,car_y))
    pygame.display.update()
