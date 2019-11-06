import time, concurrent.futures

def calc_pool(pool_id, sleep_time):
    print(f'Pool id {pool_id}: sleep {sleep_time} second(s)')
    time.sleep(sleep_time)
    return f'Pool id {pool_id}: finished'

n = 4
sleep_time = [i / 2 for i in reversed(range(n))]

now = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(calc_pool, i, sleep_time[i]) for i in range(n)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
print(f'Total time: {round(time.time() - now, 2)} second(s)\n')

now = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(calc_pool, [i for i in range(n)], sleep_time)
    for f in results: print(f)
print(f'Total time: {round(time.time() - now, 2)} second(s)\n')
