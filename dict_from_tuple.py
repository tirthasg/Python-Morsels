# def dict_from_tuple(tuples):
#     return {tuple_[0]: tuple_[1:] for tuple_ in tuples}


def dict_from_tuple(tuples):
    return {key: tuple(values) for key, *values in tuples}


print(dict_from_tuple([(1, 2, 3, 4), (5, 6, 7, 8)]))
# {1: (2, 3, 4), 5: (6, 7, 8)}

print(dict_from_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
# {1: (2, 3), 4: (5, 6), 7: (8, 9)}
