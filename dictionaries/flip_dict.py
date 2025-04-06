# def flip_dict(
#     record: dict[str, str], *, error_on_duplicates: bool = False
# ) -> dict[str, str]:
#     if error_on_duplicates and len(set(record.values())) != len(record.values()):
#         raise ValueError("Dictionary has duplicate values")

#     return dict(zip(record.values(), record.keys()))


def flip_dict(
    record: dict[str, str], *, error_on_duplicates: bool = False
) -> dict[str, str]:
    if error_on_duplicates and len(set(record.values())) != len(record.values()):
        raise ValueError("Dictionary has duplicate values")

    return {value: key for key, value in record.items()}


print(flip_dict({"Python": "2015-09-15", "Java": "2015-09-14", "C": "2015-09-13"}))
# {'2015-09-15': 'Python', '2015-09-14': 'Java', '2015-09-13': 'C'}
print(flip_dict({"Python": "2015-09-15", "Java": "2015-09-14", "C": "2015-09-15"}))
# {'2015-09-15': 'C', '2015-09-14': 'Java'}

pairs = {"Garnet": "Amethyst", "Steven": "Rose", "Pearl": "Rose"}
print(flip_dict(pairs))
# {"Amethyst": "Garnet", "Rose": "Pearl"}
print(flip_dict(pairs, error_on_duplicates=True))
#  ValueError Exception
