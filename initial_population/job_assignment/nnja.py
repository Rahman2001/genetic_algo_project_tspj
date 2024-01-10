

def nnja(route_path, jobs):

    # job number must be equal to the vertices number to be visited
    if len(jobs) == len(route_path) - 2:
        print("Passed the IF statement!\n")
        # sort jobs with the highest completion time in decreasing order
        for i in range(len(jobs)):
            job = jobs[i]
            for j in range(i+1, len(jobs)):
                if job.time_to_complete < jobs[j].time_to_complete:
                    temp = jobs[i]
                    jobs[i] = jobs[j]
                    jobs[j] = temp

                    job = jobs[i]
            route_path[i+1].set_job(job)
            print("The job number " + str(job.number) + " has the highest completion time " + str(job.time_to_complete))

        return jobs

    print("Could not pass the IF statement!\n")
    return None
