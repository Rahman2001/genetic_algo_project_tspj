from random import randint
# Random Assignment Permutation (RAP)
# Randomly assigns jobs by constructing an array of jobs


def rap(jobs):
    rand_job = []

    while rand_job.__len__() != len(jobs):
        rand_index = randint(0, len(jobs) - 1)
        next_job = jobs[rand_index]
        if not next_job.is_completed:
            rand_job.append(jobs[rand_index].number)
            next_job.set_job_completed(True)

    return rand_job
