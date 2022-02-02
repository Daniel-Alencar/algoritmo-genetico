from Problem import Problem
from Algorithm import Algorithm

problem = Problem()
population = problem.generateInitPopulation()

print("\nPopulação:")
for item in population:
  print(item.bin)

# ===================================================================

algorithm = Algorithm(0.6, 0.01)

print("\nCrossover:", algorithm.probability_crossover)

aptidao = algorithm.fitness(population)
crossoved_population = algorithm.crossover(population)

print("\nCrossoved:")
for item in crossoved_population:
  print(item.bin)

print("\nMutated:")
mutated_population = algorithm.mutation(crossoved_population)
for item in mutated_population:
  print(item.bin)