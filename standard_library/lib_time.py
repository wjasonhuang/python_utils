"""
https://docs.python.org/3/library/time.html

time.struct_time()              an object with a named tuple interface, length = 9
time.asctime([t])               convert a tuple or struct_time to a string of form: 'Sun Jun 20 23:21:05 1993'
time.gmtime([secs])             convert a time expressed in seconds since the epoch to a struct_time in UTC
time.localtime([secs])          like gmtime() but converts to local time
time.mktime(t)                  the inverse function of localtime()
time.monotonic()                return in fractional seconds, the clock is not affected by system clock updates
time.monotonic_ns()             similar to monotonic() but return time as an integer number of nanoseconds
time.sleep(secs)                suspend execution of the calling thread for the given number of seconds
time.strftime(format[, t])      convert struct_time to a string as specified by the format argument
time.time()                     return the time in seconds since the epoch as a floating point number
time.time_ns()                  similar to time() but returns time as an integer number of nanoseconds since the epoch

Epoch = gmtime(0)               on Windows and most Unix systems, the epoch is January 1, 1970, 00:00:00 (UTC)
"""

import time

print(time.asctime())  # default time.localtime()
print(time.asctime((2020, 1, 30, 15, 54, 58, 5, 30, -1)))  # space padded if the day is a single digit

print(time.gmtime())  # default time.time()
print(time.gmtime(1))  # in UTC the dst flag is always zero

print(time.localtime())  # default time.time()
print(time.localtime(1))

print(time.mktime(time.localtime(1)))

print(time.monotonic())  # return float, fractional seconds
print(time.monotonic_ns())  # return int

print('Sleep for 2 seconds ...')
time.sleep(2)

print(time.strftime("%a, %d %b %Y, %H:%M:%S"))  # default time.localtime()
print(time.strftime("%a, %d %b %Y, %H:%M:%S", time.gmtime()))

print(time.time())  # return float
print(time.time_ns())  # return int
