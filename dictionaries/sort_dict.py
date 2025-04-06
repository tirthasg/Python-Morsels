def sort_dict(record: dict) -> dict:
    return dict(sorted(record.items()))


original_dict = {1: "N", 6: "!", 4: "T", 3: "A", 2: "E", 5: "O"}
print(sort_dict(original_dict))
# {1: 'N', 2: 'E', 3: 'A', 4: 'T', 5: 'O', 6: '!'}

color_counts = {"red": 3, "blue": 4, "green": 5, "yellow": 7}
print(sort_dict(color_counts))
# {'blue': 4, 'green': 5, 'red': 3, 'yellow': 7}
