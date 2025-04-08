The keys of a dictionary must be hashable objects.
However, the values can be any python object.
In Python 3.7+, dicts are guaranteed to be ordered in the insertion order of it's keys.

{
    key1: value1,
    key2: value2,
    key3: value3,
    ...
} -> Creating a dictionary using a dict literal

dict(**kwargs) -> Returns a dictionary initialized from keyword arguments.

dict(iterable, **kwargs) -> Creating a dictionary using the optional positional argument, iterable, and possibly empty set of "valid" keyword arguments. Each item of the iterable must be an iterable of exactly two elements. The first element of each item becomes a key in the new dictionary, and the second element is it's corresponding value. If a key occurs more than once, the last value for that key becomes the corresponding value in the new dictionary. 

dict(mapping, **kwargs) -> Creating a dictionary using the optional positional argument, mapping, and possibly empty set of "valid" keyword arguments. If a key occurs more than once, the last value for that key becomes the corresponding value in the new dictionary.

If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument. If a key being added is already present, the value from the keyword argument replaces the value from the positional argument.

-> Returns a dictionary initialized from the optional positional argument, and a possible empty set of keyword arguments.
The keyword argument only work for keys when they are valid python identifiers.

dict.fromkeys(iterable, value=None) -> Creating a dictionary from the classmethod, fromkeys(), where the keys are obtained from the iterable, and all of them share the same value (the same instance). The value if unspecified, defaults to None.

key in d -> Returns True if key in d. Else, False.
key not in d -> Returns True if key not in d. Else, True.

d[key] -> As an expression, returns the value corresponding to the key, if present. Else, KeyError exception.
d[key] = value -> Updates the value for the key with value, if present. Else, inserts the key with value set to value.

d.get(key, default=None) -> Returns the value for the key, if present. Else, returns the default value. The default value defaults to None when unspecified.

d.setdefault(key, default=None) -> If key in dictionary, return it's value. Else, insert key with value set to default, and return the default. The default defaults to None.

del d[key] -> If key is present, remove it. Else, KeyError exception.

d.pop(key [, default]) -> If key is present, remove it, and return it's value. Else, if default is specified, then return it. Otherwise, KeyError exception.

    1. key is present -> remove the key, and return d[key]
    2. key not present, and default specified -> return default
    3. key not present, and default is unspecified -> KeyError exception

d.popitem() -> If dictionary isn't empty, remove, and return a (key, value) pair in LIFO order. Else, KeyError exception.

d.keys() -> Returns a view of the dictionary's keys.
d.values() -> Returns a view of the dictionary's values.
d.items() -> Returns a view of the dictionary's items.

d.clear() -> Removes all items from the dictionary.

d.copy() -> Returns a shallow copy of the dictionary. Same as dict(d)
from copy import deepcopy
deepcopy(d)

list(d) -> Returns a list of all keys in the dictionary.
len(d) -> Returns the number of items in the dictionary.

iter(d) -> Returns a iterator over the keys of the dictionary. Shortcut for iter(d.keys())
reversed(d) -> Returns a reversed iterator over the keys of the dictionary. Shortcut for reversed(d.keys())

