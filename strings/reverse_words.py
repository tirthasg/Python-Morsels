def reverse_words(sentence):
    return " ".join(reversed(sentence.split()))


print(reverse_words("words some are these"))
print(reverse_words("who is this"))
