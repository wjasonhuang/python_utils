from time import time, sleep
import concurrent.futures

def print_time():
    global now
    temp = time()
    print(f'Total time: {round(temp - now, 2)} second(s)\n')
    now = temp

def calc_pool(pool_id, sleep_time):
    print(f'Pool id {pool_id}: sleep {sleep_time} second(s)')
    sleep(sleep_time)
    return f'Pool id {pool_id}: finished'
 
def calc_pool2(sleep_time):
    pool_id = 1
    print(f'Pool id {pool_id}: sleep {sleep_time} second(s)')
    time.sleep(sleep_time)
    return f'Pool id {pool_id}: finished'

n, now = 3, time()
sleep_time = [i for i in reversed(range(n))]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(calc_pool, i, sleep_time[i]) for i in range(n)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
print_time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(calc_pool, [i for i in range(n)], sleep_time)
    for f in results: print(f)
print_time()

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(calc_pool, i, sleep_time[i]) for i in range(n)]
    #for f in concurrent.futures.as_completed(results): print(f.result())
print_time()

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(calc_pool, [i for i in range(n)], sleep_time)
    #for f in results: print(f)
print_time()
