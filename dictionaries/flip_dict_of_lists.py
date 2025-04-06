from collections import OrderedDict, defaultdict


def lowercase(string):
    return string.lower()


# def flip_dict_of_lists(record, dict_type=None, key_func=None):
#     result = {}
#     for key, value in record.items():
#         for item in value:
#             if key_func:
#                 item = key_func(item)

#             result.setdefault(item, [])
#             result[item].append(key)

#     if dict_type:
#         return dict_type(result)
#     return result


# def flip_dict_of_lists2(record, dict_type=dict, key_func=lambda k: k):
#     result = defaultdict(list)
#     for key, value in record.items():
#         for num in value:
#             num = key_func(num)
#             result[num].append(key)

#     return dict_type(result)


def flip_dict_of_lists(record, dict_type=dict, key_func=None):
    if not key_func:

        def key_func(key):
            return key

    result = defaultdict(list)

    for key, values in record.items():
        for value in values:
            result[key_func(value)].append(key)

    return dict_type(result)


d = {"a": [1, 2], "b": [3, 1], "c": [2]}
print(flip_dict_of_lists(d))

toppings = OrderedDict(
    {"Trey": ["anchovies", "olives"], "Guido": ["olives", "pineapple"]}
)
print(flip_dict_of_lists(toppings, dict_type=OrderedDict))

toppings = {"Trey": ["anchovies", "olives"], "Guido": ["Olives", "Pineapple"]}
print(flip_dict_of_lists(toppings, key_func=lowercase))
