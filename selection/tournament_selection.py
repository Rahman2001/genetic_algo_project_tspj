import random


def tournament_selection(size, population, fitness_function):
    parent_size = 2
    record = {}
    parents_index = []

    for i in range(parent_size):
        random_selection = random.sample(range(0, len(population)), size)
        print("Randomly selected individuals are: " + str(random_selection))
        if parents_index.__len__() > 0 and parents_index[0] in random_selection:
            random_selection = random.sample([i for i in range(len(population)) if i != parents_index[0]], size)
            print("Randomly re-selected individuals are: " + str(random_selection))

        for index in random_selection:
            fit_value = fitness_function(population[index])
            record.__setitem__(fit_value, index)

        best = max(list(record.keys()))
        index_of_individual = record.get(best)
        parents_index.append(index_of_individual)
        print("The fitness value of randomly selected individuals are: " + str(list(record.keys())))
        print("The vertices of individual number: " + str(index_of_individual) + " are: " +
              str([vertex.number for vertex in population[index_of_individual][0]]))
        record = {}

    return parents_index



