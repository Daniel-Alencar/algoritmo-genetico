from Problem import Problem
from Algorithm import Algorithm

# Variáveis

interval = (-10, 10)
probability_crossover = 0.8
probability_mutation = 0.01
limit_generations = 100
limit_not_improvement = 10

# Definindo o problema

problem = Problem()
population = problem.generateInitPopulation(interval[0], interval[1])

# ==========================================================================

# Algoritmo

algorithm = Algorithm(
  probability_crossover, 
  probability_mutation, 
  population,interval[0], 
  interval[1]
)
algorithm.execution(limit_generations = limit_generations, limit_not_improvement = limit_not_improvement)

index = algorithm.aptidao.index(max(algorithm.aptidao))
value = algorithm.population[index].int

print("\nRESULTADO:")
print("x =", value)
print("f(x) =", algorithm.function(value))