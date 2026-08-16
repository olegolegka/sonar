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
  if key[pygame.K_UP]:
       pass # ВОТ ТУТ ОСТАНОВИЛИСЬ!!!!!!!!! TO DO!!!!!!
  
  for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
