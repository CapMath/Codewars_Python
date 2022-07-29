"""Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    zeros = []
    without_zeros = []
    for elem in lst:
        if elem != 0:
            without_zeros.append(elem)
        else:
            zeros.append(0)
    return without_zeros + zeros


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
