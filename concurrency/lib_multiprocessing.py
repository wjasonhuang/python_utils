'''
https://docs.python.org/3/library/multiprocessing.html
if __name__ == '__main__' part is necessary
Work in command prompt but not in IDE
'''

import time, os
from multiprocessing import Process, Value, Lock

def sleep(p_id, sleep_time):
    print(f'#{p_id} Process {os.getpid()}: sleep {sleep_time} second(s)')
    time.sleep(sleep_time)
    print(f'#{p_id} Process {os.getpid()}: finished')

def sleep_multi_processing(sleep_time):
    print('\n----- sleep couple seconds multiprocessing -----')
    
    start_time = time.time()
    processes = [Process(target=sleep, args=(i, j)) for i, j in enumerate(sleep_time)]
    for p in processes: p.start()
    for p in processes: p.join()
    end_time = time.time()
    print(f'Total time: {round(end_time - start_time, 2)} second(s)')

def add_50(total):
    for i in range(50):
        time.sleep(0.01)
        total.value += 1

def add_50_lock(total, lock):
    for i in range(50):
        time.sleep(0.01)
        with lock:
            total.value += 1

def add_500_multi_processing():
    print('\n----- add one 500 times multiprocessing -----')
    
    total = Value('i', 0) # d for double, i for integer
    procs = [Process(target=add_50, args=(total, )) for _ in range(10)]
    for p in procs: p.start()
    for p in procs: p.join()
    print(f'add_50 total: {total.value}')

    total, lock = Value('i', 0), Lock()
    procs = [Process(target=add_50_lock, args=(total, lock)) for _ in range(10)]
    for p in procs: p.start()
    for p in procs: p.join()
    print(f'add_50_lock total: {total.value}')

if __name__ == '__main__':
    sleep_multi_processing([i / 2 for i in reversed(range(3))])
    add_500_multi_processing()

'''
Multiprocessing - Pipe vs Queue, Manager
'''
