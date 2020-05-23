"""
https://docs.python.org/3/library/statistics.html

statistics.mean(data)                   middle value of data, using the mean of middle two method
statistics.median(data)                 return the average of the two middle values
statistics.median_low(data)             return the smaller of the two middle values
statistics.median_high(data)            return the larger of the two middle values
statistics.mode(data)                   return the most common data point, StatisticsError if more than one
statistics.pstdev(data, mu=None)        population stdev (/n), mu the mean of data
statistics.pvariance(data, mu=None)     population variance (/n)
statistics.stdev(data, xbar=None)       sample stdev (/(n-1)), xbar the mean of data
statistics.variance(data, xbar=None)    sample variance (/(n-1))

New in Python 3.8
statistics.fmean(data)                  convert data to floats and compute the arithmetic mean
statistics.geometric_mean(data)         compute the geometric mean, StatisticsError if empty or contains value <= 0
statistics.mode(data)                   return the most common data point, tiebreaker first one encountered
statistics.multimode(data)              return a list of the most common values in the order they were first encountered
statistics.quantiles(data, n=4)         return a list of n - 1 cut points separating the intervals
"""

import statistics

a = [i for i in range(100)] + [50]
print(statistics.mean(a), statistics.pstdev(a), statistics.stdev(a))
print(statistics.mode(a))
