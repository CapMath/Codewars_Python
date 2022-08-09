"""
The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared).
Eighty one (81), is the first number in having this property (not considering numbers of one digit).
The next one, is 512. Let's see both cases with the details

8 + 1 = 9 and 9**2 = 81

512 = 5 + 1 + 2 = 8 and 8**3 = 512

We need to make a function that receives a number as argument n and returns the n-th term of this sequence of numbers.
"""

def digit_sum(n):
    str_n = str(n)
    list_of_elem = list(str_n)
    return sum([int(x) for x in list_of_elem])


def power_sumDigTerm(n):
    list_of_elem = []
    i = 0
    k = 1
    elem = 2
    pow = 2
    res = 0
    while i < 100:
        min = 10**(k-1)
        max = 10**k
        while elem < max**0.5 and elem <= 9*k:
            while res < max:
                res = elem**pow
                if min < res < max:
                    if digit_sum(res) == elem:
                        i += 1
                        list_of_elem.append(res)
                elif res >= max:
                    break
                else:
                    pass
                pow += 1
            elem += 1
            pow = 2
            res = 0
        k += 1
        elem = 2
        pow = 2
        res = 0
    list_of_elem.sort()
    return list_of_elem[n-1]

print(power_sumDigTerm(1))