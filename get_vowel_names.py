def get_vowel_names(names: list[str]):
    return [name for name in names if name.lower().startswith(tuple("aeiou"))]


names = ["Alice", "Bob", "Christy", "Jules"]
print(get_vowel_names(names))

names = ["Scott", "Arthur", "Jan", "Elizabeth"]
print(get_vowel_names(names))
