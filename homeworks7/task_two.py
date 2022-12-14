def is_right_angle_triangle(a, b, c):
    result = {}
    if a + b < c:
        result['result'] = False
        result['description'] = 'no such triangle exists'
        return result
    if a**2 + b**2 == c**2:
        result['result'] = True
        result['description'] = 'the triangle is right-angled'
    else:
        result['result'] = False
        result['description'] = 'the triangle is not right angled'
    return result


result = is_right_angle_triangle(11, 11, 21)
print(result)
