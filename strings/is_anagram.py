from string import whitespace, punctuation


def clean_string(string: str) -> str:
    black_list = set(whitespace + punctuation)
    return "".join([char.lower() for char in string if char not in black_list])


def is_anagram(s1: str, s2: str) -> bool:
    s1 = clean_string(s1)
    s2 = clean_string(s2)

    return sorted(s1) == sorted(s2)


print(is_anagram("coins kept", "in pockets"))
print(is_anagram("a diet", "I'd eat"))
