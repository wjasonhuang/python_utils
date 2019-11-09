'''
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
class threading.Lock
class threading.Semaphore(value=1)
class threading.BoundedSemaphore(value=1)
class threading.Condition(lock=None)

https://docs.python.org/3/library/threading.html#with-locks
Objects that have acquire() and release() methods can be used as context managers for a with statement.
The acquire() method will be called when the block is entered.
The release() will be called when the block is exited.
'''


import time, random
from threading import Thread, Lock, Semaphore, Condition

n= 9
sleep_times = [random.randint(1, n) / n for i in reversed(range(n))]
lock = Lock()
print('----- Serial -----')
print(f'Total time: {round(sum(sleep_times), 2)} second(s)\n')


'''
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
    start()
    join(timeout=None)
    is_alive()

class threading.Lock
    acquire(blocking=True, timeout=-1)
        * Acquire a lock, blocking or non-blocking.
    release()
        * Release a lock. This can be called from any thread, not only the thread which has acquired the lock.
'''

def calc(t_id, sleep_time, lock):
    with lock:
        print(f'Thread {t_id}: sleep {round(sleep_time, 2)} second(s)')
    time.sleep(sleep_time)
    with lock:
        print(f'Thread {t_id}: finished')

print('----- Threading -----')
now = time.time()
threads = [Thread(target=calc, args=(i, sleep_times[i], lock)) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
print(f'Total time: {round(time.time() - now, 2)} second(s)\n')


'''
class threading.Semaphore(value=1)
    The optional argument gives the initial value for the internal counter; it defaults to 1. 
    acquire(blocking=True, timeout=None)
        * If the internal counter is larger than zero on entry, decrement it by one.
        * If the internal counter is zero on entry, block until awoken by a call to release().
    release()
        * Release a semaphore, incrementing the internal counter by one.
        * When it was zero on entry and another thread is waiting, wake up that thread.

class threading.BoundedSemaphore(value=1)
    A bounded semaphore checks to make sure its current value doesn’t exceed its initial value.
    If it does, ValueError is raised.
'''

def calc_max_3_threads(t_id, sleep_time, lock, semaphore):
    with lock:
        print(f'Thread {t_id}: sleep {round(sleep_time, 2)} second(s)')
    time.sleep(sleep_time)
    with lock:
        print(f'Thread {t_id}: finished')
    semaphore.release()

print('----- Semaphore -----')
now = time.time()
semaphore = Semaphore(3) # max 3 threads each time
threads = []
for i in range(n):
    semaphore.acquire()
    t = Thread(target=calc_max_3_threads, args=(i, sleep_times[i], lock, semaphore))
    t.start()
    threads.append(t)
for t in threads: t.join()
print(f'Total time: {round(time.time() - now, 2)} second(s)\n')


'''
class threading.Condition(lock=None)
    acquire(*args)
    release()
    wait(timeout=None)
    wait_for(predicate, timeout=None)
        * Wait until a condition evaluates to true.
        * predicate should be a callable which result will be interpreted as a boolean value. 
    notify(n=1)
        * By default, wake up one thread waiting on this condition, if any.
    notify_all()
        * Wake up all threads waiting on this condition.
'''

def calc_producer_consumer(lock, cv):
    while True:
        cv.acquire()
        while not thread_queue:
            cv.wait()
        t_id = thread_queue.pop(0)
        cv.release()
        with lock:
            if not sleep_times: break
            sleep_time = sleep_times.pop(0)
            print(f'Thread {t_id}: sleep {round(sleep_time, 2)} second(s)')
        time.sleep(sleep_time)
        cv.acquire()
        thread_queue.append(t_id)
        cv.notify()
        cv.release()
        with lock:
            print(f'Thread {t_id}: sleep finished')
    
    with lock:
        print(f'Thread {t_id}: finished')

print('----- Condition Variable -----')
thread_queue, threads = [0, 1, 2], []
now = time.time()
cv = Condition()
for i in range(3):
    t = Thread(target=calc_producer_consumer, args=(lock, cv))
    t.start()
    threads.append(t)
for t in threads: t.join()
print(f'Total time: {round(time.time() - now, 2)} second(s)\n')
