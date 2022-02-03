from Problem import Problem
from Algorithm import Algorithm

problem = Problem()
population = problem.generateInitPopulation()
# ===================================================================

algorithm = Algorithm(0.6, 0.01, population)

# Algoritmo
algorithm.execution(limit_generations = 50, limit_improvement = 10)