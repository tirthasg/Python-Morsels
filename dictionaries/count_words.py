from collections import defaultdict
from string import ascii_lowercase


def count_words(sentence: str) -> dict[str, int]:
    result = defaultdict(int)
    letters = {*ascii_lowercase, "'"}
    for word in sentence.lower().split():
        result["".join(letter for letter in word if letter in letters)] += 1

    return dict(result)


print(count_words("oh what a day what a lovely day"))
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
print(count_words("don't stop believing"))
# {"don't": 1, 'stop': 1, 'believing': 1}
print(count_words("The Queen will address the House of Commons today"))
# {"the": 2, "queen": 1, "will": 1, "address": 1, "house": 1, "of": 1, "commons": 1, "today": 1,}
print(count_words("Oh what a day, what a lovely day!"))
# {"oh": 1, "what": 2, "a": 2, "day": 2, "lovely": 1}
