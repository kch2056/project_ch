import pygame

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 340

xpos = 0
ypos = SCREEN_HEIGHT

xspeed = 0.0001 * SCREEN_WIDTH
yspeed = -0.0001 * SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((102, 102, 102))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    xpos = xpos + xspeed
    ypos = ypos + yspeed

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 60)

    pygame.display.update()
