from threading import Thread, Condition
from typing import Callable


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cur = 1
        self.cv = Condition()

    def run(self, wait_cond, func, arg=0):
        while True:
            self.cv.acquire()
            while wait_cond(self.cur):
                self.cv.wait()
            if self.cur > self.n:
                self.cv.notifyAll()
                self.cv.release()
                return
            func(self.cur) if arg else func()
            self.cur += 1
            self.cv.notifyAll()
            self.cv.release()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self.run(lambda x: x <= self.n and (x % 3 != 0 or x % 15 == 0), printFizz)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self.run(lambda x: x <= self.n and (x % 5 != 0 or x % 15 == 0), printBuzz)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self.run(lambda x: x <= self.n and x % 15 != 0, printFizzBuzz)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        self.run(lambda x: x <= self.n and (x % 3 == 0 or x % 5 == 0), printNumber, 1)


threads = []
new = FizzBuzz(15)
threads.append(Thread(target=new.fizz, args=(lambda: print('fizz'),)))
threads.append(Thread(target=new.buzz, args=(lambda: print('buzz'),)))
threads.append(Thread(target=new.fizzbuzz, args=(lambda: print('fizzbuzz'),)))
threads.append(Thread(target=new.number, args=(lambda x: print(x),)))
for t in threads: t.start()
for t in threads: t.join()
