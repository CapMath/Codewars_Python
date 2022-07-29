"""This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(s):
    counter = 1
    string_list = []
    for ch in s:
        my_str = ''
        for i in range(counter):
            my_str = my_str + ch.lower()
        counter += 1
        my_str = my_str.capitalize()
        string_list.append(my_str)
    return '-'.join(string_list)


print(accum('abCd'))