'''
https://docs.python.org/3/library/queue.html

class queue.Queue(maxsize=0)            constructor for a FIFO queue
class queue.LifoQueue(maxsize=0)        constructor for a LIFO queue
class queue.PriorityQueue(maxsize=0)    data format: (priority_number, data)

Queue.qsize()
Queue.empty()
Queue.full()
Queue.put(item, block=True, timeout=None)
Queue.put_nowait(item)
Queue.get(block=True, timeout=None)     remove and return an item from the queue
Queue.task_done()                       indicate that a formerly enqueued task is complete
Queue.join()
    - The count of unfinished tasks goes up whenever an item is added to the queue.
    - The count goes down whenever a consumer thread calls task_done().
    - When the count of unfinished tasks drops to zero, join() unblocks.
'''


from queue import Queue
from threading import Thread, Lock
import time, random

def worker(t_id, lock):
    while True:
        item = q.get()
        if item is None: break
        time.sleep(item)
        with lock:
            print(f'Thread {t_id}: sleep {round(item, 2)} second(s)')
        q.task_done()

num_worker, n = 3, 9
source = [random.randint(1, n - 1) / n for i in reversed(range(n))]
q = Queue()
lock = Lock()
threads = []
for i in range(num_worker):
    t = Thread(target=worker, args=(i, lock))
    t.start()
    threads.append(t)
for item in source: q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker): q.put(None)
for t in threads: t.join()
