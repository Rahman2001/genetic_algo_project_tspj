from domain.job import Job


class Vertex:

    def __init__(self, number):
        self.number = number
        self.neighbors = []
        self.distances = []
        self.neighbor_dict = {}
        self.is_visited = False
        self.is_depot = False
        self.job = Job(0, 0)

    def add_neighbor_and_distance(self, vertex, distance):
        self.neighbors.append(vertex)
        self.distances.append(distance)
        self.neighbor_dict.__setitem__(vertex.number, distance)

    def set_job(self, job):
        self.job = job

    def set_visited(self, is_visited):
        self.is_visited = is_visited

    def set_as_depot(self):
        self.is_depot = True

