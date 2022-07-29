"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def swap(s, alphabet):
    pos = alphabet.find(s)
    if pos + 13 <= 25:
        return alphabet[pos+13]
    else:
        return alphabet[pos-13]


def rot13(text):
    encode_str = ''
    for x in text:
        if x in alphabet_lower:
            encode_str += swap(x, alphabet_lower)
        elif x in alphabet_upper:
            encode_str += swap(x, alphabet_upper)
        else:
            encode_str += x
    return encode_str


print(rot13('Test!'))
print(rot13('abcdefghijklmnopqrstuvwxyz'))



