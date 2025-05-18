from collections import Counter, OrderedDict, defaultdict
from string import punctuation


def flip_dict(record, error_on_duplicates=False):
    if error_on_duplicates and len(set(record.values())) < len(record.values()):
        raise ValueError("Dictionary has duplicate values")

    return {value: key for key, value in record.items()}


record = {"Python": "2015-09-15", "Java": "2015-09-14", "C": "2015-09-13"}
expected = {"2015-09-15": "Python", "2015-09-14": "Java", "2015-09-13": "C"}
actual = flip_dict(record)
print(actual)
print(expected == actual)

pairs = {"Garnet": "Amethyst", "Steven": "Rose", "Pearl": "Rose"}
expected = {"Amethyst": "Garnet", "Rose": "Pearl"}
actual = flip_dict(pairs)
print(actual)
print(expected == actual)

try:
    flip_dict(pairs, error_on_duplicates=True)
except ValueError:
    print("ValueError Caught!")


def flip_dict_of_lists(record, dict_type=dict, key_func=lambda ele: ele):
    result = defaultdict(list)
    for key, values in record.items():
        for value in values:
            normalized_value = key_func(value)
            result[normalized_value].append(key)

    return dict_type(result)


d = {"a": [1, 2], "b": [3, 1], "c": [2]}
expected = {1: ["a", "b"], 2: ["a", "c"], 3: ["b"]}
actual = flip_dict_of_lists(d)
print(actual)
print(expected == actual)

toppings = OrderedDict(
    {"Trey": ["anchovies", "olives"], "Guido": ["olives", "pineapple"]}
)
expected = OrderedDict(
    {"anchovies": ["Trey"], "olives": ["Trey", "Guido"], "pineapple": ["Guido"]}
)
actual = flip_dict_of_lists(toppings, dict_type=OrderedDict)
print(actual)
print(expected == actual)


def lowercase(string):
    return string.lower()


toppings = {"Trey": ["anchovies", "olives"], "Guido": ["Olives", "Pineapple"]}
expected = {"anchovies": ["Trey"], "olives": ["Trey", "Guido"], "pineapple": ["Guido"]}
actual = flip_dict_of_lists(toppings, key_func=lowercase)
print(actual)
print(expected == actual)


def count_words(sentence):
    words = (word.strip(punctuation).lower() for word in sentence.split())
    return Counter(words)


sentence = "oh what a day what a lovely day"
expected = {"oh": 1, "what": 2, "a": 2, "day": 2, "lovely": 1}
actual = count_words(sentence)
print(actual)
print(expected == actual)

sentence = "don't stop believing"
expected = {"don't": 1, "stop": 1, "believing": 1}
actual = count_words(sentence)
print(actual)
print(expected == actual)

sentence = "The Queen will address the House of Commons today"
expected = {
    "the": 2,
    "queen": 1,
    "will": 1,
    "address": 1,
    "house": 1,
    "of": 1,
    "commons": 1,
    "today": 1,
}
actual = count_words(sentence)
print(actual)
print(expected == actual)

sentence = "Oh what a day, what a lovely day!"
expected = {"oh": 1, "what": 2, "a": 2, "day": 2, "lovely": 1}
actual = count_words(sentence)
print(actual)
print(expected == actual)


def dict_from_tuple(tuples):
    return {tuple_[0]: tuple_[1:] for tuple_ in tuples}


tuples = [(1, 2, 3, 4), (5, 6, 7, 8)]
expected = {1: (2, 3, 4), 5: (6, 7, 8)}
actual = dict_from_tuple(tuples)
print(actual)
print(expected == actual)

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
expected = {1: (2, 3), 4: (5, 6), 7: (8, 9)}
actual = dict_from_tuple(tuples)
print(actual)
print(expected == actual)


def sort_dict(record):
    return dict(sorted(record.items()))


original_dict = {1: "N", 6: "!", 4: "T", 3: "A", 2: "E", 5: "O"}
expected = {1: "N", 2: "E", 3: "A", 4: "T", 5: "O", 6: "!"}
actual = sort_dict(original_dict)
print(actual)
print(expected == actual)

original_dict = {"red": 3, "blue": 4, "green": 5, "yellow": 7}
expected = {"blue": 4, "green": 5, "red": 3, "yellow": 7}
actual = sort_dict(original_dict)
print(actual)
print(expected == actual)


def get_shared_keys(dict1, dict2):
    return dict1.keys() & dict2.keys()


expired = {"c95": "20200315", "d45": "20200401", "b38": "20200415"}
used_recently = {"a56": 8, "b38": 1, "e77": 4, "d45": 3}
expected = ["d45", "b38"]
actual = get_shared_keys(expired, used_recently)
print(actual)
print(expected == actual)


def ordered_deduplication1(items):
    uniques = set()
    result = []
    for item in items:
        if item not in uniques:
            uniques.add(item)
            result.append(item)

    return result


def ordered_deduplication2(items):
    return list(dict.fromkeys(items).keys())


all_colors = ["blue", "purple", "green", "red", "green", "pink", "blue"]
print(ordered_deduplication1(all_colors))
print(ordered_deduplication2(all_colors))


# def helper(record, result):
#     if isinstance(record, int):
#         result.append(record)
#         return

#     for row in record:
#         helper(row, record)


# def flatten(record):
#     result = []
#     helper(record, result)
#     return result


# record = [[1, 2, 3], [4, 5, 6]]
# print(flatten(record))


def flatten_dict(record, *, sep="_"):
    result = {}
    for key, data in record.items():
        if not isinstance(data, dict):
            result[key] = data
            continue

        for skey, value in data.items():
            result[f"{key}{sep}{skey}"] = value

    return result


record = {"vowels": {"a": 1, "e": 4}, "consonants": {"z": 2, "v": 3}}
expected = {"vowels_a": 1, "vowels_e": 4, "consonants_z": 2, "consonants_v": 3}
actual = flatten_dict(record)
print(actual)
print(expected == actual)

record = {"A": {1: [], 2: ["z"]}, "B": {}}
expected = {"A / 1": [], "A / 2": ["z"]}
actual = flatten_dict(record, sep=" / ")
print(actual)
print(expected == actual)

record = {"vowels": {"a": 1, "e": 2}, "b": 4}
expected = {"vowels_a": 1, "vowels_e": 2, "b": 4}
actual = flatten_dict(record)
print(actual)
print(expected == actual)
