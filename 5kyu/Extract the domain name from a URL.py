"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""
import re


def domain_name(url):
    trim_http = re.sub(r'.*//', r'', url)
    trim_www = re.sub(r'www.', r'', trim_http)
    domen = re.sub(r'\..*$', r'', trim_www)
    return domen


test1 = "http://github.com/carbonfive/raygun"
test2 = "http://www.zombie-bites.com"
test3 = "https://www.cnet.com"
print(domain_name(test1))
print(domain_name(test2))
print(domain_name(test3))
