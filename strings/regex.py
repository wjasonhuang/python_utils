"""
https://docs.python.org/3/howto/regex.html
https://github.com/ziishaned/learn-regex

re.findall(A, B)
re.search(A, B)
re.split(A, B)
re.sub(A, B, C)

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
