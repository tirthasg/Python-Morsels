def characters(string, *, sort=False):
    if sort:
        return sorted(string.lower())
    
    return list(string.lower())


print(characters("hello"))
print(characters("Trey Hunner"))

print(characters("Trey Hunner", sort=True))
print(characters("hello", sort=True))
