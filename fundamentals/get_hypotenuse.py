from math import sqrt, hypot


# def get_hypotenuse(a, b):
#     return sqrt(a**2 + b**2)


def get_hypotenuse(a, b):
    return hypot(a, b)


print(get_hypotenuse(0, 0))
print(get_hypotenuse(3, 4))
print(get_hypotenuse(20, 21))
