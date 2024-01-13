from queue import Queue
from random import randint


def partially_mapped_crossover(parent1, parent2):

    child1 = []
    child2 = []

    for i in range(len(parent1)):
        # print("i is " + str(i) + " and parent1: " + str([j.number for j in parent1[i]]))
        # print("i is " + str(i) + " and parent2: " + str([j.number for j in parent2[i]]))
        chrom_mid_len_valid_no_depot = int((len(parent1[i]) - 1) / 2)
        end_ind_in_range = len(parent1[i]) - 1

        if i == 0:
            # we exclude depots at the start and end of the gene responsible for route
            # Thus, len(parent1[0])-2 means that we get index valid in the range of array and exclude a depot at the end of it
            chrom_mid_len_valid_no_depot = int((len(parent1[i]) - 2) / 2)
            end_ind_in_range = len(parent1[i]) - 2

        rand_ind1 = randint(1, chrom_mid_len_valid_no_depot)
        rand_ind2 = randint(chrom_mid_len_valid_no_depot+1, end_ind_in_range)

        # print("chrom_mid_len_valid_no_depot: " + str(chrom_mid_len_valid_no_depot))
        # print("end_ind_in_range: " + str(end_ind_in_range))
        # print("rand_ind1: " + str(rand_ind1))
        # print("rand_ind2:" + str(rand_ind2))

        temp1 = [j for j in range(len(parent1[i])) if j <= end_ind_in_range]
        temp2 = [j for j in range(len(parent2[i])) if j <= end_ind_in_range]

        range1 = [parent1[i][j] for j in range(len(parent1[i])) if rand_ind1 <= j <= rand_ind2]
        range2 = [parent2[i][j] for j in range(len(parent2[i])) if rand_ind1 <= j <= rand_ind2]
        # print("Range1: " + str([j.number for j in range1]))
        # print("Range2: " + str([j.number for j in range2]))

        queue1_missed_index = Queue(len(parent1[i]))
        queue2_missed_index = Queue(len(parent2[i]))

        for j in range(end_ind_in_range+1):
            parent1_elem = parent1[i][j]
            parent2_elem = parent2[i][j]

            if j < rand_ind1 or j > rand_ind2:
                if parent2_elem not in range1:
                    temp2[j] = parent1_elem
                else:
                    temp2[j] = 0
                    queue2_missed_index.put(j)

                if parent1_elem not in range2:
                    temp1[j] = parent1_elem
                else:
                    temp1[j] = 0
                    queue1_missed_index.put(j)

            if rand_ind1 <= j <= rand_ind2:
                temp1[j] = parent2_elem
                temp2[j] = parent1_elem
                if not queue1_missed_index.empty() and parent1_elem not in range2:
                    temp1[queue1_missed_index.get()] = parent1_elem
                if not queue2_missed_index.empty() and parent2_elem not in range1:
                    temp2[queue2_missed_index.get()] = parent2_elem
        if i == 0:
            temp1.append(temp1[0])
            temp2.append(temp2[0])

        child1.append(temp1)
        child2.append(temp2)

    return [child1, child2]


