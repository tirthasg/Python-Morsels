from math import ceil


def dog_and_bun_packs_needed(guests):
    buns = ceil(guests / 8)
    hot_dogs = ceil(guests / 10)
    return buns, hot_dogs


print(dog_and_bun_packs_needed(7))
print(dog_and_bun_packs_needed(10))
print(dog_and_bun_packs_needed(14))
print(dog_and_bun_packs_needed(20))
print(dog_and_bun_packs_needed(21))
print(dog_and_bun_packs_needed(28))
