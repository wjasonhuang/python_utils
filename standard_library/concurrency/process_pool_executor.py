import time, concurrent.futures

def calc_pool(pool_id, sleep_time):
    print(f'Pool id {pool_id}: sleep {sleep_time} second(s)')
    time.sleep(sleep_time)
    return f'Pool id {pool_id}: finished'
 
if __name__ == '__main__':
    n, now = 5, time.time()
    sleep_time = [i / 2 for i in reversed(range(n))]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(calc_pool, i, sleep_time[i]) for i in range(n)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
        '''
            results = executor.map(calc_pool, [i for i in range(n)], sleep_time)
            for f in results: print(f)
        '''
    print(f'Total time: {round(time.time() - now, 2)} second(s)\n')
