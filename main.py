import pygame
import random

pygame.init()
A = 500
size = 25
x = random.randrange(0,A,size)
y = random.randrange(0,A,size)
x_apple = random.randrange(0,A,size)
y_apple = random.randrange(0,A,size)
screen = pygame.display.set_mode((A,A))
pygame.display.set_caption("Змейка")
FPS = 3
up = True
down = True
left = True
right = True
dx = 0
dy = 0
length = 1
clock = pygame.time.Clock()
snake = [(x,y)]

while True:
  clock.tick(FPS)
  screen.fill('BLACK')
  for i,j in snake:
       pygame.draw.rect(screen,"green",(i,j,size,size))

  pygame.draw.rect(screen,"red",(x_apple,y_apple,size,size))

  pygame.display.update()
  key = pygame.key.get_pressed()
  if key[pygame.K_UP] and up == True:
       dx = 0
       dy = -1
       up = True
       down = False
       left = True
       right = True
  if key[pygame.K_DOWN] and down == True:
         dx = 0
         dy = 1
         up = False
         down = True
         left = True
         right = True
  if key[pygame.K_RIGHT] and right == True:
         dx = 1
         dy = 0
         up = True
         down = True
         left = False
         right = True
  if key[pygame.K_LEFT] and left == True:
         dx = -1
         dy = 0
         up = True
         down = True
         left = True
         right = False
  x += dx * size
  y += dy * size
  snake.append((x,y))
  snake = snake[-length:]

  if snake[-1] == (x_apple, y_apple):
     x_apple = random.randrange(0,A,size)
     y_apple = random.randrange(0,A,size)
     length += 1
     FPS += 1
  if x < 0 or x > A or y < 0 or y > A:
       break
  if len(snake) != len(set(snake)): 
       break
  for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
