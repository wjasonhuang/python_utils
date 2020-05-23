"""
https://docs.python.org/3/library/random.html

random.seed()                       initialize the random number generator using the current system time

random.choice(seq)                  return a random element from the non-empty sequence seq
random.choices(population, k=1)     return a k sized list of elements chosen from the population with replacement
random.shuffle(x[, random])         shuffle the sequence x in place
random.sample(population, k)        return a k length list of unique elements chosen from the population

random.randint(a, b)                return a random integer N such that a <= N <= b
random.random()                     random floating in the range [0.0, 1.0)
random.uniform(a, b)                random floating in [a, b] or [b, a]
random.expovariate(lambd)           exponential distribution with mean = 1/lambd
random.gauss(mu, sigma)             gaussian distribution with mean = mu and standard deviation = sigma
random.lognormvariate(mu, sigma)    log normal distribution
"""

import random

a = [i for i in range(10)]
random.shuffle(a)
print(a)
print(random.choices(a, k=5))
print(random.sample(a, 5))
print([random.gauss(0, 1) for _ in range(5)])
