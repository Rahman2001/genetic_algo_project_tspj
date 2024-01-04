
class Job:

    def __init__(self, number, time_to_complete):
        self.number = number
        self.time_to_complete = time_to_complete
        self.is_completed = False

    def set_job_completed(self, is_completed):
        self.is_completed = is_completed

