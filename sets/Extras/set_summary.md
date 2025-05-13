Set:

A set in python is an unordered collection of distinct, hashable objects.
Two objects are considered to be distinct, if they don't compare equal using == operator.

1. Creating a set:

{val1, val2, val3, ...} -> A set literal

set(iterable)

{ele_expression for ele in iterable}

2. Operations, and set methods:

ele in s
ele not in s

s.add(ele)

s.remove(ele)
s.discard(ele)
s.pop()
s.clear()

s.isdisjoint(other)

s.issubset(other)
s <= other
s < other (Equivalent to: s <= other and len(s) != len(other))

s.issuperset(other)
s >= other
s > other (Equivalent to: s >= other and len(s) != len(other))

s.union(*others)
s | other | ...

s.intersection(*others)
s | other | ...

s.difference(*others)
s - other - ...

s.symmetric_difference(other)
s ^ other

s.copy()
from copy import deepcopy
deepcopy(s)

