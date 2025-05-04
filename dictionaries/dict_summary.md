Dictionary:

A dictionary in python is a mutable mapping from unique, hashable keys to arbitrary values.
Two hashable objects are considered distinct, if they don't compare equal using == operator.
In Python 3.7+, dictionaries are ordered based on the order of insertion of (key, value) pairs.

Creating a dictionary:

{
    key1: value1,
    key2: value2,
    key3: value3,
    ...
} -> A dictionary literal

dict(**kwargs) -> Creates a dictionary from a possibly empty set of valid keyword arguments. The keys must be identifiers, and the keys of the created dictionary will be strings of these identifiers. If duplicate keys are provided in the constructor, the last value provided will be the value for that key. 

dict(iterable, **kwargs) -> Creates a dictionary from the optional positional argument, iterable, which consists of iterables of (key, value) pairs, and possibly empty set of valid keyword arguments. If keyword arguments are provided, they are added to the dictionary created from the iterable. The usual rules for keyword arguments, and duplicate keys are applied.

dict(mapping, **kwargs) -> Creates a dictionary from the optional position argument, mapping, and possibly empty set of valid keyword arguments. If keyword arguments are provided, they are added to the dictionary created from the mapping. The usual rules for keyword arguments, and duplicate keys are applied.s

dict.fromkeys(iterable, value=None) -> Creates a dictionary from the alternative constructor implemented as a class method of the dict class. It takes an iterable of hashable keys and assigns the same value to each key. While the iterable may contain duplicate keys, the resulting dictionary will only contain unique keys. If no value is provided, the default value assigned to each key will be None.

Note: All the values in the dictionary refer to the same single instance. Therefore, doesn't make sense for it to be a mutable object. To get distict values, use dict comprehensions instead.

{
    key_expression: value_expression 
    for item in iterable if condition
} -> A dictionary comprehenion

{
    key_expression: value_expression
    if condition 
    else alternative_value_expression 
    for item in iterable
} -> A dictionary comprehenion with condition to include the value_expression or the alternative_value_expression

{
    key_expression: value_expression 
    for item in iterable 
    if condition
} -> A dictionary comprehension with condition to include the (key_expression, value_expression) pair

Note:
Usual rules for duplicate keys applies.

Tip: 
Replace Dictionary comprehenion of the form: {key: value for key, value in iterable} to dict(iterable).

Operations, and dictionary methods:

key in d -> Returns True if the key exists in dictionary d, otherwise False.
key not in d -> Returns True if the key does not exist in dictionary d, otherwise False.

d[key] -> Returns the value associated with key. Raises a KeyError if the key is not found.
d[key] = value -> Inserts or updates the key-value pair for key.

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



https://www.youtube.com/@CMU1141111611/playlists

https://www.youtube.com/watch?v=vH7ZgoXSp44&list=PLy-82AVP8uEB8UipSJGUIKrA19iONeW04&index=1

https://www.youtube.com/watch?v=xjl8NG28UXM&list=PL4YhK0pT0ZhXteJ2OTzg4vgySjxTU_QUs&index=1

https://youtube.com/playlist?list=PL4YhK0pT0ZhXteJ2OTzg4vgySjxTU_QUs&si=fVMKXlXqcozU8ujg

https://www.youtube.com/@vvinoducsd/playlists

https://www.youtube.com/@neubig/playlists

https://www.youtube.com/playlist?list=PLqC25OT8ZpD3WxQ0FwWMGPS_BcWdcKyZy
