import time
from threading import Thread, Lock

def calc(t_id, sleep_time):
    print(f'Thread {t_id}: sleep {sleep_time} second(s)')
    time.sleep(sleep_time)
    print(f'Finishing thread {t_id}')

def calc_pool(t_id, sleep_time):
    print(f'Thread {t_id}: sleep {sleep_time} second(s)')
    time.sleep(sleep_time)
    return f'Finishing thread {t_id}'

def calc_lock(t_id, sleep_time):
    global mutex # mutual exclusion object
    with mutex: # same as using mutex.acquire(), mutex.release()
        print(f'Thread {t_id}: sleep {sleep_time} second(s)')
        time.sleep(sleep_time)
        print(f'Finishing thread {t_id}')
 
n = 5
sleep_time = [i for i in reversed(range(n))]

print('----- No mutex -----')
now = time.time()
threads = [Thread(target=calc, args=[i, sleep_time[i]]) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
print(f'Total time: {round(time.time()-now, 2)} second(s)')


print('\n----- Mutex -----')
mutex = Lock()
now = time.time()
threads = [Thread(target=calc_lock, args=[i, sleep_time[i]]) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
print(f'Total time: {round(time.time()-now, 2)} second(s)')

import concurrent.futures

print('\n----- ThreadPoolExecutor-----')
now = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(calc_pool, i, sleep_time[i]) for i in range(n)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
print(f'Total time: {round(time.time()-now, 2)} second(s)')
