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


https://docs.python.org/3/library/threading.html#with-locks
Objects that have acquire() and release() methods can be used as context managers for a with statement.
The acquire() method will be called when the block is entered.
The release() will be called when the block is exited.
'''

import time
from threading import Thread, Lock, Semaphore

def calc(t_id, sleep_time, output_lock):
    with output_lock:
        print(f'Thread {t_id}: sleep {round(sleep_time, 2)} second(s)')
    time.sleep(sleep_time)
    with output_lock:
        print(f'Thread {t_id}: finished')

def calc_lock(t_id, sleep_time, sleep_lock):
    '''
        with lock:
        lock.acquire()
        lock.release()
    '''
    with sleep_lock:
        print(f'Thread {t_id}: sleep {round(sleep_time, 2)} second(s)')
        time.sleep(sleep_time)
        print(f'Thread {t_id}: finished')

def calc_n_times(t_id, sleep_time, output_lock, semaphore):
    with output_lock:
        print(f'Thread {t_id}: sleep {round(sleep_time, 2)} second(s)')
    time.sleep(sleep_time)
    with output_lock:
        print(f'Thread {t_id}: finished')
    semaphore.release()

n= 9
sleep_time = [i / 9 for i in reversed(range(n))]
output_lock = Lock()

print('----- No Lock -----')
now = time.time()
threads = [Thread(target=calc, args=(i, sleep_time[i], output_lock)) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
print(f'Total time: {round(time.time() - now, 2)} second(s)\n')

print('----- Lock -----')
now = time.time()
sleep_lock = Lock()
threads = [Thread(target=calc_lock, args=(i, sleep_time[i], sleep_lock)) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
print(f'Total time: {round(time.time() - now, 2)} second(s)\n')

print('----- Semaphore -----')
now = time.time()
semaphore = Semaphore(3) # max 3 threads each time
threads = []
for i in range(n):
    semaphore.acquire()
    t = Thread(target=calc_n_times, args=(i, sleep_time[i], output_lock, semaphore))
    t.start()
    threads.append(t)
for t in threads: t.join()
print(f'Total time: {round(time.time() - now, 2)} second(s)\n')
