# 물리융합 코딩 예제

## pygame 초기화

> 📝 pygame을 import하고 초기화 하는 코드

```python
import pygame

pygame.init()
```

</br>

## pygame 실행

> 📝 pygame을 실행하는 코드

```python
pygame.display.update()
```

</br>

## screen 생성

> 📝 가로 640, 세로 340인 screen을 생성하는 코드

```python
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 340

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
```

</br>

## QUIT 설정

> 📝 QUIT를 누를때까지 반복되게 하는 코드

```python
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
```

</br>

## screen 색상 설정

> 📝 screen의 색상을 r, g, b 순서대로 102, 102, 102를 채운 코드

```python
while run:
    screen.fill((102, 102, 102))
```

</br>

## 공 설정

> 📝 screen에 위치가 (xpos, ypos)이고 반지름이 60인 원 생성하는 코드

```python
xpos = SCREEN_WIDTH/2
ypos = SCREEN_HEIGHT/2

pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 60)
```

</br>

## 등속 운동

> 📝 공이 (0, SCREEN_HEIGHT)에서 x축으로 0.001*SCREEN_WIDTH, y축으로 -0.001*SCREEN_HEIGHT만큼 등속 운동하는 코드

```python
xpos = 0
ypos = SCREEN_HEIGHT

xspeed = 0.001 * SCREEN_WIDTH
yspeed = -0.001 * SCREEN_HEIGHT
while run:
    xpos = xpos + xspeed
    ypos = ypos + yspeed
```

</br>

## 등가속도 운동

> 📝 (SCREEN_WIDTH/2, 0)에서 y축으로 0.001*SCREEN_HEIGHT만큼 등속 운동하는 공이 y축으로 0.00005*SCREEN_HEIGHT만큼 등가속도 운동하는 코드

```python
SCREEN_WIDTH = 340
SCREEN_HEIGHT = 640

xpos = SCREEN_WIDTH/2
ypos = 0

yspeed = 0.001

gravity = 0.00005

while run:
    yspeed = yspeed + gravity
    ypos = ypos + yspeed
```

</br>

## 공기저항

> 📝 위같은 속도로 등가속도 운동하는 공에 resist만큼의 저항을 걸어주는 코드

```python
resist = 0.9998

gravity = gravity*resist
```
