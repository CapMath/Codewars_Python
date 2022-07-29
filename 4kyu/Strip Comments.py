"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:
apples, pears # and bananas
grapes
bananas !apples

The output expected would be:
apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def del_comments(strng, markers):
    pos = len(strng) + 1
    for m in markers:
        if -1 < strng.find(m) < pos:
            pos = strng.find(m)
    return strng[:pos].rstrip()


def strip_comments(strng, markers):
    return '\n'.join([del_comments(one_string, markers) for one_string in strng.split('\n')])


print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))
print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']))


