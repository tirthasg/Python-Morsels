from collections import defaultdict
from string import ascii_lowercase


def char_frequency(sentence: str) -> dict:
    result = defaultdict(int)

    for char in sentence:
        key = char.strip().lower()
        if key:
            result[key] += 1

    return result


def char_frequency2(sentence: str) -> dict:
    result: dict = {}

    for char in ascii_lowercase:
        result[char] = 0

    for char in sentence:
        key = char.strip().lower()
        if key and key in ascii_lowercase:
            result[key] += 1

    for char in ascii_lowercase:
        if result[char] == 0:
            del result[char]

    return result


sentence = "Hello, world! Meow, meow."
print(char_frequency(sentence))

print(char_frequency2(sentence))

# pass vs ...
