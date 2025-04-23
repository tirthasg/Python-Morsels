def get_grouped_char_frequency(sentence: str):
    frequency = {}

    for char in sentence:
        value = char.strip()

        key = "punctuation"
        if value.islower():
            key = "lowercase"
        elif value.isupper():
            key = "uppercase"

        if value:
            frequency.setdefault(key, []).append(value)

    return {key: "".join(value) for key, value in frequency.items()}


sentence = "Hello, world! Meow. meow."
print(get_grouped_char_frequency(sentence))
