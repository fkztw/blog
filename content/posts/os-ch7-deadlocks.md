Title: OS Ch7 - Deadlocks  
Date: 2013-11-19 02:40  
Author: fkz  
Category: Course  
Tags: Operating System, Deadlock  
Slug: os-ch7-deadlocks  
  
  
# OS == Operating System  
# Ch7 - Deadlocks  
  
+ Prevent sets of concurrent processes from completing their tasks.  
+ To present a number of different methods for preventing or avoiding deadlocks in a computer system.  
  
---  
## The Deadlock Problem  
> A set of blocked processes each holding a resource and waiting to acquire a resource held by another process in the set.  
  
#### Bridge Crossing Example  
  
* Most OSes do not prevent or deal with deadlocks  
  
---  
## System Model  
  
* Resource types R1, R2, . . ., Rm  
    CPU cycles, memory space, I/O devices  
  
* Each resource type Ri has Wi instances.  
  
* Each process utilizes a resource as follows:  
    * request  
    * use  
    * release  
  
---  
## Deadlock Characterization  
![Deadlock Characterization](/files/os-ch7-deadlocks/deadlock-characterization.jpg)  
  
### Resource-Allocation Graph  
![Resource-Allocation Graph 1](/files/os-ch7-deadlocks/resource-allocation-graph-1.jpg)  
![Resource-Allocation Graph 2](/files/os-ch7-deadlocks/resource-allocation-graph-2.jpg)  
  
+ Resource Allocation Graph With A Deadlock  
![Resource Allocation Graph With A Deadlock](/files/os-ch7-deadlocks/resource-allocation-graph-with-a-deadlock.jpg)  
+ Resource Allocation Graph With A Cycle But No Deadlock  
![Resource Allocation Graph With A Cycle But No Deadlock](/files/os-ch7-deadlocks/resource-allocation-graph-with-a-cycle-but-no-deadlock.jpg)  
  
### Basic Facts  
+ If graph contains no cycles => no deadlock  
+ If graph contains a cycle =>  
    + if only one instance per resource type, then deadlock  
    + if several instances per resource type, possibility of deadlock  
  
---  
## Methods for Handling Deadlocks  
+ Ensure that the system will never enter a deadlock state  
+ Allow the system to enter a deadlock state and then recover  
+ Ignore the problem and pretend that deadlocks never occur in the system; used by most operating systems, including UNIX  
  
---  
## Deadlock Prevention  
  
* **Mutual Exclusion** - not required for sharable resources; must hold for nonsharable resources  
  
* **Hold and Wait** - must guarantee that whenever a process requests a resource, it does not hold any other resources  
    * **Require process to request and be allocated all its resources before it begins execution**  
    * Allow process to request resources only when the process has none  
    * Low resource utilization  
    * Starvation possible  
  
* **No Preemption** (preemption - 先發制人)  
>某個 process 用完 resources 後，一定要該 process 自願釋出 resources ，不能強制奪取其 resources.  
    * **If a process that is holding some resources requests another resource that cannot be immediately allocated to it, then all resources currently being held are released**  
    * Preempted resources are added to the list of resources for which the process is waiting  
    * Process will be restarted only when it can regain its old resources, as well as the new ones that it is requesting  
  
* **Circular Wait**  
    * impose a total ordering of all resource types => 可能非常非常的多  
    * require that each process requests resources in an **increasing order of enumeration**  
  
  
* **Deadlock prevention by resource ordering** - Linux kernel 3.6.7 use this method.  
![double_rq_lock](/files/os-ch7-deadlocks/double-rq-lock.png)  
> 當你可能需要把某個 process 從一個 core 移到另一個 core (作 Load balance) 的時候，兩邊的 core 都要使用 lock 。  
    * All resources will be requested in order. => **total ordering**  
    * No two resources unrelated by order will ever be used by a single unit of work at the same time.  
  
---  
## Deadlock Avoidance  
  
* Simplest and most useful model requires that each process declare the maximum number of resources of each type that it may need  
  
* The deadlock-avoidance algorithm dynamically examines the resource-allocation state to ensure that there can never be a circular-wait condition  
  
* Resource-allocation state is defined by the number of available and allocated resources, and the maximum demands of the processes  
  
### Safe State  
  
* When a process requests an available resource, **system must decide if immediate allocation leaves the system in a safe state**.  
  
```mathjax  
\begin{align}  
  
& \text{ System is in safe state if there exists a sequence } \langle P_{1}, P_{2}, \cdots, P_{n} \rangle \\  
& \text{ of ALL the processes in the systems such that for each } P_{i} \\  
& \text{ , the resources that } P_{i} \text{ can still request can be satisfied } \\  
& \text{ by currently available resources + resources held by all the } P_{j}, \text{ with } j < i \\  
  
\end{align}  
```  
  
```mathjax  
\begin{align}  
& \text { If } P_{i} \text{ resource needs are not immediately available, } \\  
& \text{ then } P_{i} \text{ can wait until all } P_{j} \text{ have finished. } \\  
& \text{     When } P_{j} \text{ is finished, } \\  
& P_{i} \text{ can obtain needed resources, execute, return allocated resources, and terminate. } \\  
& \text{     When } P_{i} \text{ terminates, } P_{i+1} \text{ can obtain its needed resources, and so on } \\  
\end{align}  
```  
  
#### Basic Facts  
  
* If a system is in safe state => no deadlocks  
* If a system is in unsafe state => possibility of deadlock  
* **Avoidance => ensure that a system will never enter an unsafe state.**  
  
  
### Avoidance algorithms  
  
* **Single** instance of a resource type => Use a **resource-allocation graph**  
* **Multiple** instances of a resource type => Use **the banker’s algorithm**  
  
### Resource-Allocation Graph Scheme  
  
```mathjax  
\begin {align}  
& \text{ Claim edge } P_{i} \rightarrow R_{j} \text{ indicated that process } P_{j} \text{ may request resource } R_{j} \text{ ; }\\  
& \text{ represented by a dashed line. }  
\end {align}  
```  
  
* Claim edge converts to request edge when a process requests a resource  
* Request edge converted to an assignment edge when the resource is allocated to the process  
* When a resource is released by a process, assignment edge reconverts to a claim edge  
* Resources must be claimed a **priori** in the system  
  
### Resource Allocation Graph  
![Resouce Allocation Graph 3](/files/os-ch7-deadlocks/resource-allocation-graph-3.png)  
  
#### Unsafe State Resource Allocation Graph  
![Unsafe State Resource Allocation Graph](/files/os-ch7-deadlocks/unsafe-state-resource-allocation-graph.png)  
  
### Resource-Allocation Graph Algorithm  
+ The request can be granted only if converting the request edge to an assignment edge does not result in the formation of a cycle in the resource allocation graph  
  
#### Banker’s Algorithm  
> 檢查之後有沒有可能進到 Unsafe State  
  
+ Multiple instances  
+ Each process must a priori claim maximum use  
+ When a process requests a resource it may have to wait  
+ When a process gets all its resources it must return them in a finite amount of time  
  
##### Data Structures for the Banker’s Algorithm  
![Data Structures for the Banker’s Algorithm](/files/os-ch7-deadlocks/bankers-algorithm.png)  
  
#### Safety Algorithm  
![Safety Algorithm](/files/os-ch7-deadlocks/safety-algorithm.png)  
> process 有可能還需要 resource, 可以由 work 提供  
  
### ￼Resource-Request Algorithm for Process Pi  
  
```python  
# Request = request vector for process P[i]  
# If Request[i][j] = k then,  
# process P[i] wants k instances of resource type R[j]  
  
# 1.  
If Request[i] <= Need[i]: goto step2  
else: raise error condition  
# since process has exceeded its maximum claim  
  
# 2.  
If Request[i] <= Available: goto step3  
else: P[i] wait  
# since resources are not available  
  
# 3.  
# Pretend to allocate requested resources to Pi  
# by modifying the state as follows:  
  
Available = Available – Request[i]  
Allocation[i] = Allocation[i] + Request[i]  
Need[i] = Need[i] – Request[i]  
```  
+ If safe => the resources are allocated to Pi  
+ If unsafe => Pi must wait, and the old resource-allocation state is restored  
  
> Available == 當下系統可用的 Resource 的量  
> Resource-Request Algorithm 很少在用，主要的原因是因為 Avaliable 不好估算，如果 Avaliable 無法得知的話，這個 Algorithm 基本上沒什麼用，這邊只是表達一下觀念。  
  
---  
## Deadlock Detection  
+ Allow system to enter deadlock state  
+ Detection algorithm  
+ Recovery scheme  
  
### Single Instance of Each Resource Type  
![Single Instance of Each Resource Type](/files/os-ch7-deadlocks/single-instance-of-each-resource-type.jpg)  
  
### Resource-Allocation Graph and Wait-for Graph  
![Resource-Allocation Graph and Wait-for Graph](/files/os-ch7-deadlocks/resource-allocation-graph-and-wait-for-graph.jpg)  
  
### Several Instances of a Resource Type  
![Several Instances of a Resource Type](/files/os-ch7-deadlocks/several-instances-of-a-resource-type.jpg)  
  
### Detection Algorithm  
![Detection Algorithm 1](/files/os-ch7-deadlocks/detection-algorithm-1.jpg)  
![Detection Algorithm 2](/files/os-ch7-deadlocks/detection-algorithm-2.jpg)  
  
> Algorithm requires an order of O(m * n^2) operations to detect whether the system is in deadlocked state  
  
#### Example of Detection Algorithm  
![Example of Detection Algorithm 1](/files/os-ch7-deadlocks/example-of-detection-algorithm-1.jpg)  
![Example of Detection Algorithm 2](/files/os-ch7-deadlocks/example-of-detection-algorithm-2.jpg)  
  
#### Detection-Algorithm Usage  
+ When, and how often, to invoke depends on:  
    + How often a deadlock is likely to occur?  
    + How many processes will need to be rolled back?  
        + one for each disjoint cycle  
+ If detection algorithm is invoked arbitrarily, there may be many cycles in the resource graph and so we would not be able to tell which of the many deadlocked processes “caused” the deadlock  
  
---  
## Recovery from Deadlock  
### Process Termination  
+ Abort all deadlocked processes  
+ Abort one process at a time until the deadlock cycle is eliminated  
+ In which order should we choose to abort?  
    + Priority of the process  
    + How long process has computed, and how much longer to completion  
    + Resources the process has used  
    + Resources process needs to complete  
    + How many processes will need to be terminated  
    + Is process interactive or batch?  
  
### Resource Preemption  
+ Selecting a victim => minimize cost  
+ Rollback => return to some safe state, restart process for that state  
+ Starvation => same process may always be picked as victim, include number of rollback in cost factor  
