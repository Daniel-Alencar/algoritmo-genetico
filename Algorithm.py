from bitstring import BitArray
from random import randint
import random


class Algorithm:
  def __init__(self, probability_crossover: float, probability_mutation: float, population):
    self.probability_crossover = probability_crossover
    self.probability_mutation = probability_mutation
    self.population = population
    self.generations = 0

    self.fitness()
    self.probabilitySelection()

    self.aptidao_history = []

  # Dentro desta função será calculada a f(x)
  def function(self, x):
    return (x**2 - 3*x + 4)

  # Os menores valores de f(x) devem ter maiores aptidões
  # Ou seja, podemos inverter e usarmos 0 - f(x)
  def fitness(self):
    self.aptidao = []
    for item in self.population:
      self.aptidao.append(0 - self.function(item.int))

  # Divisão da probabilidade de seleção (equação do slide 32)
  def probabilitySelection(self):
    soma = 0
    for value in self.aptidao:
      soma += value
    
    self.probabilities = []
    for value in self.aptidao:
      self.probabilities.append(value / soma)

  def selection(self):
    aptidao_list = self.aptidao.copy()
    promising = []

    for index in range(0, 2):
      maximus = max(aptidao_list)
      promising.append(aptidao_list.index(maximus))
      aptidao_list.pop(aptidao_list.index(maximus))

    return promising

  # Faz o crossover com a probabilidade X de haver algum crossover
  # O ponto de corte do crossover pode ser aleatório
  def crossover(self, population: BitArray):
    # Pegar os dois cromossomos mais promissores
    promising_indexes = self.selection()

    # Calcular a probabilidade
    value = random.random()

    if value <= self.probability_crossover:
      # 0|0|1|0|0
      ponto_de_corte = randint(1, 4)
      crossoved_cromossomos = []

      # Fazer o fatiamento
      for i in range(0, 2):
        new = population[promising_indexes[i]][:ponto_de_corte] + population[promising_indexes[(i + 1) % 2]][ponto_de_corte:]
        while(-10 > new.int > 10):
          new = population[promising_indexes[i]][:ponto_de_corte] + population[promising_indexes[(i + 1) % 2]][ponto_de_corte:]
        crossoved_cromossomos.append(new)

      return crossoved_cromossomos
      
    return [population[promising_indexes[0]], population[promising_indexes[1]]]


  # Faz a mutação com a probabilidade X de algum dos bits terem mutação
  def mutation(self, population: BitArray):
    mutated_cromossomos = []
    for cromossomo in population:
      while True:
        bit_string = cromossomo.bin
        
        for position in range(0, 5):
        # Calcular a probabilidade
          value = random.random()

          if value <= self.probability_mutation:
            # Mutação
            list_bits = list(bit_string)
            if list_bits[position] == '0':
              list_bits[position] = '1'
            else:
              list_bits[position] = '0'
            bit_string = "".join(list_bits)
        
        new = BitArray(bin = bit_string)
        if (-10 <= new.int <= 10):
          break
        
      mutated_cromossomos.append(new)

    return mutated_cromossomos
  
  def generateNewGeneration(self):
    news = []
    for i in range(0, 2):
      crossoved_population = self.crossover(self.population)
      mutated_population = self.mutation(crossoved_population)

      news.append(mutated_population)
    newPopulation = (news[0] + news[1])

    self.population = newPopulation
    self.generations += 1
    self.fitness()
    self.probabilitySelection()
    self.aptidao_history.append(self.aptidao)

    print(self.aptidao)

  def evaluate():
    return True

  def execution(self, limit_generations: int):
    while (self.generations < limit_generations):
      self.generateNewGeneration()
