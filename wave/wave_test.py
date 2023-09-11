import pygame

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 640

xpos = SCREEN_WIDTH/2
ypos = SCREEN_HEIGHT/2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((102, 102, 102))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.draw.line(screen, (0, 0, 0), [500, 10], [500, 200], 5)
    pygame.draw.line(screen, (0, 0, 0), [600, 50], [600, 150], 5)

    pygame.draw.line(screen, (0, 0, 0), [500, 100], [100, 100], 5)
    pygame.draw.line(screen, (0, 0, 0), [100, 100], [100, 500], 5)
    pygame.draw.line(screen, (0, 0, 0), [100, 500], [1000, 500], 5)
    pygame.draw.line(screen, (0, 0, 0), [1000, 500], [1000, 100], 5)
    pygame.draw.line(screen, (0, 0, 0), [1000, 100], [600, 100], 5)

    pygame.draw.circle(screen, (0, 0, 0), (xpos, ypos), 10)

    pygame.display.update()
