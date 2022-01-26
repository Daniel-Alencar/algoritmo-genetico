import math
from random import random

from numpy import floor

a, b = -10, 10
X = [11111111]
init = 4
mutation = 0.01
crossover = 0.6
battle = 2
generations = 5

def f(x):
  return x ** 2 - 3 * x + 4

def generateInitPopulation():
  list = []
  for c in range(3):
    list.append(int(math.floor(random() * 21) - 10))
  return list

print(generateInitPopulation())

print('{:0b}'.format(generateInitPopulation()).zfill(5))

list = []

list.append(bin(1))
list.append(bin(2))
list.append(bin(3))
list.append(bin(4))

    