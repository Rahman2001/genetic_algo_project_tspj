from random import randint

from domain.job import Job
from domain.vertex import Vertex
from initial_population.route_construction.nearest_neighbor import nearest_neighbor
from initial_population.route_construction.random_route import random_route
from initial_population.job_assignment.rap import rap
from initial_population.job_assignment.nnja import nnja


def main():
    v1 = Vertex(2)
    v2 = Vertex(4)
    v3 = Vertex(11)
    v4 = Vertex(43)
    v5 = Vertex(23)
    v6 = Vertex(13)

    v_list = [v1, v2, v3, v4, v5, v6]
    for i in range(v_list.__len__()):
        for j in range(v_list.__len__()):
            if i != j:
                v_list[i].add_neighbor_distance(v_list[j], randint(1, 40))

    # nn = nearest_neighbor(v_list)
    # print([vertex.number for vertex in nn])
    # rr = random_route(v_list)
    # print(rr)

    # j1 = Job(2, 23)
    # j2 = Job(4, 11)
    # j3 = Job(9, 44)
    # j4 = Job(10, 12)
    # j5 = Job(22, 6)
    #
    # j_list = [j1, j2, j3, j4, j5]

    # rand_job = rap(j_list)
    # print(rand_job)
    #
    # nnja_job = nnja(nn, j_list)
    # print([job.number for job in nnja_job])


main()
