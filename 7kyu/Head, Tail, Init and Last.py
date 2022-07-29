"""
Your job is to implement these functions in your given language. Make sure it doesn't edit the array; that would cause problems! Here's a cheat sheet:

| HEAD | <----------- TAIL ------------> |
[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
| <----------- INIT ------------> | LAST |

Here's how I expect the functions to be called in your language:

head([1,2,3,4,5]) => 1
tail([1,2,3,4,5]) => [2,3,4,5]
init([1,2,3,4,5]) => [1,2,3,4]
last([1,2,3,4,5]) => 5
"""


def head(lst):
    return lst[0]


def tail(lst):
    return lst[1:]


def init(lst):
    return lst[:-1]


def last(lst):
    return lst[-1]


print(head([42, 16, 24, 33, 24]))
print(tail([42, 16, 24, 33, 24]))
print(init([42, 16, 24, 33, 24]))
print(last([42, 16, 24, 33, 24]))
