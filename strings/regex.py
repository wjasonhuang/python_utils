import re

filename = 'regex_sum_207425.txt'
handle = open(filename)

total = 0;
for line in handle:
    numbers = re.findall('[0-9]+', line)
    total = total + sum([int(num) for num in numbers])

print(total)
