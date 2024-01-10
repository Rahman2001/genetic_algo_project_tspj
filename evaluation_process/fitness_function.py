
def second_element(route, jobs):
    result = []
    for i in range(1, len(route)-2):
        k1 = jobs[i].time_to_complete + route[0].neighbor_dict.get(route[1].number)
        k2 = 0
        # since our route includes depot too, we add +1 to the variable l.
        for l in range(1+1, i+1):
            k2 = k2 + route[l-1].neighbor_dict.get(route[l].number)

        result.append(k1 + k2)

    return result


def third_element(route):
    d1 = route[0].neighbor_dict.get(route[1].number)
    d2 = 0
    # since our route includes depot too, l starts from index 1 in route array.
    for l in range(1, len(route) - 2):
        d2 = d2 + route[l].neighbor_dict.get(route[l+1].number)

    d2 = d2 + route[len(route)-2].neighbor_dict.get(route[0].number)
    return d1 + d2


def evaluate_individual(individual):
    # individual consists of route and jobs -> individual = [][] -> [1][route], [2][jobs]
    # max[ jobs[0] + (distance from depot to next vertex) , max[for each i in (n-2) where i=1 -> sum(
    #                                                               jobs[i] + (distance from depot to next vertex) +
    #                                                               for each l in i where l=1 -> sum(distance[l-1] to distance[l])
    #                                                         )],
    #     (distance from depot to next vertex) + for each l in (n-2) where l=0 ->
    #                                                           sum(distance[l] to distance[l+1]) + (distance[n-1] to depot)
    #   ]    where n is vertex size (doesn't include depot and the end of route which is why it's n-2)

    route = individual[0]
    jobs = individual[1]

    first_elem = jobs[0].time_to_complete + route[0].neighbor_dict.get(route[1].number)
    print("The first_elem result: " + str(first_elem))
    second_elem = max(second_element(route, jobs))
    print("The second_elem result: " + str(second_elem))
    third_elem = third_element(route)
    print("The third_elem result: " + str(third_elem))

    return max([first_elem, second_elem, third_elem])



