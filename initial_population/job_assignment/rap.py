import random
# Random Assignment Permutation (RAP)
# Randomly assigns jobs by constructing an array of jobs


def rap(jobs):
    rand_job = []
    rand_index = random.sample(range(0, len(jobs)-1), len(jobs)-1)

    for index in rand_index:
        rand_job.append(jobs[index])

    return rand_job
