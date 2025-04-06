from collections import defaultdict
from string import ascii_lowercase


def count_words(sentence: str) -> dict[str, int]:
    result = defaultdict(int)
    letters = {*ascii_lowercase, "'"}
    for word in sentence.lower().split():
        result["".join(letter for letter in word if letter in letters)] += 1

    return dict(result)


print(count_words("oh what a day what a lovely day"))
print(count_words("don't stop believing"))

print(count_words("The Queen will address the House of Commons today"))

print(count_words("Oh what a day, what a lovely day!"))
