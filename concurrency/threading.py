import time
from threading import Thread, Lock

def print_time():
    global now
    temp = time.time()
    print(f'Total time: {round(temp - now, 2)} second(s)\n')
    now = temp

def calc(t_id, sleep_time):
    print(f'Thread {t_id}: sleep {sleep_time} second(s)')
    time.sleep(sleep_time)
    print(f'Thread {t_id}: finished')

def calc_lock(t_id, sleep_time):
    global lock
    '''
        with lock:
        lock.acquire()
        lock.release()
    '''
    with lock:
        print(f'Thread {t_id}: sleep {sleep_time} second(s)')
        time.sleep(sleep_time)
        print(f'Thread {t_id}: finished')
 
n, now = 4, time.time()
sleep_time = [i / 2 for i in reversed(range(n))]

print('----- No Lock -----')
threads = [Thread(target=calc, args=(i, sleep_time[i])) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
print_time()

print('----- Lock -----')
lock = Lock()
threads = [Thread(target=calc_lock, args=[i, sleep_time[i]]) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
print_time()
