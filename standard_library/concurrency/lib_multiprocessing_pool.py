import time
from multiprocessing import Pool

def compute(n):
    ret = 0
    for i in range(n):
        ret += i * i
    return ret

def compute_serial(numbers):
    
    start_time = time.time()
    results = [compute(n) for n in numbers]
    print(f'compute_serial: {round(time.time()-start_time, 2)} second(s) {sum(results)}')

def compute_multi_processing(numbers):
    
    start_time = time.time()
    p = Pool()      # when args missing, default to maximum cores = os.cpu_count()
    results = p.map(compute, numbers)
    p.close()       # Prevents any more tasks from being submitted to the pool.
    p.join()
    print(f'compute_multi_processing: {round(time.time()-start_time, 2)} second(s) {sum(results)}')

if __name__ == '__main__':
    
    numbers = range(10000, 15000)
    compute_serial(numbers)
    compute_multi_processing(numbers)
