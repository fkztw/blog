Title: OS Ch1 - Introduction to Operating System  
Date: 2013-11-04 15:23  
Author: fkz  
Category: Course  
Tags: Operating System  
Slug: os-ch1-introduction-to-operating-system  
Modified: 2015-10-26 15:30  
  
  
* What is an Operating System?  
    * A program that acts as an intermediary between an application and the computer hardware  
    * A program that provides a convenient interface to the user  
    * Controls and coordinates use of hardware among various applications and users  
    * Provides a multi-user environment  
        * time-sharing  
    * Distributed computing  
    * Cloud computing  
    * a piece of program (or pieces of programs)  
    * a resource allocator  
    * a control program  
  
* Computer system can be divided into four components  
    * Hardware  
    * Operating system  
    * Application programs  
    * Users  
  
> “The one program running at all times on the computer” is the kernel."  
"Everything else is either a system program (ships with the operating system) or an application program."  
  
* Computer-System operation  
    * One or more CPUs, device controllers connect through common bus providing access to  
      shared memory  
    * Concurrent execution of CPUs and devices competing for memory cycles  
    * I/O devices and the CPU can execute concurrently  
    * Each device controller is in charge of a particular device type  
    * Each device controller has a local buffer  
    * CPU moves data from/to main memory to/from local buffers  
    * I/O is from the device to local buffer of controller  
    * Device controller informs CPU that it has finished its operation by causing an interrupt  
* ￼Common Functions of Interrupts  
    * Interrupt transfers control to the interrupt service routine generally, through the **interrupt vector, which contains the addresses of all the service routines**  
    * Interrupt architecture must save the address of the interrupted instruction  
    * Incoming interrupts are disabled while another interrupt is being processed to prevent       a lost interrupt  
    * A **trap is a software-generated interrupt caused either by an error or a user request**  
    * An operating system is **interrupt driven**  
  
* Interrupts  
![Interrupt Vectors in Liunx](/files/os-ch1/interrupt-vectors-in-linux.png)  
  
* I/O structure  
    * After I/O starts, control returns to user program only upon I/O completion  
        * Wait instruction idles the CPU until the next interrupt  
        * At most one I/O request is outstanding at a time, no simultaneous I/O processing  
  
    * **I/O muliplexing** After I/O starts, control returns to user program without waiting f			   or I/O completion  
        * **System call** – request to the operating system to allow user to wait for I/O  
        	completion  
        * **Device-status table** contains entry for each I/O device indicating its type,  
        	address, and state  
        * Operating system indexes into I/O device table to determine device status and to  
        	modify table entry to include interrupt  
  
* Direct Memory Access Structure (DMA)  
    * Device controller transfers blocks of data from buffer storage directly to main  
      memory without CPU intervention  
    * Only one interrupt is generated per block, rather than the one interrupt per byte  
  
* Storage Structure  
   * Main memory  
   * Secondary storage - extension of main memory that provides nonvolatile  
  	 capacity  
   * Magnetic disks  
       * Disk surface is logically divided into tracks, which are subdivided into sectors  
       * The **disk controller** determines the logical interaction between the device  
       	 and the computer  
       * NCQ vs no NCQ  
  
* Storage Hierarchy  
    * Speed  
    * Cost  
    * Volatility  
  
* Caching  
    * copying information into faster storage system; main memory  
      can be viewed as a last cache for secondary storage  
    * Information in use copied from slower to faster storage temporarily  
    * Faster storage (cache) checked first to determine if information is there  
    * Cache smaller than storage being cached  
        * Cache management important design problem  
        * Cache size and replacement policy  
  
* Computer-System Architecture  
    * single general-purpose processor (PDAs through mainframes)  
    * special-purpose processors  
    * Multiprocessors systems == parallel systems == tightly-coupled systems  
        * Increased throughput  
        * Economy of scale  
        * Increased reliability – graceful degradation or fault tolerance  
        * Two types  
            * Asymmetric Multiprocessing  
            * Symmetric Multiprocessing  
  
* Clustered Systems  
    * multiple systems working together  
    * Usually sharing storage via a storage-area network (SAN)  
    * Provides a high-availability service which survives failures  
        * Asymmetric clustering has one machine in hot-standby mode  
        * Symmetric clustering has multiple nodes running applications, monitoring  
          each other  
    * Some clusters are for high-performance computing (HPC). Applications must be written to 		 use parallelization  
  
* Computer Startup  
    1. bootstrap program is loaded at power-up or reboot  
        * Typically stored in ROM or EPROM, generally known as firmware  
        * Initializes all aspects of system  
        * Loads operating system kernel and starts execution  
    2. Operating system probes and initializes hardware  
    3. Hardware provides the driving power  
    4. Operating system administers the power to system services and applications (jobs)  
  
* Operating System Structure  
    * Multiprogramming  
        * Needed for efficiency  
        * Single user cannot keep CPU and I/O devices busy at all times  
        * Organizes jobs (code and data) so CPU always has one to execute  
        * A subset of total jobs in system is kept in memory  
        * One job selected and run via **job scheduling**  
        * When it has to wait (for I/O for example), OS **switches to another job**  
    * Timesharing (multitasking)  
        * logical extension in which CPU switches jobs so frequently that users can interact  
        	with each job while it is running, creating **interactive** computing  
        * **Response time** should be < 1 second  
        * Each user has at least one **program executing in memory => process**  
        * If several jobs ready to run at the same time => **CPU scheduling**  
        * If processes don’t fit in memory, **swapping** moves them in and out to run  
        * **Virtual memory** allows execution of processes not completely in memory  
  
* Operating-System Operations  
    * **Interrupt** driven by hardware  
    * Software error or request creates **exception** or **trap**  
        * Division by zero, request for operating system service  
    * **Dual-mode** operation allows OS to protect itself and other system components  
        * **User mode** and **kernel mode**  
        * **Mode bit** provided by hardware  
            * Provides ability to distinguish when system is running user code or kernel code  
            * Some instructions designated as **privileged**, only executable in kernel mode  
            * System call changes mode to kernel, return from call resets it to user  
        * Transition from User to Kernel Mode  
            * Timer to prevent infinite loop / process hogging resources  
                * Set interrupt after specific period  
                * Operating system decrements counter  
                * When counter zero generate an interrupt  
                * Set up before scheduling process to regain control or terminate program  
                  that exceeds allotted time  
  
* Process Management  
    * Single-threaded process has one **program counter** specifying location of  
      next instruction to execute  
        * Process executes instructions sequentially, one at a time, until completion  
    * **Multi-threaded process has one program counter per thread**  
    * Concurrency by multiplexing the CPUs among the processes / threads  
    * Process termination requires reclaim of any reusable resources  
    * Activities  
        * Creating and deleting both user and system processes  
        * Suspending and resuming processes  
        * Process synchronization  
        * Process communication  
        * Deadlock handling  
  
* Memory Management  
    * Determines what is in memory when optimizing CPU utilization and computer response to  
    	users  
    * Activities  
        * Keeping track of which parts of memory are currently being used and by whom  
        * Deciding which processes (or parts thereof) and data to move into and out of memory  
        * Allocating and deallocating memory space as needed  
  
* Storage Management  
    * OS provides uniform, logical view of information storage  
        * **file** - Abstracts physical properties to logical storage unit  
        * Each medium is controlled by device  
            * access speed  
            * capacity  
            * data-transfer rate  
            * access method (sequential or random)  
   * File-System management  
       * Access control on most systems to determine who can access what  
       * OS Activities  
           * Creating and deleting files and directories  
           * Primitives to manipulate files and dirs  
           * Mapping files onto secondary storage  
           * Backup files onto stable (non-volatile) storage media  
  
* Mass-Storage Management  
    * Disks used to store data that does not fit in main memory or data that must be kept for  
    	a “long” period of time  
    * WORM (write-once, read-many-times) and RW (read-write)  
    * OS activities  
        * Free-space management  
        * Storage allocation  
        * Disk scheduling  
  
* Performance of Various Levels of Storage  
![Performance of Various Levels of Storage](/files/os-ch1/performance-of-various-levels-of-storage.png)  
  
> Multitasking environments must be careful to use most recent value, no matter where it is stored in the storage hierarchy  
  
> Multiprocessor environment must provide cache coherency in hardware such that all CPUs have the most recent value in their cache  
  
* I/O Subsystem  
    * Memory management of I/O  
        * buffering (storing data temporarily while it is being transferred)  
        * caching (storing parts of data in faster storage for performance)  
        * spooling (the overlapping of output of one job with input of other jobs)  
    * General device-driver interface  
    * Drivers for specific hardware devices  
  
* Protection and Security  
    * **Protection** – any mechanism for controlling access of processes or users to resources defined by the OS  
    * **Security** – defense of the system against internal and external attacks  
        * denial-of-service, worms, viruses, identity theft, theft of service  
    * Some properties to check  
        * **uid, sid** - User identities (user IDs, security IDs), User ID then associated with all files, processes of that user to determine access control  
        * **gid** - Group identifier (group ID) allows set of users to be defined and controls managed, then also associated with each process, file  
        * **euid, egid** - **Privilege escalation** allows user to change to effective ID with more rights  
  
* Computing Environments  
    * **Compute-server** provides an interface to client to request services (i.e. database)  
    * **File-server** provides interface for clients to store and retrieve files  
  
* Peer-to-Peer Computing  
    * Another model of distributed system  
    * P2P does not distinguish clients and servers  
    * Node must join P2P network  
    * Broadcast request for service and respond to requests for service via discovery protocol  
    * Examples include Napster and Gnutella  
  
* Web-Based Computing  
  
* Cloud Computing  
  
* Open-Source Operating Systems  
    * Operating systems made available in source-code format rather than just binary closed-source  
    * Counter to the copy protection and Digital Rights Management (DRM) movement  
    * Started by Free Software Foundation (FSF), which has “copyleft” GNU Public License (GPL)  
    * Examples include **GNU/Linux**, **BSD UNIX** (including **core of Mac OS X**), and **Sun Solaris**  
