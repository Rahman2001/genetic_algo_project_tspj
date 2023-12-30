from random import randint
# RR = Random Route algorithm which generates routes randomly with probability a1 (alpha1)


def random_route(vertices):
    rand_route = []

    for i in range(vertices.size):
        rand_index = randint(0, vertices.size - 1)
        rand_route.append(vertices[rand_index])

    return rand_route

