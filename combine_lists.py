def combine_lists(first, second):
    return list(first) + list(second)


first = [1, 2, 3]
second = [4, 5, 6]
print(combine_lists(first, second))

letter_tuple = ("a", "b", "c")
number_list = [2, 1, 3, 4, 7]
print(combine_lists(letter_tuple, number_list))
