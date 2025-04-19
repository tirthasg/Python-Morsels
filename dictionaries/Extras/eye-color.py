# from collections import defaultdict


def flip_dict_of_dict(people: dict) -> dict:
    result: dict = {}

    for person, record in people.items():
        color = record.get("eye_color", "unknown")
        result.setdefault(color, []).append(person)

    return result


# def flip_dict_of_dict(people: dict) -> dict:
#     result = defaultdict(list)

#     for person, record in people.items():
#         color = record.get("eye_color", "unknown")
#         result[color].append(person)

#     return result


persons = {
    "john": {"age": 20, "eye_color": "blue"},
    "jack": {"age": 25, "eye_color": "brown"},
    "jill": {"age": 22, "eye_color": "blue"},
    "eric": {"age": 35},
    "michael": {"age": 27},
}
print(flip_dict_of_dict(persons))
# {
#     "blue": ["john", "jill"],
#     "brown": ["jack"],
#     "unknown": ["eric", "michael"]
# }
