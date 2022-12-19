def upper_case(func):
    def wrap(list):
        res = str(func(list)).upper()
        return res
    return wrap


@upper_case
def get_text(list):
    result = ''
    for i in range(len(list)):
        result += list[i] + ' '
    return result


list_one = ['Hello', 'my', 'dear', 'friends']
print(get_text(list_one))
