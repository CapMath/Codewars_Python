"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def lim(num):
    if num < 0:
        num = 0
    elif num > 255:
        num = 255
    return num


def rgb(a, b, c):
    return '{:02X}{:02X}{:02X}'.format(lim(a), lim(b), lim(c))


print(rgb(255, 255, 255))
print(rgb(255, 255, 300))
print(rgb(0, 0, 0))
print(rgb(255, 255, 3))
print(rgb(-20, 255, 3))
