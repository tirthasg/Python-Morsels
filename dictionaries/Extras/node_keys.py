def get_keys(n1, n2, n3):
    union = n1.keys() | n2.keys() | n3.keys()
    intersection = n1.keys() & n2.keys() & n3.keys()
    relevant = union - intersection

    return {key: (n1.get(key, 0), n2.get(key, 0), n3.get(key, 0)) for key in relevant}


n1 = {
    "employees": 100,
    "employee": 5000,
    "users": 10,
    "user": 100,
}

n2 = {
    "employees": 250,
    "users": 23,
    "user": 230,
}

n3 = {
    "employees": 150,
    "users": 4,
    "login": 1000,
}

print(get_keys(n1, n2, n3))
