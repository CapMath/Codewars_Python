"""
DESCRIPTION:
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


# My solution
def generate_hashtag(s):
    capitalized_list = [x.capitalize() for x in s.split()]
    hashtag_string = f'#{"".join(capitalized_list)}'
    if hashtag_string == '#' or len(hashtag_string) > 140:
        return False
    else:
        return hashtag_string


# Good solution
def generate_hashtag_good(s):
    hashtag_string = '#' + str(s.title().replace(' ', ''))
    return False if (len(hashtag_string) == 1 or len(hashtag_string) > 140) else hashtag_string


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))

print(generate_hashtag_good(" Hello there thanks for trying my Kata"))
print(generate_hashtag_good("    Hello     World   "))
print(generate_hashtag_good(""))
