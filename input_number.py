def input_number(prompt="Enter a number: "):
    while True:
        number = input(prompt)
        try:
            return float(number)
        except ValueError:
            print(f"'{number}' is not a valid number")


print(input_number())
