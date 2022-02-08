from Problem import Problem
from Algorithm import Algorithm

limit_inferior = -10
limit_superior = 10

problem = Problem()
population = problem.generateInitPopulation(limit_inferior, limit_superior)

# ==========================================================================

algorithm = Algorithm(0.8, 0.01, population,limit_inferior, limit_superior)

# Algoritmo
algorithm.execution(limit_generations = 100, limit_not_improvement = 10)

index = algorithm.aptidao.index(max(algorithm.aptidao))
value = algorithm.population[index].int

print("\nRESULTADO:")
print("x =", value)
print("f(x) =", algorithm.function(value))