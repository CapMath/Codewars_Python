"""
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum
of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed
in the same manner as in the drawing:

Hint:
See Fibonacci sequence

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
"""


def perimeter(n):
    fib_seq = [0, 1]
    for i in range(n):
        fib_seq.append(fib_seq[i] + fib_seq[i+1])
    return sum(fib_seq) * 4


print(perimeter(0))
