from collections import Counter, defaultdict


def count_chars_using_get(sentence):
    frequency = {}
    for char in sentence:
        key = char.strip().lower()
        if key:
            frequency[key] = frequency.get(key, 0) + 1

    return frequency


def count_chars_using_setdefault(sentence):
    frequency = {}
    for char in sentence:
        key = char.strip().lower()
        if key:
            frequency[key] = frequency.setdefault(key, 0) + 1

    return frequency


def count_chars_using_defaultdict(sentence):
    frequency = defaultdict(int)
    for char in sentence:
        key = char.strip().lower()
        if key:
            frequency[key] += 1

    return frequency


def count_chars_using_counter(sentence):
    return Counter([char.strip().lower() for char in sentence if char.strip()])


sentence = "Hello, world! Meow, meow."

d1 = count_chars_using_get(sentence)
d2 = count_chars_using_setdefault(sentence)
d3 = count_chars_using_counter(sentence)
d4 = count_chars_using_defaultdict(sentence)

print(d1)
print(d2)
print(d3)
print(d4)

print(d1 == d2 == d3 == d4)


def flip_dict_using_get(record):
    result = {}
    for key, values in record.items():
        for value in values:
            new_key = value
            new_item = key

            new_value = result.get(new_key, [])
            new_value.append(new_item)
            result[new_key] = new_value

    return result


def flip_dict_using_setdefault(record):
    result = {}
    for key, values in record.items():
        for value in values:
            new_key = value
            new_value = key

            result.setdefault(new_key, []).append(new_value)

    return result


def flip_dict_using_defaultdict(record):
    result = defaultdict(list)
    for key, values in record.items():
        for value in values:
            new_key = value
            new_value = key

            result[new_key].append(new_value)

    return result


record = {"a": [1, 2], "b": [3, 1], "c": [2]}

d1 = flip_dict_using_get(record)
d2 = flip_dict_using_setdefault(record)
d3 = flip_dict_using_defaultdict(record)

print(d1)
print(d2)
print(d3)

print(d1 == d2 == d3)
