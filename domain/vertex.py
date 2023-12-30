from job import Job


class Vertex:
    number = 0
    neighbors = []  # [Vertex]
    distances = []  # [distance for each vertex] in neighbors[i]
    job = Job

    def __init__(self, number):
        self.number = number

    def add_neighbor_distance(self, vertex, distance):
        self.neighbors.append(vertex)
        self.distances.append(distance)

