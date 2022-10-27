class LinearSearch:

    def line_search(self, list_, el_):
        for idx_ in range(list_.__len__() - 1):
            if list_[idx_] == el_:
                print(f'Element {el_} is found in position {idx_}')
            # if list_[idx_] != el_ and idx_ == len(list_) - 2:
            #     print(f'Element {el_} is not found in the list.')
        if el_ not in list_:
            print(f'Element {el_} is not found in the list.')
        choose_mode()


# On user's choice stops or run the process again.
def choose_mode():
    the_mode_ = input('Type \'y\' to continue or any other key to stop.')
    if the_mode_ == 'y':
        set_conditions()
    else:
        return


# Setting a list to pass into function:
list_to_sort: list = [100, 33, 66, 22, 99, 66, 12, 77, 2, -3]
# An instance of the class needed for passing arguments into 'self' function:
cls_inst_ = LinearSearch()


# Gets user's input. Checks it for being an integer. If so, runs a search algo.
# Otherwise stops with warning.
def set_conditions():
    try:
        el_to_find = input('Enter a number:')
        int(el_to_find)
        cls_inst_.line_search(list_to_sort, int(el_to_find))
    except:
        print('Element must be integer.')
        choose_mode()


if __name__ == '__main__':
    set_conditions()
