def words_containing(words, letter):
    return [word for word in words if letter.lower() in word.lower()]


zen_line_2 = ["Explicit", "is", "better", "than", "implicit"]
print(words_containing(zen_line_2, "p"))
print(words_containing(zen_line_2, "i"))
print(words_containing(zen_line_2, "x"))

print(words_containing(zen_line_2, "e"))
print(words_containing(zen_line_2, "X"))
