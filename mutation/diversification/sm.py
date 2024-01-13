from random import randint


def successor_mutation(individual):
    # we don't want to include last index. -1 for making index valid in range of array and -1 for excluding last index
    rand_ind = randint(0, len(individual[1])-2)
    # swap operation between random index and its successor
    for i in range(len(individual)):
        if i == 0:
            rand_ind = rand_ind + 1
        temp = individual[i][rand_ind]
        individual[i][rand_ind] = individual[rand_ind+1]
        individual[i][rand_ind+1] = temp

    return individual

