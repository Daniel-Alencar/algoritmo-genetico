from bitstring import BitArray
from random import randint
import random
import numpy as np

class Algorithm:

  def __init__(self, probability_crossover: float, probability_mutation: float):
    self.probability_crossover = probability_crossover
    self.probability_mutation = probability_mutation
    self.aptidao = []
    self.generations = 0

  # Dentro desta função será calculada a f(x)
  def function(self, x):
    return (x**2 - 3*x + 4)

  # Os menores valores de f(x) devem ter maiores aptidões
  # Ou seja, podemos inverter e usarmos 0 - f(x)
  def fitness(self, population: BitArray):
    self.aptidao = []
    for item in population:
      self.aptidao.append(0 - self.function(item.int))
    return self.aptidao

  # Divisão da probabilidade de seleção (equação do slide 32)
  def probabilitySelection(self, aptidao):
    soma = 0
    for value in aptidao:
      soma += value
    
    self.probabilities = []
    for value in aptidao:
      self.probabilities.append(value / soma)
    return self.probabilities

  # Faz o crossover com a probabilidade X de haver algum crossover
  # O ponto de corte do crossover pode ser aleatório
  def crossover(self, population: BitArray):

    # Pegar os dois cromossomos mais promissores
    aptidao_list = self.aptidao.copy()

    promising_index = []

    index = aptidao_list.index(max(aptidao_list))
    aptidao_list.pop(index)
    promising_index.append(index)
    index = aptidao_list.index(max(aptidao_list))
    aptidao_list.pop(index)
    promising_index.append(index)

    # Calcular a probabilidade
    value = random.random()
    print("Valor aleatório:", value)

    if value <= self.probability_crossover:
      print("\nFazendo crossover...")

      # 0|0|1|0|0
      ponto_de_corte = int(randint(1, 4))
      print("\nPonto de corte:", ponto_de_corte)
      crossoved_cromossomos = []

      # Fazer o fatiamento
      print("\nOs escolhidos:")
      for i in range(0, 2):
        print(population[promising_index[i]].bin)
        new = population[promising_index[i]][:ponto_de_corte] + population[promising_index[(i+1) % 2]][ponto_de_corte:]
        crossoved_cromossomos.append(new)

      return crossoved_cromossomos
      
    return [population[promising_index[0]], population[promising_index[1]]]


  # Faz a mutação com a probabilidade X de algum dos bits terem mutação
  def mutation(self, population: BitArray):

    mutated_cromossomos = []
    for cromossomo in population:

    # Calcular a probabilidade
      value = random.random()

      if value <= self.probability_mutation:

        # Posição da mutação
        position = randint(0, 4)
        print("Posição da mutação:", position)

        # Mutação
        bit_string = cromossomo.bin
        list_bits = list(bit_string)
        if list_bits[position] == '0':
          list_bits[position] = '1'
        else:
          list_bits[position] = '0'
        bit_string = "".join(list_bits)
        new = BitArray(bin=bit_string)
      
        mutated_cromossomos.append(new)
      else:
        mutated_cromossomos.append(cromossomo)

    return mutated_cromossomos
