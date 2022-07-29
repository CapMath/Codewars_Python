"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""
import re


def read_number(s):
    str_num = re.search(r'[\d]*$', s).group(0)
    if str_num == '':
        return '0'
    else:
        return str_num



def read_text(s):
    clr_str = re.search(r'^.*[^\d]', s)
    if clr_str == None:
        return ''
    else:
        return clr_str.group(0)


def start_with_zero(s):
    inc_number = int(s) + 1
    my_format = '{:0' + str(len(s)) + 'd}'
    return f'{my_format}'.format(inc_number)


def increment_string(s):
    s_num = read_number(s)
    clear_string = read_text(s)
    if s_num[0] == '0':
        return f'{clear_string}{start_with_zero(s_num)}'
    else:
        return f'{clear_string}{str(int(s_num) + 1)}'


print(increment_string('foo'))
print(increment_string(''))
print(increment_string('1'))
print(increment_string('foo1'))
print(increment_string('foo01'))
print(increment_string('foo0099'))
print(increment_string('foo00'))


# Best practice
def increment_string_best(s):
    head = s.rstrip('0123456789')
    tail = s[len(head):]
    if tail == "":
        return s+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

