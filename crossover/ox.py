# a.k.a. Order Crossover
#  two points are selected randomly in the parents. Then the genes between these two points from
#  parent-one are directly transferred to child-one and from parent-two to child-two.
#  After that, for child-one we start from the second point of parent-two, and we transfer
#  to child-one what is not already transferred to child-one. We do the same thing for child-two with parent-one.
from queue import Queue
from random import randint


def order_crossover(parent1, parent2):
    child1 = []
    child2 = []

    for i in range(len(parent1)):
        print([vertex.number for vertex in parent1[i]])
        print([vertex.number for vertex in parent2[i]])

        chrom_mid_len_valid_no_depot = int((len(parent1[i]) - 1) / 2)
        end_ind_in_range = len(parent1[i]) - 1

        if i == 0:
            # we exclude depots at the start and end of the gene responsible for route
            # Thus, len(parent1[0])-2 means that we get index valid in the range of array and exclude a depot at the end of it
            chrom_mid_len_valid_no_depot = int((len(parent1[i]) - 2) / 2)
            end_ind_in_range = len(parent1[i]) - 2

        print("chrom_mid_len_valid_no_depot : ", chrom_mid_len_valid_no_depot)
        print("end_ind_in_range : ", end_ind_in_range)
        rand_int1 = randint(1, chrom_mid_len_valid_no_depot)
        rand_int2 = randint(chrom_mid_len_valid_no_depot, end_ind_in_range)
        print("rand_int1 : ", rand_int1)
        print("rand_int2 : ", rand_int2)

        range1 = [parent1[i][j] for j in range(len(parent1[i])) if (rand_int1 <= j <= rand_int2)]
        range2 = [parent2[i][j] for j in range(len(parent2[i])) if (rand_int1 <= j <= rand_int2)]

        print("Range1: " + str([k.number for k in range1]))
        print("Range2: " + str([k.number for k in range2]))

        # copy chromosomes
        temp1 = [parent1[i][j] for j in range(len(parent1[i])) if j <= end_ind_in_range]
        temp2 = [parent2[i][j] for j in range(len(parent2[i])) if j <= end_ind_in_range]
        print("Copied temp1: " + str([j.number for j in temp1]))
        print("Copied temp2: " + str([j.number for j in temp2]))

        par_length = len(parent1[i])
        if i == 0:
            par_length = len(parent1[i]) - 1

        queue1 = Queue(par_length - range1.__len__())
        queue2 = Queue(par_length - range2.__len__())

        for j in range(rand_int2 + 1, par_length):
            if temp1[j] not in range2:
                queue1.put(temp1[j])
            if temp2[j] not in range1:
                queue2.put(temp2[j])

        for j in range(0, rand_int2+1):
            if temp1[j] not in range2:
                queue1.put(temp1[j])
            if temp2[j] not in range1:
                queue2.put(temp2[j])

        for j in range(rand_int2 + 1, par_length):
            if not queue2.empty():
                temp1[j] = queue2.get()
                print("Queue2 item: " + str(temp1[j].number))
            if not queue1.empty():
                temp2[j] = queue1.get()
                print("Queue1 item: " + str(temp2[j].number))

        for j in range(0, rand_int2+1):
            if not queue2.empty():
                temp1[j] = queue2.get()
                print("Queue2 item: " + str(temp1[j].number))
            if not queue1.empty():
                temp2[j] = queue1.get()
                print("Queue1 item: " + str(temp2[j].number))

        temp1.append(temp1[0])
        temp2.append(temp2[0])

        print("Temp1: " + str([l.number for l in temp1]))
        print("Temp2: " + str([l.number for l in temp2]))

        # pass genes to children
        child1.append(temp1)
        child2.append(temp2)

    return [child1, child2]
