"""
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def multiplies(n):
    multiply_arr = []
    div = n
    i = 2
    while div >= i:
        if div % i == 0:
            div = div / i
            multiply_arr.append(i)
        else:
            i += 1
    return multiply_arr


def prime_factors(n):
    final_arr = []
    multi_arr = multiplies(n)
    for x in sorted(set(multi_arr)):
        if multi_arr.count(x) == 1:
            final_arr.append(f'({x})')
        else:
            final_arr.append(f'({x}**{multi_arr.count(x)})')
    return ''.join(final_arr)


# print(prime_factors(23143432564564))

