'''
class datetime.date         Attributes: year, month, and day
class datetime.time         Attributes: hour, minute, second, microsecond, and tzinfo
class datetime.datetime     Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo
class datetime.timedelta    Attributes: days, seconds, microseconds (1e-6)
class datetime.tzinfo
class datetime.timezone

object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
'''

import datetime

'----------datetime.date----------'
print(datetime.date.today())
d1 = datetime.date(2019,9,7)
d2 = datetime.date(2005,1,1)
print(d1, '|', d2, '|', d1-d2, "\n")

'----------datetime.time----------'
t = datetime.time(11, 52, 20, 111111)
print(t, '|', t.hour, t.minute, t.second, t.microsecond, "\n")

'----------datetime.datetime----------'
dt1 = datetime.datetime(2019,9,7,23,59,59,999999)
print(dt1, '|', dt1.year, dt1.month, dt1.day, dt1.hour, dt1.minute, dt1.second, dt1.microsecond)
dt2 = datetime.datetime(1900,1,2,3,4,5,6)
print(dt1 > dt2)
ddt = dt1 - dt2
print(ddt, '|', ddt.days, ddt.seconds, ddt.microseconds)
print(ddt.total_seconds(), "\n")

'----------datetime.timedelta----------'
timedelta = datetime.timedelta(1,3661,1)
print(dt1, '|', timedelta, '|', dt1+timedelta, '\n')

'----------strftime----------'
print(dt1)
print(dt1.strftime('%a %A'))                    # weekday as name
print(dt1.strftime('%b %B'))                    # month as name
print(dt1.strftime('%Y %m %d %H %M %S %f'))     # YYYYMMDDHHMMSSFFFFFF as number
