from job import Job


class Vertex:
    number = 0
    neighbors = []  # [Vertex]
    distances = []  # for each distance[i] ->  in neighbors[i]
    job = Job

    def __init__(self, number):
        self.number = number

    def add_neighbor_distance(self, vertex, distance):
        self.neighbors.append(vertex)
        self.distances.append(distance)

    def set_job(self, job):
        self.job = job

