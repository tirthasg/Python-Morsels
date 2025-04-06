# from collections import Counter, defaultdict
from collections import defaultdict
from string import punctuation


# def count_words(sentence: str) -> dict[str, int]:
#     frequency: dict[str, int] = {}
#     for word in sentence.split():
#         key = word.strip(punctuation).lower()
#         frequency[key] = frequency.setdefault(key, 0) + 1

#     return frequency


def count_words(sentence: str) -> dict[str, int]:
    frequency: dict[str, int] = defaultdict(int)
    for word in sentence.split():
        frequency[word.strip(punctuation).lower()] += 1

    return frequency


# def count_words(sentence: str) -> dict[str, int]:
#     return Counter([word.strip(punctuation).lower() for word in sentence.split()])


print(count_words("oh what a day what a lovely day"))
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
print(count_words("don't stop believing"))
# {"don't": 1, 'stop': 1, 'believing': 1}
print(count_words("The Queen will address the House of Commons today"))
# {"the": 2, "queen": 1, "will": 1, "address": 1, "house": 1, "of": 1, "commons": 1, "today": 1,}
print(count_words("Oh what a day, what a lovely day!"))
# {"oh": 1, "what": 2, "a": 2, "day": 2, "lovely": 1}
