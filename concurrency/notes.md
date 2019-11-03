# Threading vs Multiprocessing

Threading:
- A new thread is spawned within the existing process
- Starting a thread is faster than starting a process
- Memory is shared between all threads
- Mutexes often necessary to control access to shared data
- One GIL (Global Interpreter Lock) for all threads
- Interpreter runs the instructions serially due to GIL
- Use for programs that are IO bound or network bound

Multiprocessing:
- A new process is started independent from the first process
- Starting a process is slower than starting a thread
- Memory is not shared between all processes
- Mutexes not necessary (unless threading in the new process)
- One GIL (Global Interpreter Lock) for each process
- Utilize multiple CPU cores
- Use for programs that are CPU bound

