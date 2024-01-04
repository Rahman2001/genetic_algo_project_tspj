from random import randint
# RR = Random Route algorithm which generates routes randomly with probability a1 (alpha1)


def random_route(vertices):
    rand_route = []

    while rand_route.__len__() != len(vertices):
        rand_index = randint(0, len(vertices) - 1)
        next_route = vertices[rand_index]
        if not next_route.is_visited:
            rand_route.append(vertices[rand_index].number)
            next_route.set_visited(True)

    rand_route.append(rand_route[0])

    return rand_route

