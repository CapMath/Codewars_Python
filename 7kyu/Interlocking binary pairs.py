def interlockable(a, b):
    a_arr = list('{0:b}'.format(a)[::-1])
    b_arr = list('{0:b}'.format(b)[::-1])
    is_one = list(map(lambda x, y: x == y == '1', a_arr, b_arr))
    return not any(is_one)


print(interlockable(1, 7))
