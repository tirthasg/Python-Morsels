def dict_difference(d1: dict, d2: dict) -> dict:
    # return {key: d1[key] if key in d1 else d2[key] for key in d1.keys() ^ d2.keys()}
    return {key: d1.get(key) or d2.get(key) for key in d1.keys() ^ d2.keys()}


d1 = dict(zip("abcd", range(1, 5)))
d2 = dict(zip("abce", (10, 20, 30, 5)))
print(dict_difference(d1, d2))
