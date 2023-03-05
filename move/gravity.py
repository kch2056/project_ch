import pygame

pygame.init()

SCREEN_WIDTH = 340
SCREEN_HEIGHT = 640

xpos = SCREEN_WIDTH/2
ypos = 0

yspeed = 0.001

gravity = 0.00005

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((102, 102, 102))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    yspeed = yspeed + gravity
    ypos = ypos + yspeed

pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 60)

pygame.display.update()
