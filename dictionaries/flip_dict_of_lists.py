# from collections import defaultdict
from collections import OrderedDict
from typing import Callable


def lowercase(string: str) -> str:
    return string.lower()


def flip_dict_of_lists(
    record: dict | OrderedDict,
    dict_type: Callable = dict,
    key_func: Callable[[str], str] = lambda k: k,
) -> dict | OrderedDict:
    flipped_record: dict = {}
    for key, values in record.items():
        for value in values:
            flipped_record.setdefault(key_func(value), []).append(key)

    return dict_type(flipped_record)


# def flip_dict_of_lists(
#     record: dict | OrderedDict,
#     dict_type: Callable = dict,
#     key_func: Callable[[str], str] = lambda k: k,
# ) -> dict | OrderedDict:
#     flipped_dict: defaultdict = defaultdict(list)
#     for key, values in record.items():
#         for value in values:
#             flipped_dict[key_func(value)].append(key)

#     return dict_type(flipped_dict)


d = {"a": [1, 2], "b": [3, 1], "c": [2]}
print(flip_dict_of_lists(d))
# {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}

toppings = OrderedDict(
    {"Trey": ["anchovies", "olives"], "Guido": ["olives", "pineapple"]}
)
print(flip_dict_of_lists(toppings, dict_type=OrderedDict))
# OrderedDict({'anchovies': ['Trey'], 'olives': ['Trey', 'Guido'], 'pineapple': ['Guido']})

toppings_2 = {"Trey": ["anchovies", "olives"], "Guido": ["Olives", "Pineapple"]}
print(flip_dict_of_lists(toppings_2, key_func=lowercase))
# {'anchovies': ['Trey'], 'olives': ['Trey', 'Guido'], 'pineapple': ['Guido']}
