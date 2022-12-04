a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

list_a = [a.get('a'), b.get('a')]
list_b = [a.get('b'), b.get('b')]
list_c = [a.get('c'), b.get('c')]
list_d = [a.get('d'), b.get('d')]
list_e = [a.get('e'), b.get('e')]
ab = {'a': list_a, 'b': list_b, 'c': list_c, 'd': list_d, 'e': list_e}
print(ab)
