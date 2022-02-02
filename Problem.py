from bitstring import BitArray 
import math
from random import randint

class Problem:

  def generateInitPopulation(self):
    population: BitArray = []
    for counter in range(4):
      value = int(randint(-10, 10))
      value_bitstring = BitArray(int=value, length=5)
      population.append(value_bitstring)
    return population