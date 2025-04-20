def common_keys(d1: dict, d2: dict) -> dict:
    return {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}


d1 = dict(zip("abcd", range(1, 5)))
d2 = dict(zip("bcyz", range(20, 60, 10)))

print(common_keys(d1, d2))
