import math
from random import random

generations = 1

# ===========================================================================

def convertBinaryValuesToNumbers(list):
  return []

def generateInitPopulation():
  list = []
  for c in range(3):
    list.append('{:0b}'.format(int(math.floor(random() * 21) - 10)).zfill(5))
  return list

# Dentro desta função será calculada a f(x)
def f(x):
  return (x**2 - 3*x + 4)

# Os menores valores de f(x) devem ter maiores aptidões
# Ou seja, podemos inverter e usarmos 0 - f(x)
def fitness(population):
  values = convertBinaryValuesToNumbers(population)
  aptidao = []
  for x in values:
    aptidao.append(0 - f(x))
  return aptidao

# Divisão da probabilidade de seleção (equação do slide 32)
def seletionProbability(list):
  soma = 0
  for value in list:
    soma += value
  
  probabilities = []
  for value in list:
    probabilities.append(value / soma)
  return probabilities

# Faz o crossover com a probabilidade X de haver algum crossover
# O ponto de corte do crossover pode ser aleatório
def crossover(list, probability):
  return []

# Faz a mutação com a probabilidade X de algum dos bits terem mutação
def mutate(list, probability):
  return []

# ===========================================================================

# gerar a população inicial
population = generateInitPopulation()

# Os menores valores de f(x) devem ter maiores aptidões
# Esta lógica deve ser feita na função fitness()
capacities = fitness(population)

# Divisão da probabilidade de seleção (equação do slide 32)
seletion = seletionProbability(capacities)


# repetir enquanto o critério de parada não for atingido
while True:
  # selecionar os indivíduos
  # Selecionar dois indivíduos mais prováveis definidos em 'seletion'
  cromossomos = ['01001', '01110']
  # criar novos indivíduos (crossover e mutação)

  # crossovedCromossomos é uma lista com 4 elementos
  crossovedCromossomos = crossover(cromossomos)
  # mutatedCromossomos é uma lista com 4 elementos
  mutatedCromossomos = mutate(crossovedCromossomos)

  # armazenar os novos indivíduos
  population = mutatedCromossomos
  # avaliar os indivíduos
  capacities = fitness(population)
  seletion = seletionProbability(capacities)

  generations += 1

  # Quando parar:
  # - número de gerações
  # - convergência
  #     nas últimas k gerações não houve melhora na:
  #        - aptidão média
  #        - aptidão máxima
  if generations == 5:
    print('O melhor indivíduo foi:', population[max(seletion)])
    break
