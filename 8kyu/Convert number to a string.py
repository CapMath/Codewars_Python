'''
We need a function that can transform a number into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
'''


def number_to_string(num):
    return str(num)


print(number_to_string(10))
print(type(number_to_string(-5)))
print(number_to_string(67) == '67')