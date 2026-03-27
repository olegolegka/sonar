print("Добро пожаловать в приложение 'сундукивмореискатор(сонар)'")

import random

cells = []
lines = [[], [], [], [], [],[], [], [], [], []]
x_chests = []
y_chests = []

def field():
  for i in range(10):
    for j in range(10):
      lines[i].append('~ ')

def output():
  num = 0
  print('  0 1 2 3 4 5 6 7 8 9')
  for i in lines:
    cells = ''
    for j in i:
      cells += j
    print(num, cells)
    num += 1

def chests():
  for i in range(3):
    x_chests.append(random.randint(0, 9))
    y_chests.append(random.randint(0, 9))

field()
chests()
output()

score = 0
while score < 3:
  x = int(input('введите координату x:\t'))
  y = int(input('введите координату y:\t'))
  lines[y][x] = 'x '
  for i in range(0, 3, 1):
    if x == x_chests[i] and y == y_chests[i]:
      lines[y][x] = '1 '
      score += 1
      print('вы нашли', score, 'сундуков.')
    elif x == x_chests[i]:
      lines[y][x] = str(abs(y - y_chests[i])) + ' '
    elif y == y_chests[i]:
      lines[y][x] = str(abs(x - x_chests[i])) + ' '
  output()
