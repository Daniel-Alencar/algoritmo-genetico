from Problem import Problem
from Algorithm import Algorithm

problem = Problem()
population = problem.generateInitPopulation()

print("\nPopulação:")
for item in population:
  print(item.bin)

# ===================================================================

algorithm = Algorithm(0.6, 0.01)

# Algoritmo

aptidao = algorithm.fitness(population)

news = []

for i in range(0, 2):
  print("\nCrossover:", algorithm.probability_crossover)
  crossoved_population = algorithm.crossover(population)

  print("\nCrossoved cromossomos:")
  for item in crossoved_population:
    print(item.bin)

  print("\nMutation:", algorithm.probability_mutation)
  mutated_population = algorithm.mutation(crossoved_population)

  print("\nMutated cromossomos:")
  for item in mutated_population:
    print(item.bin)

  news.append(mutated_population)

newPopulation = (news[0] + news[1])

# Avaliar os indivíduos
aptidao = algorithm.fitness(newPopulation)
seletion = algorithm.probabilitySelection(aptidao)

if algorithm.generations >= 5:
  print("Dar um 'break'")
