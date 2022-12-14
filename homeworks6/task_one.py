def dist(*args):
    distance_sum = 0
    for index, coords in enumerate(args):
        if index == len(args) - 1:
            break
        x1, y1 = coords
        x2, y2 = args[index + 1]
        length = ((x2-x1)**2 + (y2-y1)**2)**0.5
        distance_sum += length
    return distance_sum


result = dist((1, 1), (1, 2), (2, 2), (3, 3))
print(result)
