

import pygame
from random import randrange

#размер окна:
A = 500
#шаг змейки
size = 50
#координаты головы змейки
x = randrange(0, A, size)
y = randrange(0, A, size)
#координаты яблока
xapple = randrange(0, A, size)
yapple = randrange(0, A, size)
#частота смены кадров
fps = 5
#начальное направление
dx = 0
dy = 0
#разрешаем движение во всех направлениях
UP = True
DOWN = True
RIGHT = True
LEFT = True
#список координат змейки:
snake = [(x, y)]
#длина змейки:
length = 1

#инициализируем библиотеку:
pygame.init()
#вызов окна:
win = pygame.display.set_mode((A, A)) 
#даём окну название:
pygame.display.set_caption("Змейка")
#объект для регулирования скорости змейки
clock = pygame.time.Clock()

#основной цикл:
while True:
  clock.tick(fps)
#закрашиваем фон
  win.fill(pygame.Color('blue'))
#рисуем змейку, состоящую из зелёных квадратов
  for i, j in snake:
    pygame.draw.rect(win, 'green', (i, j, size, size))
#рисуем красное яблоко
  pygame.draw.rect(win, 'red', (xapple, yapple, size, size))
#обновляем экран
  pygame.display.update()
#проверка на закрытие приложения
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
#управление змейкой
  key = pygame.key.get_pressed()
  if key[pygame.K_UP] and UP:
    dx = 0
    dy = -1
    UP = True
    DOWN = False
    RIGHT = True
    LEFT = True
  if key[pygame.K_DOWN] and DOWN:
    dx = 0
    dy = 1
    UP = False
    DOWN = True
    RIGHT = True
    LEFT = True
  if key[pygame.K_RIGHT] and RIGHT:
    dx = 1
    dy = 0
    UP = True
    DOWN = True
    RIGHT = True
    LEFT = False
  if key[pygame.K_LEFT] and LEFT:
    dx = -1
    dy = 0
    UP = True
    DOWN = True
    RIGHT = False
    LEFT = True
  x += dx * size
  y += dy * size
  #добавляем каждый шаг змейки в её список координат
  snake.append((x, y))
  #срез координат в соответствии с длиной змейки
  snake = snake[-length:]

    #змейка ест яблоко
  if snake[-1] == (xapple, yapple):
    xapple = randrange(0, A, size)
    yapple = randrange(0, A, size)
    length += 1
    fps += 0.5

      #условие проигрыша
  if x < 0 or x > A or y < 0 or y > A:
    break
  if len(snake) != len(set(snake)):
    break
