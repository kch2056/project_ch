# 물리융합 코딩 예제

## 모듈 생성

> 📝 pygame, random 모듈을 생성하는 코드

```python
import pygame
import random
```

</br>

## 초기화

> 📝 pygame을 초기화 하는 코드

```python
pygame.init()
```

</br>

## 창 생성

> 📝 창을 생성하는 코드

```python
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 340
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
```

</br>

## 원 정보

> 📝 원을 설정하는 코드

```python
rad = 10
xpos = SCREEN_WIDTH/2
ypos = SCREEN_HEIGHT/2

xspeed = random.randrange(10) - 5
yspeed = random.randrange(10) - 5

xdirection = 1
ydirection = 1

color = pygame.Color((255, 255, 255))
alpha = 10  # 투명도 값 (0~255)
```

</br>

## Surface 객체 생성

> 📝 Surface 객체를 생성하는 코드

```python
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
background.fill((0, 0, 0, alpha))
```

</br>

## 메인 루프

> 📝 메인 루프를 설정하는 코드

```python
running = True
while running : 
```

</br>

## 이벤트 처리

> 📝 이벤트를 처리하는 코드

```python
for event in pygame.event.get() : 
    if event.type == pygame.QUIT : 
            running = False
    
xpos = xpos + (xspeed * xdirection)
ypos = ypos + (yspeed * ydirection)

if xpos > SCREEN_WIDTH-rad or xpos < rad : 
        xdirection *= -1
if ypos > SCREEN_HEIGHT-rad or ypos < rad : 
        ydirection *= -1
```

</br>

## 잔상 그리기

> 📝 잔상을 그리는 코드

```python
screen.blit(background, (0, 0))
pygame.draw.circle(screen, color, (xpos, ypos), rad)
```

</br>

## 화면 업데이트

> 📝 화면을 업데이트하는 코드

```python
pygame.display.update()
```

</br>

## 초당 프레임 설정

> 📝 초당 프레임을 설정하는 코드

```python
clock.tick(60)
```

</br>

## 게임 종료

> 📝 게임을 종료하는 코드

```python
pygame.quit()
```