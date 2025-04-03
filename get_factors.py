# def get_factors(num):
#     return [div for div in range(1, num + 1) if num % div == 0]


def get_factors(num: int) -> list[int]:
    if num <= 0:
        return []

    smaller_factors = []
    larger_factors = []
    div = 1
    while div * div <= num:
        if num % div == 0:
            smaller_factors.append(div)

            other_div = num // div
            if div != other_div:
                larger_factors.append(other_div)

        div += 1

    return smaller_factors + sorted(larger_factors)


print(get_factors(2))
print(get_factors(6))
print(get_factors(100))

print(get_factors(1))

print(get_factors(0))
print(get_factors(-2))
