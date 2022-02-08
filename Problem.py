from bitstring import BitArray 
from random import randint

class Problem:

  def generateInitPopulation(self, limit_inferior: int, limit_superior: int):
    population: BitArray = []
    for counter in range(4):
      value = int(randint(limit_inferior, limit_superior))
      value_bitstring = BitArray(int = value, length = 5)
      population.append(value_bitstring)
    return population
