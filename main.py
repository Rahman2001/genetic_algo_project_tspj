from random import randint

from domain.vertex import Vertex
from initial_population.route_construction.nearest_neighbor import nearest_neighbor


def main():
    v1 = Vertex(2)
    v2 = Vertex(4)
    v3 = Vertex(11)
    v4 = Vertex(43)
    v5 = Vertex(23)

    v_list = [v1, v2, v3, v4, v5]
    for i in range(v_list.__len__()):
        for j in range(v_list.__len__()):
            if i != j:
                v_list[i].add_neighbor_distance(v_list[j], randint(1, 40))

    nn = nearest_neighbor(v_list)
    print(nn)


main()
