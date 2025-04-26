Dictionary:

Mutable mapping from unique, hashable keys to arbitrary python object values. Two hashable objects are considered unique, if they don't compare equal using ==. Dictionaries are ordered in order of insertion of (key, value) pairs in Python 3.7+.

{
    key1: value1,
    key2: value2,
    key3: value3,
    ...
} -> Dictionary literal

dict(**kwargs) -> Dictionary created from a possibly empty set of "valid" keyword arguments. For the keys to be valid, they must be identifiers. The keys of the dictionary will be strings of these identifiers. In case of duplicate keys in the constructor, the last value for that key becomes the corresponding value in the dictionary. 

dict(iterable, **kwargs) -> Dictionary created from an optional positional argument, iterable, whose values are themselves iterables of two values. The first value must be hashable, and represents the key, and the second value is any arbitrary python object, and represents the value corresponding to the key. The usual rules apply for the keyword arguments. If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument. In case of duplicate keys in the constructor, the last value for that key becomes the corresponding value in the dictionary. 

dict(mapping, **kwargs) -> Dictionary created from an optional positional argument, mapping, and possibly empty set of valid keyword arguments. The usual rules apply for the keyword arguments. If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument. In case of duplicate keys in the constructor, the last value for that key becomes the corresponding value in the dictionary. 

dict.fromkeys(iterable, value=None) -> Alternative constructor, implemented as a classmethod of dict. Dictionary created from an iterable, with usual rules applied. All of the values of the key refer to the same single instance. Therefore, doesn't make sense for it to be a mutable object. To get distict values, use dict comprehensions instead. Value defaults to None.

{
    key_expression: value_expression 
    for item in iterable if condition
} -> Simple Dictionary comprehenion

{
    key_expression: value_expression
    if condition 
    else alternative_value_expression 
    for item in iterable
} -> Dictionary comprehenion with condition on value_expression

{
    key_expression: value_expression 
    for item in iterable 
    if condition
} -> Dictionary comprehension with condition on the pair key_expression: value_expression

Tip: 
Replace Dictionary comprehenion of the form: {key: value for key, value in iterable} to dict(iterable).

key in d -> True if key in d, else False.
key not in d -> True if key not in d, else False.

d[key] -> Returns value corresponding to key, if key is present in d. Else, KeyError.
d[key] = value -> Inserts key with value, if key is not present in d. Else, updates the value for key.

d.get(key, default=None) -> Returns value corresponding to key, if key is present in d. Else, returns default. The default defaults to None. The key is not inserted with default value, if it's not present in d. Note that, default isn't a keyword argument.

d.setdefault(key, default=None) -> Returns value corresponding to key, if key is present in d. Else, insert the key with default value, and return default. The default defaults to None. Note that, default isn't a keyword argument.

del d[key] -> Removes the key, and its value from the dictionary, if present. Else, KeyError.

d.pop(key [, default]) -> Removes the key from the dictionary, and returns it's value, if present. Else if, default is provided, returns the default value. Else, KeyError. Note that, default isn't a keyword argument.

d.popitem() -> Deletes, and returns the (key, value) pair as a tuple in LIFO, if d is non-empty. Else, KeyError.

d.clear() -> Empties the dictionary in-place.

d.copy() -> Returns a shallow-copy of d.
from copy import deepcopy
deepcopy(d) -> Returns a deep-copy of d.

{**d}, dict(d), {key: value for key, value in d.items()} -> All are shallow-copies of d.

len(d) -> Returns the number of items in the d.

list(d) -> Returns the list of keus in d.

iter(d) -> Returns an iterator over the keys in d. Shortcut for iter(d.keys()).
reversed(d) -> Returns a reverse iterator over the keys in d. Shortcut for reversed(d.keys()).

d.keys() -> Returns a view of the keys of d. The keys view behave as a (frozen) set because, the keys are unique, and hashable.
d.values() -> Returns a view of the values of d. The values view never behave as a set.
d.items() -> Returns a view of the items of d. The items view may behave as a (frozen) set, depending on whether the values are hashable. They need not be unique. The key's uniqueness is enough to make a (key, value) pair unique.

Note:
Views are read-only iterables. Can't update the dictionary using the views. However, they reflect the changes in the dictionary.

An equality comparison between one dict.values() view and another will always return False. This also applies when comparing dict.values() to itself.

d1.keys(), and d2.keys() are ordered, but d1.keys() | d2.keys() is a set, and isn't ordered.

Common set operations:
Union: |
Intersection: &
Difference: -
Symmetric difference: ^

d.update(d2) -> For every key in d2, if key is not in d, then insert (key, value) pair in d. Else, update the value.

d.update(iterable) -> Usual rules of iterable applies. And, usual rules of insert/update applies.

d.update(**kwargs) -> Usual rules of insert/update applies. And, usual rules of keyword argument applies.

d | d2 -> Create a new dictionary with the merged keys and values of d and d2, which must both be dictionaries. The values of d2 take priority when d and d2 share keys.

d |= d2 -> Update the dictionary d with keys and values from d2, which may be either a mapping or an iterable of (key, value) pairs. Usual rules of iterable applies. The values of d2 take priority when d and d2 share keys.

Dictionaries compare equal if and only if they have the same (key, value) pairs (regardless of ordering). They are same if they compare equal using ==. Order comparisons (<, <=, >=, >) raise TypeError.

**d -> Double-star notation to unpack the dictionary.
{**d1, **d2, **d3} -> Insertion order preserved while unpacking, but the last update wins.
{**d, 'c': 100, 'd': 200} -> Again, insertion order preserved while unpacking, but the last update wins.