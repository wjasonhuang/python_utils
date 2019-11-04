import time
from multiprocessing import Process

def calc(p_id, sleep_time):
    print(f'Process {p_id}: sleep {sleep_time} second(s)')
    time.sleep(sleep_time)
    print(f'Finishing process {p_id}')

n, now = 5, time.time()
sleep_time = [i / 2 for i in reversed(range(n))]

processes = [Process(target=calc, args=[i, sleep_time[i]]) for i in range(n)]
for p in processes: p.start()
for p in processes: p.join()
print(f'Total time: {round(time.time()-now, 2)} second(s)')

'''
https://stackoverflow.com/questions/21198857/python-multiprocessing-example-not-working
'''
