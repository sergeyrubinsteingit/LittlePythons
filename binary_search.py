import math


def binary_search(bn_search_array_, fnd_idx_of_):
    ##########################################################################################################
    # This part sorts an array in ascending order, because this algorithm requires this.
    for recurs_ in range(0, bn_search_array_.__len__()):
        for ix_ in range(bn_search_array_.__len__() - 1):
            if bn_search_array_[ix_] > bn_search_array_[ix_ + 1]:
                bn_search_array_[ix_], bn_search_array_[ix_ + 1] = bn_search_array_[ix_ + 1], bn_search_array_[ix_]
    print(f'The A-Z sorted array: {bn_search_array_}')
    ##########################################################################################################
    # This part commits binary search in array.
    idx_first: int = 0
    idx_last: int = bn_search_array_.__len__() - 1
    idx_middle: int = math.floor((idx_first + idx_last) / 2)

    while (bn_search_array_[idx_middle] != fnd_idx_of_ and idx_first <= idx_last):
        if bn_search_array_[idx_middle] > fnd_idx_of_:
            idx_last = idx_middle - 1
        else:
            idx_first = idx_middle + 1
        idx_middle = math.floor((idx_first + idx_last) / 2)
    # return bn_search_array_[idx_middle] == fnd_idx_of and idx_middle or -1
    print(bn_search_array_[idx_middle] == fnd_idx_of and
          f'After sorting in ascending order '
          f'the index of {fnd_idx_of} is {idx_middle}'
          or r'No such element in array.')


bn_srch_array = [112, 45, 2, 5, 7, 8, 12, 15, 0, 22, 54]
fnd_idx_of: int = 12

if __name__ == '__main__':
    binary_search(bn_srch_array, fnd_idx_of)
