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
drive = True
clock = pygame.time.Clock()
while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False;
            
    #Creating virtual camera for detecting objects
    cam_x = car_x+20
    cam_y = car_y+5
    
    #Reduce the car y positions
    # car_y -= 1
    
    window.blit(track, (0,0))
    window.blit(car,(car_x,car_y))
    
    #Drawing the virtual camera
    pygame.draw.circle(window, (0,255,0), (cam_x, cam_y),5,5)
    
    
    pygame.display.update()
