from string import ascii_uppercase, digits


def convert_from10(num: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("In-valid value for base")

    if num == 0:
        return str(num)

    result = []
    while num != 0:
        digit = num % base
        result.append(digit)

        num = num // base

    result.reverse()
    encoding = digits + ascii_uppercase
    return "".join(encoding[digit] for digit in result)


print(convert_from10(10, 2))
print(convert_from10(15, 8))
print(convert_from10(210, 16))
