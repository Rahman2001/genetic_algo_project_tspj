
def evaluate_individual(individual):
    # individual consists of route and jobs -> individual = [][] -> [1][route], [2][jobs]
    # max[ jobs[0] + (distance from depot to next vertex) , max[for each i in (n-2) where i=1 -> sum(
    #                                                               jobs[i] + (distance from depot to next vertex) +
    #                                                               for each l in i where l=1 -> sum(distance[l-1] to distance[l])
    #                                                         )],
    #     (distance from depot to next vertex) + for each l in (n-2) where l=0 ->
    #                                                           sum((distance[l] to distance[l+1]) + distance[n-1] to depot)
    #   ]    where n is vertex size (doesn't include depot and the end of route which is why it's n-2))


