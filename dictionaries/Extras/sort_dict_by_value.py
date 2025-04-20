def sort_dict_by_value(composers: dict) -> dict:
    return dict(sorted(composers.items(), key=lambda ele: ele[1]))


composers = {
    "Johann": 65,
    "Ludwig": 56,
    "Frederic": 39,
    "Wolfgang": 35,
}

print(sort_dict_by_value(composers))
