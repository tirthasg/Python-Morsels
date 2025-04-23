from collections import defaultdict


def flip_dict(record: dict) -> dict:
    result: dict = {}

    for char, values in record.items():
        for value in values:
            result.setdefault(value, []).append(char)

    return result


def flip_dict2(record: dict) -> dict:
    result = defaultdict(list)

    for char, values in record.items():
        for value in values:
            result[value].append(char)

    return result


record = {"a": [1, 2], "b": [3, 1], "c": [2]}
print(flip_dict(record))
print(flip_dict2(record))
# {1: ["a", "b"], 2: ["a", "c"], 3: ["b"]}

# {
#     key1: value1,
#     key2: value2,
#     key3: value3,
#     ...
# }

# dict(**kwargs)
# dict(iterable, **kwargs)
# dict(mapping, **kwargs)

# dict.fromkeys(iterable, default=None)

# d[key]
# d[key] = value

# d.get(key, default=None)
# d.setdefault(key, default=None)

# del d[key]

# d.pop(key [, default])
# d.popitem()

# d.copy()
# from copy import deepcopy
# deepcopy(d)

# d.keys()
# d.values()
# d.items()

# list(d)
# len(d)

# d.clear()

# iter(d)
# reversed(d)
