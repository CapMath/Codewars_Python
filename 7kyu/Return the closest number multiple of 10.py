"""
Given a number return the closest number to it that is divisible by 10.

Example input:
22
25
37

Expected output:
20
30
40
"""


def closest_multiple_10(i):
    if i % 10 >= 5:
        return (int(i/10) + 1) * 10
    else:
        return int(i/10) * 10


print(closest_multiple_10(23))
print(closest_multiple_10(25))


def closest_multiple_10_perf(i):
    return round(i, -1)


print(closest_multiple_10(23))
print(closest_multiple_10(25))

