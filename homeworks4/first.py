a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}
for key in a.keys():
    if key in b.keys():
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [a[key], None]
for key in b.keys():
    if key not in a.keys():
        ab[key] = [None, b[key]]

print(ab)
