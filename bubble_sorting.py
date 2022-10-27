class BubbleSort:
    list_to_sort = [100, 33, 66, 22, 99, 77, 2, -3]
    print('Before: ' + str(list_to_sort) + '\n')

    for recurs_ in range(0, list_to_sort.__len__()):
        for ix_ in range(list_to_sort.__len__() - 1):
            if list_to_sort[ix_] > list_to_sort[ix_ + 1]:
                list_to_sort[ix_], list_to_sort[ix_ + 1] = list_to_sort[ix_ + 1], list_to_sort[ix_]

    print('After: ' + str(list_to_sort))
