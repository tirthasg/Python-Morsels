def split_in_half(sequence):
    mid = len(sequence) // 2
    return sequence[:mid], sequence[mid:]


print(split_in_half([1, 2, 3, 4]))
print(split_in_half([1, 2, 3, 4, 5]))
print(split_in_half([1, 2]))
print(split_in_half([]))
print(split_in_half([1]))

print(split_in_half("This is a string"))
print(split_in_half((1, 2, 3, 4, 5, 6)))
print(split_in_half(b"bytestring"))