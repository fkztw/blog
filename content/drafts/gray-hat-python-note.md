Title: Gray Hat Python Note  
Slug: gray-hat-python-note  
Date: 2015-03-27 01:21:07  
Authors: fkz  
Category: Note  
Tags: Note, Gray Hat Python  
Summary: Just a Note for "Gray Hat Python"  
  
+ x86 debug register - DR7  
    + Why the types of breakpoint trigger only have  
        + 00 - on executino  
        + 01 - on data write  
        + 11 - on data read/write (but not execution)  
        + where's 10 ?  
            + 10b is defined to mean break on IO read or write but no hardware supports it.  
    + Why the lengths of breakpoint only have  
        + 00 - for 1 byte  
        + 01 - for 2 bytes  
        + 11 - for 4 btyes  
        + where's 10 ?  
            + 10b - for 8 bytes  
    + [x86 debug register - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/X86_debug_register#DR7_-_Debug_control)  
> DR7 - Debug control  
>  
> The low-order eight bits of DR7 (0,2,4,6 and 1,3,5,7) selectively enable the four address breakpoint conditions.  
> There are two levels of enabling: the local (0,2,4,6) and global (1,3,5,7) levels.  
> The local enable bits are automatically reset by the processor at every task switch to avoid unwanted breakpoint conditions in the new task.  
> The global enable bits are not reset by a task switch;  
> therefore, they can be used for conditions that are global to all tasks.  
>  
> Bits 16-17 (DR0), 20-21 (DR1), 24-25 (DR2), 28-29 (DR3), define when breakpoints trigger.  
> Each breakpoint has a two-bit entry that specifies whether they break on execution (00b), data write (01b), data read or write (11b).  
> 10b is defined to mean break on IO read or write but no hardware supports it.  
> Bits 18-19 (DR0), 22-23 (DR1), 26-27 (DR2), 30-31 (DR3), define how large an area of memory is watched by breakpoints.  
> Again each breakpoint has a two-bit entry that specifies whether they watch one (00b), two (01b), eight (10b) or four (11b) bytes.  
