import pygame 
pygame.init() # Initialise pygame
window = pygame.display.set_mode((1200,400)) # width, height
track = pygame.image.load('/Users/apuroop/python/Projects/tesla/track6.png')
car = pygame.image.load('/Users/apuroop/python/Projects/tesla/tesla.png')
car = pygame.transform.scale(car,(30,60)) #Change the car size
car_x, car_y = 155,300
clock = pygame.time.Clock()
cam_x_offset = 0
cam_y_offset = 0 
direction ='upward'
focal_dist = 25 
drive = True
# Cam focal length = 15 px inside the car + 10 px ahead = 25px
while drive:
     for event in pygame.event.get(): # Get every event happening in pygame
          if event.type == pygame.QUIT: # Stop running when uses presses 'x' button
               drive = False # To stop while loop 
     clock.tick(60) # 60fps for smoother transition
     cam_x = car_x + cam_x_offset + 15 # Initialise cam poition to top of car coordinates
     cam_y = car_y + cam_y_offset +15 # Initialise cam poition to top of car coordinates
     upper_px = window.get_at((cam_x, cam_y - focal_dist))[0]
     # For car to go upward we must reduce the value of y axis hence y-focl dist
     # Returns a  list, fetch 1st element of list
     down_px = window.get_at((cam_x, cam_y + focal_dist ))[0]
     right_px = window.get_at((cam_x + focal_dist, cam_y ))[0]
     print(upper_px,right_px,down_px)
     # Car to move right, change x axis value, y axis reamins same
     if direction == 'upward'and upper_px !=255 and right_px == 255: # Change Direction
          direction = 'right'
          cam_x_offset = 30 # gets added to cam_x eventually
          car = pygame.transform.rotate(car, -90) # Rotate clockwise(90 degrees) to turn right
          # Camera goes to the back of the car upon rotation, hence we declare cam offset
     elif direction == 'right' and right_px != 255 and down_px == 255:
          direction = 'downward'
          car_x = car_x + 30 # Car goes off axis after transform hence change x value to bring it back on track
          cam_x_offset = 0
          cam_y_offset = 30
          car = pygame.transform.rotate(car, -90)
     elif direction == 'downward' and down_px != 255 and right_px == 255: # track5
          direction = 'right'
          car_y = car_y + 30
          cam_x_offset = 30
          cam_y_offset = 0
          car = pygame.transform.rotate(car, 90) # Rotate clockwise
     elif direction == 'right' and right_px != 255 and upper_px == 255:
          direction = 'upward'
          car_x =  car_x + 30
          cam_x_offset = 0
          car = pygame.transform.rotate(car, 90) 
     
     # DRIVE
     if direction == 'upward' and upper_px == 255: # If upper px is white, the car goes forward
          car_y = car_y - 2
     elif direction =='right' and right_px == 255: # If right px is white and road exists
          car_x = car_x + 2
     elif direction == 'downward' and down_px == 255:
          car_y = car_y + 2 # opp of upward

     window.blit(track,(0,0)) # Transfer the image as block
     window.blit(car,(car_x,car_y)) # Position the car on the track
     pygame.draw.circle(window,(0,255,0,),(cam_x,cam_y),5,5)
     # Draw a circle, on top of window
     # 2nd param is RGB colors, R=0, G=255, B =0 , hence our cam is green
     # 3rd param is center or position of camera
     # 4th param is radius
     # 5th param is width of camera lens
     pygame.display.update() # Update the display when new elements are added

