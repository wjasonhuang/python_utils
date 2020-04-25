"""
https://docs.python.org/3/howto/regex.html
https://github.com/ziishaned/learn-regex

re.findall(A, B)    Matches all instances of an expression A in a string B and returns them in a list.
re.search(A, B)     Matches the first instance of an expression A in a string B, and returns it as a re match object.
re.split(A, B)      Split a string B into a list using the delimiter A.
re.sub(A, B, C)     Replace A with B in the string C.

Regex Flags
re.IGNORECASE   ignore case.
re.MULTILINE	make begin/end {^, $} consider each line.
re.DOTALL       make . match newline too.
"""

import re

with open('new.txt', 'r', encoding='utf-8') as f:
    total = 0
    for line in f:
        ret = re.findall('the', line, re.IGNORECASE)
        total += len(ret)
    print(total)

s = 'hello world!'
print(re.split('l', s))
print(re.sub('l+', '$', s))
