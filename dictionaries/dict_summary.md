Dictionary:

A dictionary in python is a mutable mapping from distinct, hashable keys to arbitrary values.
Two objects are considered to be distinct, if they don't compare equal using == operator.
In Python 3.6+, dictionaries are ordered based on the order of insertion of (key, value) pairs.

1. Creating a dictionary:

{
    key1: value1,
    key2: value2,
    key3: value3,
    ...
} -> A dictionary literal

dict(**kwargs) -> Creates a dictionary from a possibly empty set of valid keyword arguments. The keys must be identifiers, and the keys of the created dictionary will be strings of these identifiers. If duplicate keys are provided in the constructor, the last value provided will be the value for that key. 

dict(iterable, **kwargs) -> Creates a dictionary from the optional positional argument, iterable, which consists of iterables of (key, value) pairs, and using a possibly empty set of valid keyword arguments. If keyword arguments are provided, they are added to the dictionary created from the iterable. And, the usual rules for keyword arguments, and duplicate keys are applied.

dict(mapping, **kwargs) -> Creates a dictionary from the optional positional argument, mapping, and possibly empty set of valid keyword arguments. If keyword arguments are provided, they are added to the dictionary created from the mapping. The usual rules for keyword arguments, and duplicate keys are applied.

dict.fromkeys(iterable, value=None) -> Creates a dictionary from the alternative constructor implemented as a class method of the dict class. It takes an iterable of hashable keys and assigns the same value to each key. While the iterable may itself contain duplicate keys, the resulting dictionary will only contain unique keys. If no value is provided, the default value assigned to each key will be None.

Note:
All the values in the dictionary refer to the same single instance. Therefore, doesn't make sense for it to be a mutable object. To get distict values, use dict comprehensions instead.
default isn't a keyword argument.

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

2. Operations, and dictionary methods:

key in d -> Returns True if the key exists in dictionary d, otherwise False.
key not in d -> Returns True if the key does not exist in dictionary d, otherwise False.

d[key] -> Returns the value associated with key. Raises a KeyError if the key is not found.
d[key] = value -> Inserts or updates the key-value pair for key.

d.get(key, default=None) -> Returns the value for key if present, otherwise returns default (defaulting to None). The key is not inserted with the default value.

Note:
default isn't a keyword argument.

d.setdefault(key, default=None) -> Returns the value for key if present, otherwise inserts the key with the default (defaulting to None) value and returns the default.

Note:
default isn't a keyword argument.

del d[key] -> Deletes the key and its associated value. Raises a KeyError if the key is not found.

d.pop(key [, default]) -> Removes and returns the value associated with key. If the key is not found, it returns default if provided, otherwise raises a KeyError.

d.popitem() -> Removes and returns the last inserted (key, value) pair as a tuple (LIFO order). Raises a KeyError if the dictionary is empty.

d.clear() -> Removes all items from the dictionary.

d.copy() -> Returns a shallow copy of the dictionary.
from copy import deepcopy
deepcopy(d) -> Returns a deep copy of the dictionary, which copies all objects recursively.

{**d}, dict(d), {key: value for key, value in d.items()} -> All are methods to create shallow copies of d.

len(d) -> Returns the number of items in the dictionary.

list(d) -> Returns a list of the keys in the dictionary.

iter(d) -> Returns an iterator over the keys. Equivalent to iter(d.keys()).
reversed(d) -> Returns a reverse iterator over the keys. Equivalent to reversed(d.keys()).

d.keys() -> Returns a read-only view of the dictionary's keys. Since, keys are unique and hashable, the view behaves like a frozen set.

d.values() -> Returns a read-only view of the dictionary's values. It doesn't behave like a frozen set.

d.items() -> Returns a read-only view of the dictionary's (key, value) pairs. It may behave as a frozen set, depending on whether the values are hashable. They need not be unique though, since the key's uniqueness guarantees that a (key, value) pair is also unique.

Note:
Views are read-only iterables. Can't update the dictionary using the views. However, they reflect the changes in the dictionary.
An equality comparison between one dict.values() view and another will always return False. This also applies when comparing dict.values() to itself.
d1.keys(), and d2.keys() are ordered, but d1.keys() | d2.keys() is a set, and isn't ordered. Moreover, set operations return an ordinary set, not a frozen set.

d.update(d2) -> Updates dictionary d with key-value pairs from dictionary d2. If a key is already present in d, its value is updated with value from d2.
d.update(iterable) -> Updates d with key-value pairs from an iterable. Usual rule for an iterable applies.
d.update(**kwargs) -> Updates d with key-value pairs from the given keyword arguments. Usual rule for keyword argument applies.

d | d2 -> Creates a new dictionary by merging d and d2, where d2 values take precedence in case of key overlap.
d |= d2 -> Updates dictionary d with keys and values from d2. This can be a dictionary or an iterable of (key, value) pairs.

3. Comparison and equality of dictionaries:

(i) Dictionaries are considered equal if they contain the same (key, value) pairs, regardless of insertion order.
(ii) Dictionary comparisons using == will check if the (key, value) pairs are the same.
(iii) Order comparisons (<, <=, >=, >) raise a TypeError.

4. Dictionary unpacking:

**d -> The double-star notation unpacks the dictionary.

{**d1, **d2, **d3} -> When unpacking multiple dictionaries, the insertion order is preserved, but the last dictionary in the sequence overrides previous ones in case of key overlap.

{**d, 'c': 100, 'd': 200} -> Unpacks the dictionary d, adding or overriding specific keys ('c' and 'd' in this case).



https://www.youtube.com/@CMU1141111611/playlists

https://www.youtube.com/watch?v=vH7ZgoXSp44&list=PLy-82AVP8uEB8UipSJGUIKrA19iONeW04&index=1

https://www.youtube.com/watch?v=xjl8NG28UXM&list=PL4YhK0pT0ZhXteJ2OTzg4vgySjxTU_QUs&index=1

https://youtube.com/playlist?list=PL4YhK0pT0ZhXteJ2OTzg4vgySjxTU_QUs&si=fVMKXlXqcozU8ujg

https://www.youtube.com/@vvinoducsd/playlists

https://www.youtube.com/@neubig/playlists

https://www.youtube.com/playlist?list=PLqC25OT8ZpD3WxQ0FwWMGPS_BcWdcKyZy
