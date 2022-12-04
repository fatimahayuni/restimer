import sys, pygame
pygame.display.init()
size = width, height = 800, 600
background_color_rgb = (0, 0, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Balls")
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Clear the screen, render the ball and display.
    screen.fill(background_color_rgb)
    pygame.draw.circle(screen, (255,0,0), (50,50), 10)
    pygame.draw.circle(screen, (0,255,0), (100,50), 10)
    pygame.display.flip()