from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    truthy_args = [arg for arg in args if arg]
    if not truthy_args:
        return set()

    result = truthy_args[0]
    for arg in truthy_args:
        result &= set(arg)

    return result


inputs = (None,)
# inputs = ([1, 2, 3, 3, 2, 1],)
print(intersection(*inputs))
