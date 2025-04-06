def flip_dict(record, *, error_on_duplicates=False):
    if error_on_duplicates and len(record.values()) != len(set(record.values())):
        raise ValueError("Dictionary has duplicate values")

    return {old_value: old_key for old_key, old_value in record.items()}
    # return {
    #     old_value: old_key
    #     for old_key, old_value in record.items()
    # }


# def flip_dict(old_dict):
#     return dict(zip(old_dict.values(), old_dict.keys()))


print(flip_dict({"Python": "2015-09-15", "Java": "2015-09-14", "C": "2015-09-13"}))
print(flip_dict({"Python": "2015-09-15", "Java": "2015-09-14", "C": "2015-09-15"}))

pairs = {"Garnet": "Amethyst", "Steven": "Rose", "Pearl": "Rose"}
print(flip_dict(pairs))
print(flip_dict(pairs, error_on_duplicates=True))
