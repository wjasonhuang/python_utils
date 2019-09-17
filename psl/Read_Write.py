'''
https://docs.python.org/3/tutorial/inputoutput.html

input([prompt])     read a line from input, converts it to a string (stripping a trailing newline), 
                    and returns that. When EOF is read, EOFError is raised.
f.read([size])      size = number of bytes to be read from the file
f.readline()        read a single line from the file, \n is left at the end of the string
next(f)             read next line from the file

printf-style String Formatting      %[flags][width][.precision]type
                                    flags = #, 0, -,  , +

open(file, mode='r')                mode = 'r', 'w', 'x' (create/fail if exsits), 'a' (append to the end)
https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
'''

print('----------input----------')
filename = 'input.txt'

'''
n = int(input ("\nEnter a number : "))
arr = list(map(int, input("\nEnter a list of numbers : ").split()))
'''

# It is good practice to use the with keyword when dealing with file objects.
# The advantage is that the file is properly closed after its suite finishes.
with open(filename) as f:
    read_data = f.read()        # save all data as one string
print(f.closed)                 # f.closed = True

with open(filename) as f:
    for line in f:              # read line by line
        print(line, end='')     # \n already exsits at the end of line

with open(filename) as f:
    lines = list(f)             # same as lines = f.readlines()
    lines = list(map(str.strip, lines))
    print(lines)

with open(filename) as f:
    arr = [int(x) for x in next(f).split()]
    arr += [[int(x) for x in line.split()] for line in f]
    print(arr)

print('----------output----------')
print('{0}, {1}, {2}'.format('a', 'b', 'c'), '/', '{}, {}, {}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format('a', 'b', 'c'), ',', '{2}, {1}, {0}'.format(*'abc'))
print('{0}{1}{0}'.format('aa', 'bb'))
print('{0:,.2%} {1:,} {0:,.4f}'.format(1234.56789, 9876.54321))

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print(f'Coordinates: {coord["latitude"]}, {coord["longitude"]}')
print('Coordinates: {latitude}, {longitude}'.format(**coord))
print('Coordinates: {0[latitude]}, {0[longitude]}'.format(coord))

print('.2f = %(num).2f  d = %(num)d  010d = %(num)010d' %{'num': 1234.56789})
print('.2f = %.2f  d = %d  10d = %10d  010d = %010d' %(1234.56789, 1234.56789, 1234.56789, 1234.56789))
print('%015.4e/%-15.4e/%15.4E' %(1234.56789, 1234.56789, 1234.56789))
