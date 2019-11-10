# Threading vs Multiprocessing
Resources needed?

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



# Context Switching

## When to switch:
- Multitasking - Most commonly, within some scheduling scheme, one process must be switched out of the CPU so another process can run.
- Interrupt handling - Modern architectures are interrupt driven. This means that if the CPU requests data from a disk, for example, it does not need to busy-wait until the read is over; it can issue the request and continue with some other execution. When the read is over, the CPU can be interrupted and presented with the read.
- User and kernel mode switching - A context switch may take place but isn't always necessary

## Steps:
- The process state includes all the registers (usually consist of a small amount of fast storage) that the process may be using, especially the program counter (a processor register that indicates where a computer is in its program sequence), plus any other operating system specific data that may be necessary. This is usually stored in a data structure called a process control block (PCB) or switchframe.
- The PCB might be stored on a per-process stack in kernel memory (as opposed to the user-mode call stack), or there may be some specific operating system defined data structure for this information. A handle to the PCB is added to a queue of processes that are ready to run, often called the ready queue.
- Since the operating system has effectively suspended the execution of one process, it can then switch context by choosing a process from the ready queue and restoring its PCB. In doing so, the program counter from the PCB is loaded, and thus execution can continue in the chosen process.

## Thread Switch vs Process Switch:
- Both handing control over to the operating system kernel to perform the context switch.
- The process of switching in and out of the OS kernel along with the cost of switching out the registers is the largest fixed cost of performing a context switch.
- Both need to change the execution context (registers, stack pointers, program counters)

- The virtual memory space remains the same for a thread switch, it does not during a process switch.
- When you context switch, all of the memory addresses that the processor "remembers" in its cache effectively become useless.
- When you change virtual memory spaces, the processor's Translation Lookaside Buffer (TLB, on CPU) or equivalent gets flushed making memory accesses much more expensive for a while. 



# Scheduling
https://youtu.be/2h3eWaPx8SA
```
                |<----- partially executed swapped-out process <-----|            
                |                                                    |            
job queue ----->|-----> ready queue -----(scheduler)-----> CPU ----->|-----> end
                |                                                    |
                |<----- I/O <--------------- I/O waiting queue <-----|
```



# Lock vs Mutex vs Semaphore vs Condition Variable vs Monitor

## Lock:
- A lock allows only one thread to enter the part that's locked
- Lock is not shared with any other processes

## Mutex:
- A mutex is the same as a lock but it can be system wide
- Mutex is shared by multiple processes
- Mutex is locking mechanism 

## Semaphore:
- A semaphore does the same as a mutex but allows x number of threads to enter
- Can be used for example to limit the number of cpu, io or ram intensive tasks running at the same time
- Use a semaphore when you (thread) want to sleep till some other thread tells you to wake up
- Semaphore is signaling mechanism

## Condition Variable
- Used to wait for a particular condition to become true (e.g. characters in buffer)
- https://docs.python.org/2.0/lib/condition-objects.html

## Monitor:
- A synchronization construct that allows threads to have both mutual exclusion and the ability to wait (block) for a certain condition to become true
- Monitors also have a mechanism for signaling other threads that their condition has been met
- A monitor consists of a mutex (lock) object and condition variables



# Race Condition vs Deadlock vs Livelock vs Starvation
https://www.geeksforgeeks.org/deadlock-starvation-and-livelock/

## Race Condition:
The program ends with an undesired output, resulting from the sequence of execution among the processes. 

## Deadlock:
A deadlock is a state in which each member of a group of actions, is waiting for some other member to release a lock.
- All threads wait forever
- Cannot end without external intervention
```
lock(p):
    lock(p): 
        // since p is previously locked, we will never reach here... 
```

## Livelock:
A livelock on the other hand is almost similar to a deadlock, except that the states of the processes involved in a livelock constantly keep on changing with regard to one another, none progressing.
```
    // Thread1       
    while True:
        if (!l1.Lock(1000)) continue; 
        if (!l2.Lock(1000)) continue; 
        // do some work 
    }); 
  
    // Thread2      
    while True:
        if (!l2.Lock(1000)) continue; 
        if (!l1.Lock(1000)) continue; 
        // do some work 
    }); 
```

## Starvation:
Starvation is a problem which is closely related to both, Livelock and Deadlock. In a dynamic system, requests for resources keep on happening. Thereby, some policy is needed to make a decision about who gets the resource when. This process, being reasonable, may lead to some processes never getting serviced even though they are not deadlocked. Starvation happens when “greedy” threads make shared resources unavailable for long periods.
- One or more threads wait indefinitely
- Can end but does not have to



# Dealing with deadlock

## 4 Conditions for Deadlock:
All 4 conditions must hold for deadlock to occur
1. Mututal Exclusoin
    *  At least one held resource must be non-sharable
2. Hold and Wait
    * There exists a process holding a resource and waiting for another
3. No preemption
    * Resources cannot be preempted
4. Cicular Wait
    * There exists a set of processes {P1, .., Pn}, such that P1 is waiting for P2, P2 for P3, ..., Pn for P1

In computing, preemption is the act of temporarily interrupting a task being carried out by a computer system, without requiring its cooperation, and with the intention of resuming the task at a later time. Such changes of the executed task are known as context switches. It is normally carried out by a privileged task or part of the system known as a preemptive scheduler, which has the power to preempt, or interrupt, and later resume, other tasks in the system.

## Resource Allocation Graph
A set of vertices V and a set of edges E
* V is partitioned into two types:
    * P = {P1, P2, …, Pn}, the set consisting of all the processes in the system
    * R = {R1, R2, …, Rm}, the set consisting of all resource types in the system
* E is partitioned into two types:
    * request edge – directed edge Pi -> Rj
    * assignment edge – directed edge Rj -> Pi

Basic Facts:
- If graph contains no cycles => no deadlock
- If graph contians a cycle =>
    * if only one instance per resource type => deadlock
    * if several instances per resource type => possibility of deadlock

## Deadlock Prevention
1. Pretend deadlocks will never occur and reboot the system if a deadlock occurs
2. Reactive
    * Periodically check for evidence of deadlock (timeouts)
    * Blue screen and reboot the computer
    * Pick a thread to terminate (thread must be cleaned up when terminated and retries from scratch)
    * This breaks the preemption condition, database systems do this
3. Proactive: prevent 1 of the 4 necessary conditions
    * No mutual exclusion
    * No hold and wait, only request a resource when have none, release before requesting another (low concurrency)
    * Preempt resources (not possible if a resource cannot be saved and restored)
    * No circular wait, lock hierarchy, give all resources a ranking and must acquire highest ranking first

## Deadlock Avoidance
Banker’s Algorithm
