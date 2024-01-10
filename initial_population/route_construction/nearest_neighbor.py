from random import randint


def nearest_neighbor(vertices):
    ver_size = len(vertices)
    p = randint(0, ver_size - 1)
    # print("Random starting point/index is: ", p)
    # print("Given vertices are: ")
    # print([i.number for i in vertices])
    # to keep track of visited vertices
    record = {}
    # random starting point/vertex
    start_vertex = vertices[p]
    # route_path path initialization
    route_path = [start_vertex]
    neighbor_candidate_index = 0

    while route_path.__len__() != ver_size:  # the last index must be the depot
        next1_distance = start_vertex.distances[neighbor_candidate_index]
        next1_vertex = start_vertex.neighbors[neighbor_candidate_index]
        # print("starting vertex is: " + str(start_vertex.number) + " and Neighbors are: " +
        #       str([n.number for n in start_vertex.neighbors]) + " with distances: " +
        #       str([n for n in start_vertex.distances]))
        # print("route_path is: " + str(route_path))

        for i in range(len(start_vertex.neighbors)):
            next2_vertex = start_vertex.neighbors[i]
            next2_distance = start_vertex.distances[i]

            if next2_distance <= next1_distance and record.get(next2_vertex.number) is None:
                # print("For P=" + str(p) + " which is " + "next2_vertex is " + str(next2_vertex.number))
                next1_vertex = next2_vertex
                next1_distance = next2_distance

        if record.get(next1_vertex.number) is not None:
            neighbor_candidate_index = neighbor_candidate_index + 1
            # print("neighbor_candidate_index is updated: +1")

        else:
            record.__setitem__(start_vertex.number, next1_vertex.number)
            start_vertex = next1_vertex
            route_path.append(start_vertex)

        # print("Keys in record are: " + str([k for k in record]))
        # print("Values in record are: " + str([v for v in record.values()]) + "\n")

    record.__setitem__(start_vertex.number, route_path[0])
    route_path.append(route_path[0])

    # print(route_path)
    return route_path
