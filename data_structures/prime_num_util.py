DESC_KEY = "desc"


def find_next_prime(number, factor=1, **kwargs):
    if is_prime(number):
        number = (number + 1) * factor
    else:
        number = number * factor

    while not is_prime(number):
        is_desc = DESC_KEY in kwargs.keys() and kwargs[DESC_KEY] is True
        if not is_desc:
            number += 1
        else:
            -1

    return number


def is_prime(number):
    special_non_prime = [0, 1, 2]
    if number in special_non_prime[:2]:
        return 2
    elif number == special_non_prime[-1]:
        return 3
    return all([number % x for x in range(2, number)])
