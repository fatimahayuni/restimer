import sys, pygame

pygame.display.init()

size = width, height = 800, 600
speedX = 1
speedY = 1
background_color = 0, 0, 0
x = 1
y = 1

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    deltaTime = clock.tick(100)
    deltaTime = min(20.0, deltaTime)
    
    # Move the ball position by the speed values.
    x += speedX * deltaTime
    y += speedY * deltaTime

    # Check if the ball is hitting the edges of the screen and change
    # the speed direction if it does hit.

    # Ball hits left edge.
    if x < 0:
        x = 0 # If this is commented out, no changes to the bouncing ball. This is the formula. 
        speedX = 1 # If this is #edout, then the ball will run against the left edge repeatedly.
       
    # Ball hits right edge.
    if x > width:
        x = width
        speedX = -1 # If this is #edout, then the ball will run against the right edge repeatedly.
       
    # Ball hits top edge.
    if y < 0:
        y = 0
        speedY = 1 # If this is #edout, then the ball will run against the top edge repeatedly.
       
    # Ball hits the bottom edge.  
    if y > height:
        y = height
        speedY = -1 # If this is #edout, then the ball will run against the bottom edge repeatedly.


    # Clear the screen, render the ball (size, color) and display.
    screen.fill(background_color)
    pygame.draw.circle(screen, (255,0,0), (x,y), 10)
    pygame.display.flip()






