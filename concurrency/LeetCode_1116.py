from typing import Callable

from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.c = 1
        self.l = Lock()
        self.lo = Lock()
        self.le = Lock()
        self.lo.acquire()
        self.le.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.l.acquire()
            if self.c > self.n:
                self.lo.release()
                self.le.release()
                return
            printNumber(0)
            if self.c & 1:
                self.lo.release()
            else:
                self.le.release()
            
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.le.acquire()
            if self.c > self.n: return
            printNumber(self.c)
            self.c += 1
            self.l.release()
    
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.lo.acquire()
            if self.c > self.n: return
            printNumber(self.c)
            self.c += 1
            self.l.release()


from threading import Thread

def printNumber(x):
    print(x, end='')

a = ZeroEvenOdd(5)
threads = [Thread(target=a.zero, args=[printNumber]), \
           Thread(target=a.even, args=[printNumber]), \
           Thread(target=a.odd, args=[printNumber])]
for t in threads: t.start()
for t in threads: t.join()
