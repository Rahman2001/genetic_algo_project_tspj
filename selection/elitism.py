
def elitism(current_population, prior_population, evaluation_function):
    best_prior_individual = []
    for individual in prior_population:
        best_prior_individual.append(evaluation_function(individual[0], individual[1]))
    current_population.append(min(best_prior_individual))
    return current_population
