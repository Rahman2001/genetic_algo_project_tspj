from domain.job import Job


class Vertex:

    def __init__(self, number):
        self.number = number
        self.neighbors = []
        self.distances = []
        self.is_visited = False
        self.job = Job(0, 0)

    def add_neighbor_distance(self, vertex, distance):
        self.neighbors.append(vertex)
        self.distances.append(distance)

    def set_job(self, job):
        self.job = job

    def set_visited(self, is_visited):
        self.is_visited = is_visited

