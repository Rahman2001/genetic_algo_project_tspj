import random
from random import randint
# RR = Random Route algorithm which generates routes randomly with probability a1 (alpha1)


def random_route(vertices):
    rand_route = []
    rand_indices = random.sample(range(0, len(vertices) - 1), len(vertices) - 1)
    # print(rand_indices)
    for index in rand_indices:
        rand_route.append(vertices[index])

    rand_route.append(rand_route[0])

    return rand_route

