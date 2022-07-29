"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    formatted_list = []
    text_list = text.split()
    for word in text_list:
        if word.isalpha():
            formatted_list.append(word[1:] + str(word[0]) + 'ay')
        else:
            formatted_list.append(word)
    return ' '.join(formatted_list)


def pig_it_short(text):
    return ' '.join([word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split()])

print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))

print(pig_it_short('Pig latin is cool'))
print(pig_it_short('Hello world !'))


