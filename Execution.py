from Problem import Problem
from Algorithm import Algorithm

problem = Problem()
population = problem.generateInitPopulation()
# ===================================================================

algorithm = Algorithm(0.8, 0.01, population)

# Algoritmo
algorithm.execution(limit_generations = 500, limit_not_improvement = 100)

index = algorithm.aptidao.index(max(algorithm.aptidao))
value = algorithm.population[index].int

print("\nRESULTADO:")
print("x =", value)
print("f(x) =", algorithm.function(value))