def dict_intersection1(d1: dict, d2: dict) -> dict:
    return {key: value for key, value in d1.items() & d2.items()}


def dict_intersection2(d1: dict, d2: dict) -> dict:
    return {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 2, "c": 30, "d": 4}
# {"b": 2}
print(dict_intersection1(d1, d2))
# {"b": (2, 2), "c": (3, 30)}
print(dict_intersection2(d1, d2))
