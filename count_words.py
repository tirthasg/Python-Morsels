from collections import defaultdict
from string import punctuation


# def count_words(string):
#     record = {}
#     for word in string.lower().split():
#         clean_word = word.strip(punctuation)
#         record.setdefault(clean_word, 0)
#         record[clean_word] += 1

#     return record


def count_words(sentence):
    result = defaultdict(int)
    for word in sentence.lower().split():
        result[word.strip(punctuation)] += 1

    return dict(result)


print(count_words("oh what a day what a lovely day"))
print(count_words("don't stop believing"))

print(count_words("The Queen will address the House of Commons today"))

print(count_words("Oh what a day, what a lovely day!"))
