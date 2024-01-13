import random


def reverse_mutation(individual):
    # we chose sample length of job because we don't want to include depots in the route array
    rand_int = random.sample((0, len(individual[1])-1), 2)
    print("rand_int: " + str([i for i in rand_int]))

    # reverse items in selected range
    for i in range(len(individual)):
        range_of_individual = [individual[i][j] for j in range(0, len(individual[i])) if rand_int[0] <= j <= rand_int[1]]
        # we don't want to include depots in the route array of individual
        if i == 0:
            range_of_individual = [individual[i][j+1] for j in range(0, len(individual[i])) if rand_int[0] <= j <= rand_int[1]]
        for j in range(rand_int[0], rand_int[1] + 1):
            index = j
            # wa want to reverse sub-tours by excluding depots in the route array
            if i == 0:
                index = index + 1
            individual[i][index] = range_of_individual.pop()

    return individual
