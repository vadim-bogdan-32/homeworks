def get_winners(results):
    index_list = []
    length = len(results)
    for i in range(length):
        if results[i] > 600 or results[i] < 0:
            return 'Invalid value'
    sorted_results = sorted(results)

    for i in range(length - 1, length - 4, -1):
        index_list.append(results.index(sorted_results[i]) + 1)
    return index_list


results = [500, 550, 300, 590, 100, 599]
print(get_winners(results))
