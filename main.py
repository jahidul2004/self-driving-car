#Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((1200, 400))
pygame.display.set_caption("Goriber Tesla")  # Set the window title

# Load the track image
track = pygame.image.load("assets/track6.png")

# Load the car image and resize it
car = pygame.image.load("assets/car.png")
car = pygame.transform.scale(car, (30, 60))  # Width: 30, Height: 60

# Initial position of the car
car_x = 155
car_y = 300

# Camera offset from the car
cam_x_offset = 0
cam_y_offset = 0

# Distance of the camera from the car (focal point)
focal_dist = 25

# Initial direction of the car
direction = 'up'

# Main game loop control
drive = True
clock = pygame.time.Clock()

# Game loop starts
while drive:
    clock.tick(60)  # Run the loop at 60 FPS
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    # Create a virtual camera point ahead of the car
    cam_x = car_x + cam_x_offset + 15  # 15 is half the width of the car
    cam_y = car_y + cam_y_offset + 15  # 15 is half the height of the car

    # Get the red value (R from RGB) of the pixels in different directions
    up_px = window.get_at((cam_x, cam_y - focal_dist))[0]
    right_px = window.get_at((cam_x + focal_dist, cam_y))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dist))[0]

    # Direction change logic based on pixel color detection (white = 255)
    
    # Turn right from 'up' to 'right'
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)

    # Turn down from 'right' to 'down'
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x += 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)

    # Turn right again from 'down' to 'right'
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y += 30
        cam_y_offset = 0
        cam_x_offset = 30
        car = pygame.transform.rotate(car, 90)

    # Turn up from 'right' to 'up'
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x += 30
        cam_x_offset = 0
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)

    # Move the car forward based on current direction and track color
    if direction == 'up' and up_px == 255:
        car_y -= 1
    elif direction == 'right' and right_px == 255:
        car_x += 1
    elif direction == 'down' and down_px == 255:
        car_y += 1

    # Draw the track and car on the window
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))

    # Draw the virtual camera point (green dot)
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)

    # Update the display
    pygame.display.update()
