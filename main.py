import pygame
pygame.init()

# Setup the window
window = pygame.display.set_mode((1200,400))


#Load the track
track = pygame.image.load("assets/track3.png")

#Load the car
car = pygame.image.load("assets/car.png")
car = pygame.transform.scale(car,(30,60))

#Car positions
car_x = 155
car_y = 300

#Camera offset
cam_x_offset = 0

#Camera Focal point
focal_dist = 25

#Car direction
direction = 'up'

#Condition
drive = True
clock = pygame.time.Clock()
while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False;
            
    #Creating virtual camera for detecting objects
    cam_x = car_x+cam_x_offset+15
    cam_y = car_y+15
    
    #Detect the track
    up_px = window.get_at((cam_x, cam_y-focal_dist))[0]
    right_px = window.get_at((cam_x+focal_dist,cam_y))[0]
    

    #Change the direction
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    #Car driving code
    if direction == 'up' and up_px == 255:
        car_y -= 1
        
    if direction == 'right' and right_px == 255:
        car_x += 1
    
    window.blit(track, (0,0))
    window.blit(car,(car_x,car_y))
    
    #Drawing the virtual camera
    pygame.draw.circle(window, (0,255,0), (cam_x, cam_y),5,5)
    
    
    pygame.display.update()
