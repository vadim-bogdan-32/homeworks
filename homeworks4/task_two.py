for i in range(1, 101):
    output_str = ''
    if i % 3 == 0 and i % 5 == 0:
        output_str += 'fuzzbuss'
    elif i % 3 == 0:
        output_str += 'fuzz'
    elif i % 5 == 0:
        output_str += 'buzz'
    else:
        output_str += str(i)
    print(output_str)
