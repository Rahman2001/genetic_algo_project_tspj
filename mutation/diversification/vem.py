import random


def vertex_exchange_mutation(individual):
    route = individual[0]
    # generate two random indices to exchange in route
    rand_ind = random.sample((0, len(route)-1), 2)
    # swap operation
    temp = route[rand_ind[0]]
    route[rand_ind[0]] = route[rand_ind[1]]
    route[rand_ind[1]] = temp

    individual[0] = route
    return individual
