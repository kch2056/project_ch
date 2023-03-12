import pygame 
import random

# 초기화
pygame.init()

# 창 생성
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 340
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 시계 변수
clock = pygame.time.Clock()

# 원 정보
rad = 10
xpos = SCREEN_WIDTH/2
ypos = SCREEN_HEIGHT/2

xspeed = random.randrange(10) - 5
yspeed = random.randrange(10) - 5

xdirection = 1
ydirection = 1

color = pygame.Color((255, 255, 255))
alpha = 10  # 투명도 값 (0~255)

# Surface 객체 생성
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
background.fill((0, 0, 0, alpha))

# 메인 루프
running = True
while running : 
    # 이벤트 처리
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            running = False
    
    xpos = xpos + (xspeed * xdirection)
    ypos = ypos + (yspeed * ydirection)

    if xpos > SCREEN_WIDTH-rad or xpos < rad : 
        xdirection *= -1
    if ypos > SCREEN_HEIGHT-rad or ypos < rad : 
        ydirection *= -1

    # 잔상 그리기
    screen.blit(background, (0, 0))
    pygame.draw.circle(screen, color, (xpos, ypos), rad)

    # 화면 업데이트
    pygame.display.update()

    # 초당 프레임 설정
    clock.tick(60)

# 게임 종료
pygame.quit()