Title: [Course] OS Ch9 - Virtual-Memory Management
Date: 2013-11-26 03:26
Author: fkz
Category: Course
Tags: Operating-System, Virtual-Memory
Slug: course-os-ch9-virtual-memory-management
Status: draft

## NCTUCS 2013-Fall Introduction to Operating System Hank Wu  
+ To describe the benefits of a virtual memory system  
+ To explain the concepts of demand paging, page-replacement algorithms, and allocation of page frames  
+ To discuss the principle of the working-set model  
  
<script async class="speakerdeck-embed" data-id="81ccbd30387801315ae85eae0478e863" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>  
  
[Slides can be found here.](https://speakerdeck.com/fkz/os-ch9-virtual-memory-management)  
  
<!--more-->  
  
---  
## Background  
> Virtual memory – separation of user logical memory from physical memory.  
  
+ 可讓 fork 更有效率，透過 Page Table 和 Virtual Memory 可以不用真的把 Parent 的 Physical Memory 複製到 Child 中，而是讓他看起來像是多複製了一份出來，但實際上還是只有一份。  
  
### ￼Virtual Memory That is Larger Than Physical Memory  
  
` $ cat /proc/self/maps `  
見 p.5 的圖  
  
+ Virtual Memory 分散在各個角落 (2^64)  
+ 圖中右邊看到的區段是用 Page Table 隔出來的，不是 Segmentation 隔出來的  
    + Page Table 的 Entry 相同  
    + 每個 Page Table 的 Entry 都要設定權限  
      
+ 虛擬記憶體為何可以比實體記憶體大?  
    + Address Space 可以比 Physical 還大 => 最大可到達 2^64 而物理記憶體實際上可能很小  
      
### Virtual-address Space  
見 p.7 的圖  
  
### ￼Shared Library Using Virtual Memory  
見 p.8 的圖  
  
---  
## Demand Paging  
  
+ 降低 Memory 需求量  
+ 將 Memory 做更有效率的配置  
+ 可以容納更多的 User 同時使用  
  
+ 如果要存取的 Page 不存在，OS 必須要能夠知道。  
    + Invalid Reference (Page Fault) => Abort  
    + Disk 還沒把資料 load 到對應的 Memory Frame => OS 要負責把對應的資料從 Disk load 到記憶體，並產生相對應的 Page Table  
      
+ Lazy swapper => 等到真的要做的時候才拿出來用，不會預先作處理。  
  
### ￼Transfer of a Paged Memory to Contiguous Disk Space  
見 p.10 的圖  
  
> 手機的記憶體不大，也是利用了 Virtual Memory 來達到比較好的使用者體驗。但和桌上型電腦比起來，因為手機的硬碟大都為 Flash，所以 Data 從 Disk load 到 Memory 的速度會比較快些。  
  
### Valid-Invalid Bit  
> 需要有個欄位來記載目前這個 Page 有沒有 Map 到一個 Frame  
> v => in-memory  
> i => not-in-memory  
  
如果在使用 Memory 時，發現 Valid-Invalid Bit 為 i 時，則代表記憶體存取錯誤。  
  
### ￼Page Table When Some Pages Are Not in Main Memory  
見 p.12 的圖  
  
### Page Fault  
  
+ 會跳到 OS 對應的 Page Table Handler 的 Function 中  
+ 作業系統自己會有另外一個 table (文中提到的 Another Table) 去紀錄使用的記憶體，CPU 不會看這個 Table  
  
見 p.13 的圖  
  
> Page Fault 也有可能會發生在 Kernel Space  
  
### Steps in Handling a Page Fault  
見 p.15 的圖  
  
### ￼Performance of Demand Paging  
  
+ Page Fault Rate  
  
```mathjax  
0 \leqslant p \leqslant 1.0  
```  
  
+ Effective Access Time (EAT)  
  
```mathjax  
\text {EAT} = \left (  1-p\right ) \times \text {memory access} \\  
+ p \times \left( \text{page fault overhead} + \text{swap page out} + \text{swap page in} + \text{restart overhead} \right )  
```  
  
---  
## Copy-on-Write (COW)  
## Page Replacement  
## Allocation of Frames  
## Thrashing  
## Memory-Mapped Files  
## Allocating Kernel Memory  
## Other Considerations  
## Operating-System Examples  
