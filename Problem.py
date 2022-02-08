import math
from bitstring import BitArray 
from random import randint
import numpy as np

class Problem:

  def generateInitPopulation(self, limit_inferior: int, limit_superior: int):
    population: BitArray = []
    values = []
    for counter in range(4):
      value = int(randint(limit_inferior, limit_superior))
      values.append(value)

    lengths = []

    lengths.append(np.log2(2 * (limit_superior + 1)))
    lengths.append(np.log2(2 * (abs(limit_inferior))))

    length = (math.ceil(int(max(lengths)) + 1))

    for value in values:
      value_bitstring = BitArray(int = value, length = int(length))
      population.append(value_bitstring)
    
    return population
