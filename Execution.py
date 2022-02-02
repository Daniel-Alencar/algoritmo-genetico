from bitstring import BitArray

# ===========================================================================

generations = 1

# ===========================================================================

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
