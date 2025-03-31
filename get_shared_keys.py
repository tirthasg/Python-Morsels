def get_shared_keys(dict1, dict2):
    return [key for key in dict1.keys() if key in set(dict2.keys())]


expired = {"c95": "20200315", "d45": "20200401", "b38": "20200415"}
used_recently = {"a56": 8, "b38": 1, "e77": 4, "d45": 3}
print(get_shared_keys(expired, used_recently))
# ['d45', 'b38']
