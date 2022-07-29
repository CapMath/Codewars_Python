"""[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)"""


def find_outlier(integers):
    even_list = [x for x in integers if x % 2 == 0]
    odd_list = [x for x in integers if x % 2 == 1]
    if len(even_list) > len(odd_list):
        return odd_list[0]
    else:
        return even_list[0]


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
