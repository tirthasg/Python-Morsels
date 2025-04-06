Creating a dictionary:

Note:
The keys of a dictionary must be hashable objects.
However, the values can be any python object.
In Python 3.7+, dicts are guaranteed to be ordered in the insertion order of it's keys.

1. Using the constructor:

```python
dict([iterable], **kwargs)
```

Examples:

(i) Using a list of tuples:

```python
pairs = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(pairs)
print(my_dict)
```

(ii) Using a list of key-value pairs (using a list of lists):

```python
pairs = [['a', 1], ['b', 2], ['c', 3]]
my_dict = dict(pairs)
print(my_dict)
```

(iii) Using zip() with two lists:

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)
```

(iv) Using keyword arguments:

```python
my_dict = dict(a=1, b=2, c=3)
print(my_dict)
```
Note:
While using keyword arguments to construct the dict object, the keys must be valid identifier names.
Moreover, in the dict object, the keys will be strings of those names.

2. Using a dict literal:

{
    key1: value1,
    key2: value2,
    key3: value3,
    ...
}


Example:

```python
d = {
    "john": ["John", "Cleese", 78],
    (0, 0): "origin",
    "repr": lambda x: x ** 2,
    "eric": {
        "name": "Eric Idle",
        "age": 75
    }
}
```

dict(**kwargs)

dict(iterable, **kwargs) -> Iterable, where each item of the iterable is an iterable with exactly two elements. The first element becomes the key, and the second element becomes it's value.

dict(mapping, **kwargs)

Returns a dictionary initialized from the optional positional argument, and a possible empty set of keyword arguments.
The keyword argument only work for keys when they are valid python identifiers.


list(d) -> Returns a list of all keys in the dictionary.
len(d) -> Returns the number of items in the dictionary.

key in d -> Returns True if key in d. Else, False.
key not in d -> Returns True if key not in d. Else, True.

d[key] -> As an expression, returns the value corresponding to the key, if present. Else, KeyError exception.
d[key] = value -> Updates the value for the key with value, if present. Else, inserts the key with value set to value.

iter(d) -> Returns a iterator over the keys of the dictionary. Shortcut for iter(d.keys())
reversed(d) -> Returns a reversed iterator over the keys of the dictionary. Shortcut for reversed(d.keys())

d.clear() -> Removes all items from the dictionary.
d.copy() -> Returns a shallow copy of the dictionary. Same as dict(d)

dict.fromkeys(iterable, value=None) -> A classmethod which returns a dictionary with keys from the iterable, and all the values are set to value. All the values refer to the same instance. Mutating, if possible, will result in mutation of all the values in the dictionary. If value isn't specified, it defaults to None.

d.get(key, default=None) -> Returns the value for the key, if present. Else, returns the default value. The default value defaults to None when unspecified.

d.setdefault(key, default=None) -> If key in dictionary, return it's value. Else, insert key with value set to default, and return the default. The default defaults to None.

d.update ???

d.pop(key [, default]) -> If key is present, remove it, and return it's value. Else, if default is specified, then return it. Otherwise, KeyError exception.

    1. key is present -> remove the key, and return d[key]
    2. key not present, and default specified -> return default
    3. key not present, and default is unspecified -> KeyError exception

d.popitem() -> If dictionary isn't empty, remove, and return a (key, value) pair in LIFO order. Else, KeyError exception.   

dict.items() -> Returns a view of the dictionary's items.
dict.keys() -> Returns a view of the dictionary's keys.
dict.values() -> Returns a view of the dictionary's values.


