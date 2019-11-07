# Threading vs Multiprocessing

## Threading:
- A new thread is spawned within the existing process
- Starting a thread is faster than starting a process
- Memory is shared between all threads
- Mutexes often necessary to control access to shared data
- One GIL (Global Interpreter Lock) for all threads
- Interpreter runs the instructions serially due to GIL
- Use for programs that are IO bound or network bound

## Multiprocessing:
- A new process is started independent from the first process
- Starting a process is slower than starting a thread
- Memory is not shared between all processes
- Mutexes not necessary (unless threading in the new process)
- One GIL (Global Interpreter Lock) for each process
- Utilize multiple CPU cores
- Use for programs that are CPU bound


# Concurrency 
The concurrency is designed to above all enable multitasking, yet it could easily bring some bugs into the program if not applied properly. Depending on the consequences, the problems caused by concurrency can be categorized into three types:
- race conditions: the program ends with an undesired output, resulting from the sequence of execution among the processes. 
- deadlocks: the concurrent processes wait for some necessary resources from each other. As a result, none of them can make progress. 
- resource starvation: a process is perpetually denied necessary resources to progress its works.


# Lock vs Mutex vs Semaphore
https://stackoverflow.com/questions/34519/what-is-a-semaphore/40238#40238

## Lock:
- A lock allows only one thread to enter the part that's locked
- Lock is not shared with any other processes

## Mutex:
- A mutex is the same as a lock but it can be system wide
- Mutex is shared by multiple processes

## Semaphore:
- A semaphore does the same as a mutex but allows x number of threads to enter
- Can be used for example to limit the number of cpu, io or ram intensive tasks running at the same time


# Deadlock vs Livelock vs Starvation
https://www.geeksforgeeks.org/deadlock-starvation-and-livelock/

## Deadlock:
A deadlock is a state in which each member of a group of actions, is waiting for some other member to release a lock.
```
var p = new object() 
lock(p):
    lock(p):
        // deadlock. Since p is previously locked 
        // we will never reach here... 
```
 
## Livelock:
A livelock on the other hand is almost similar to a deadlock, except that the states of the processes involved in a livelock constantly keep on changing with regard to one another, none progressing. T
```
var l1 = .... // lock object like semaphore or mutex etc 
var l2 = .... // lock object like semaphore or mutex etc 
    // Thread1       
    while True:
        if (!l1.Lock(1000)) continue; 
        if (!l2.Lock(1000)) continue; 
        // do some work 
    }); 
  
    // Thread12      
    while True:
        if (!l2.Lock(1000)) continue; 
        if (!l1.Lock(1000)) continue; 
        // do some work 
    }); 
```
