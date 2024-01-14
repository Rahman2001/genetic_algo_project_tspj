import random


def job_exchange_mutation(population):

    for individual in population:
        jobs = individual[1]
        # generate two random indices to exchange in jobs
        rand_ind = random.sample((0, len(jobs) - 1), 2)
        # swap operation
        temp = jobs[rand_ind[0]]
        jobs[rand_ind[0]] = jobs[rand_ind[1]]
        jobs[rand_ind[1]] = temp
        individual[1] = jobs

    return population
