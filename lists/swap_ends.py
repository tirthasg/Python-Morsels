def swap_ends(sequence, *, allow_empty=False):
    if not sequence:
        if allow_empty:
            return
        raise ValueError("Empty sequence not allowed without allow_empty=True")

    sequence[0], sequence[-1] = sequence[-1], sequence[0]


numbers = [2, 1, 3, 4, 7]
swap_ends(numbers)
print(numbers)

print(swap_ends([1]) is None)

numbers = []
swap_ends(numbers, allow_empty=True)
swap_ends(numbers)
