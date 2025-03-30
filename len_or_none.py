def len_or_none(thing):
    if hasattr(thing, "__len__"):
        return len(thing)
    return None

    # try:
    #     return len(thing)
    # except TypeError:
    #     return None


print(len_or_none("hello"))
print(len_or_none(4))
print(len_or_none([]))
print(len_or_none(range(10)))
print(len_or_none(zip([1, 2], [3, 4])))
