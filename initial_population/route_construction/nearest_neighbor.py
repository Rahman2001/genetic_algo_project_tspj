from random import randint


def nearest_neighbor(vertices):
    p = randint(0, vertices.size - 1)
    # to keep track of visited vertices
    record = {}
    # route_path path initialization
    route_path = []

    while route_path.__len__() != vertices.size + 1:  # the last index must be the depot
        # random starting point/vertex
        start_vertex = vertices[p]
        route_path.append(start_vertex.number)
        record.__setitem__(start_vertex.number, None)
        next1_distance = start_vertex.distances[0]
        next1_vertex_number = start_vertex.neighbors[0].number

        for i in range(start_vertex.neighbors.lenght):
            next2_vertex_number = start_vertex.neighbors[i].number
            next2_distance = start_vertex.distances[i]

            if next2_distance < next1_distance & record.get(next2_vertex_number) is None:
                next1_vertex_number = next2_vertex_number
                p = i
                record.__setitem__(start_vertex.number, next1_vertex_number)

            elif route_path.__len__() == vertices.size & next2_vertex_number == route_path[0]:
                record.__setitem__(start_vertex.number, route_path[0].number)
                route_path.append(route_path[0].number)

    return route_path
