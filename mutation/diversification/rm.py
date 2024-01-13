import random


def reverse_mutation(individual):
    # we chose sample length of job because we don't want to include depots in the route array
    rand_int = random.sample((1, len(individual[1]) - 2), 2)
    print("rand_int: " + str([i for i in rand_int]))

    # reverse items in selected range
    range_of_individual = [individual[0][j] for j in range(0, len(individual[0])) if rand_int[0] <= j <= rand_int[1]]

    for j in range(rand_int[0], rand_int[1]):
        individual[0][j] = range_of_individual.pop()

    return individual
