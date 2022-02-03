from Problem import Problem
from Algorithm import Algorithm

problem = Problem()
population = problem.generateInitPopulation()
# ===================================================================

algorithm = Algorithm(0.6, 0.01, population)

# Algoritmo
algorithm.execution(limit_generations = 100, limit_not_improvement = 10)

index = algorithm.aptidao.index(max(algorithm.aptidao))

print("RESULTADO:")
print("x =", algorithm.population[index].int)
print("f(x) =", algorithm.function(algorithm.population[index].int))