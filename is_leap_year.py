def is_leap_year(year):
    if year % 4 != 0:
        return False

    if year % 100 == 0 and year % 400 != 0:
        return False

    return True

    # return (
    #     year % 4 == 0
    #     and (
    #         year % 100 != 0
    #         or year % 400 == 0
    #     )
    # )


print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2012))
print(is_leap_year(2018))
