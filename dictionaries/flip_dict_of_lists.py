from collections import OrderedDict, defaultdict
from typing import Callable, Mapping


def lowercase(string):
    return string.lower()


def flip_dict_of_lists(
    record: Mapping[str, list[int | str]],
    dict_type: Mapping = dict,
    key_func: Callable[[str], str] = lambda k: k,
) -> Mapping[int | str, list[str]]:
    result = {}
    for key, values in record.items():
        for value in values:
            result.setdefault(key_func(value), []).append(key)

    return dict_type(result)


# def flip_dict_of_list(
#     record: Mapping[str, list[int | str]],
#     dict_type: Mapping = dict,
#     key_func: Callable[[str], str] = lambda k: k,
# ) -> Mapping[int | str, list[str]]:
#     pass


d = {"a": [1, 2], "b": [3, 1], "c": [2]}
print(flip_dict_of_lists(d))
# {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}

toppings = OrderedDict(
    {"Trey": ["anchovies", "olives"], "Guido": ["olives", "pineapple"]}
)
print(flip_dict_of_lists(toppings, dict_type=OrderedDict))
# OrderedDict({'anchovies': ['Trey'], 'olives': ['Trey', 'Guido'], 'pineapple': ['Guido']})

toppings = {"Trey": ["anchovies", "olives"], "Guido": ["Olives", "Pineapple"]}
print(flip_dict_of_lists(toppings, key_func=lowercase))
# {'anchovies': ['Trey'], 'olives': ['Trey', 'Guido'], 'pineapple': ['Guido']}
