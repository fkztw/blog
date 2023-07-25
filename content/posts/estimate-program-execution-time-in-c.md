Title: Estimate program execution time in C  
Date: 2013-05-30 16:35  
Author: fkz  
Category: Note  
Tags: C, Cpp  
Slug: estimate-program-execution-time-in-c  
Modified: 2015-10-28 13:15  
  
  
Just wanna estimate the process time of my algorithm homework.  
  
---  
  
# Method 1  
  
```c  
#include <sys/time.h>  
  
struct timeval t_start, t_end;  
  
gettimeofday(&t_start, NULL);  
double start = t_start.tv_sec + (double)t_start.tv_usec / 1000000;  
  
// Code to be estimated here  
  
gettimeofday(&t_end, NULL);  
double end = t_end.tv_sec + (double)t_end.tv_usec / 1000000;  
  
printf("%f seconds\n", end - start);  
```  
  
This method came from one of my Data Structure homework in last semester.  
  
Can estimated even if the process time is less than one second.  
  
This is the method which I prefer to use.  
  
But, [sys/time.h is a POSIX header, not part of the C/C++ standard library.](http://www.cplusplus.com/forum/beginner/22384/)  
  
So, this method can only be implemented on UNIX system.  
  
---  
  
# Method 2  
  
```c  
#include <time.h>  
  
clock_t start = clock();  
  
//Code to be estimated here  
  
clock_t end = clock();  
  
printf("%f seconds\n", (end - start) / (float)CLOCKS_PER_SEC);  
```  
  
This method seems be common used.  
  
But, seems it cannot estimate those process time less than one second.  
  
Don't Know why... even if I remove the / (float)CLOCKS_PER_SEC.   
  
It still comes out zero. O_o"  
