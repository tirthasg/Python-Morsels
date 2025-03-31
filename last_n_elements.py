def last_n_elements(sequence, n, *, reverse=False):
    if n <= 0:
        return []

    if reverse:
        return sequence[-1 : -(n + 1) : -1]
        # return items[: -(n + 1): -1]

    return sequence[-n:]


fruits = ["apples", "grapes", "peaches", "apricots", "bananas"]
print(last_n_elements(fruits, 3))
print(last_n_elements(fruits, 1))
print(last_n_elements(fruits, 3, reverse=False))
print(last_n_elements(fruits, 3, reverse=True))

numbers = [41, 25, 54, 15, 76, 68, 32, 38]
print(last_n_elements(numbers, 4))
print(last_n_elements(numbers, 0))
