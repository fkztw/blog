Title: OS Ch6 - Synchronization  
Date: 2013-11-05 03:07  
Author: fkz  
Category: Course  
Tags: Operating System  
Slug: os-ch6-synchronization  
  
  
# Monitors  
  
+ Invented by **Tony Hoare** in 1974  
+ Like a C++ class  
    + Consists of vars and procedures  
        1. Only one thread in a monitor at a time (automatic mutual exclusion)  
        2. Specifal type of variable, called **condition variable**  
            + wait  
            + signal  
            + broadcast  
        3. No public variables allowed (must call procedures to access variables)  
  
+ A high-level abstraction that provides a convenient and effective mechanism for process synchronization  
+ Only one process may be active within the monitor at a time  
  
+ Condition Variables  
    1. Automatic unlock and lock for mutual exclusion  
    2. cond.wait () - Thread is put on queue for “cond”, goes to sleep.  
    3. cond.signal () - If queue for “cond” not empty, wake up on thread  
    4. cond.broadcast() - Wake up all threads waiting on queue for “cond”  
  
  
+ Semantics of Signal  
    + Signal and Wait (Hoare-style)  
        + Signaler passes lock, CPU to waiter; waiter runs immediately  
        + Waiter gives lock, CPU back to signaler when  
            1. It exits critical section  
            2. Or, it waits again  
    + Signal and Continue (Mesa-style)  
        + invented by Xerox company  
        + signaler continues executing  
        + waiter put on ready queue  
        + when waiter actually gets to run  
            1. May have to wait for lock again  
            2.  State may have changed! Use “while”, not “if”  
        + Used in Java, Pthread  
    + [Monitor types](http://www.cs.mtu.edu/~shene/NSF-3/e-Book/MONITOR/monitor-types.html)  
  
+ Bounded Buffer by Monitor  
    In Bounded Buffer,  
```c  
Enqueue (int v)  
{  
		while( size == MAX_SIZE) full.wait();  
  
		BUFFER[tail] = v;  
		tail = (tail+1) % MAX_SIZE;  
		size++;  
  
		if (size ==1) empty.signal();  
}  
```  
```c  
Deque (int v)  
{  
		while(size==0) empty.wait();  
  
		int i = head;  
		head = (head+1) % MAX_SIZE;  
		size--;  
  
		if ( size == MAX_SIZE-1) full.signal();  
		return BUFFER[i];  
}  
```  
  
+ Hoare Style  
    + Monitor Implementation (using semaphores)  
        + Need mutual exclusion semaphore **mutex (init to 1)** so that only one process is    active within monitor  
        + Need a semaphore **next (next to exit)** for the signaling process to suspend itself  
            + initialized to zero  
        + **next_count** is number of processes blocked on **next**  
        + Before exiting a procedure, process must either:  
            1. Signal other waiting processes in monitor next before exiting  
            2. Signal mutex and exit  
    + Monitor Implementation  
```lisp  
	Procedure F:  
				wait(mutex);  
				...  
				body of F  
				...  
				if (next_count > 0) signal(next);  
				else signal(mutex);  
	end;  
```  
  
    + Condition Variable Implementation  
