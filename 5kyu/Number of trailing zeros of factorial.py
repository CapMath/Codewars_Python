"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...
"""


def zeros(n):
    counter = 0
    i = 1
    while n >= 5**i:
        counter += n // 5**i
        i += 1
    return counter

print(zeros(4))
print(zeros(5))
print(zeros(25))




