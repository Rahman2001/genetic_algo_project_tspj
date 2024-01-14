import random

from mutation.diversification.rm import reverse_mutation
from mutation.diversification.sm import successor_mutation
from mutation.diversification.vem import vertex_exchange_mutation
from mutation.diversification.two_opt import two_opt
from mutation.intensification.jem import job_exchange_mutation
from mutation.intensification.lsja import lsja


def mutation(sigma1, sigma2, sigma3, sigma4, sigma5, sigma6, sigma7, sigma8, population):
    random_prob = random.random()
    if random_prob <= sigma1:
        random_prob = random.random()

        if random_prob <= sigma3:
            return vertex_exchange_mutation(population)
        elif random_prob <= sigma3 + sigma4:
            return reverse_mutation(population)
        elif random_prob <= sigma3 + sigma4 + sigma5:
            return successor_mutation(population)
        elif random_prob <= sigma3 + sigma4 + sigma5 + sigma6:
            return two_opt(population)

    random_prob = random.random()
    if random_prob <= sigma2:

        random_prob = random.random()
        if random_prob <= sigma7:
            return lsja(population)
        elif random_prob <= sigma7 + sigma8:
            return job_exchange_mutation(population)
