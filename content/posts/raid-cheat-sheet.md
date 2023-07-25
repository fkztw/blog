Title: RAID Cheat Sheet  
Date: 2014-01-12 19:22  
Author: fkz  
Category: Note  
Tags: RAID, Cheat Sheet  
Slug: raid-cheat-sheet  
Modified: 2015-10-26 13:43  
  
## Format of the note below  
  
+ Type - Name  
    + Minimum Disks (M)  
    + Fault Tolerance Disks (F)  
    + Attributes (A)  
  
---  
  
+ RAID0 - Non Redundant Striping  
    + M: 2  
    + F: 0  
    + A: Block Level Striping  
+ RAID1 - Mirrored Disks  
    + M: 2  
    + F: n-1  
    + A: Mirroring  
+ RAID2 - Memory Style Error Correcting Codes  
    + M: 3  
    + F: 1 (Can Recover)  
    + A:  
        + Bit Level Striping  
        + Dedicated Hamming Code (Error Correction)  
        + Recovery  
+ RAID3 - Bit Interleaved Parity  
    + M: 3  
    + F: 1  
    + A:  
        + Bit Level Striping (Wikipedia said Byte Level)  
        + Dedicated Parity Code (Error Detection)  
+ RAID4 - Block Interleaved Parity  
    + M: 3  
    + F: 1  
    + A:  
        + Block Level Striping  
        + Dedicated Parity Code (Error Detection)  
+ RAID5 - Block Interleaved Distributed Parity  
    + M: 3  
    + F: 1  
    + A:  
        + Block Level Striping  
        + Distributed Parity Code (Error Detection)  
+ RAID6 - P + Q Redundancy  
    + M: 4  
    + F: 2  
    + A:  
        + Block Level Striping  
        + Double Distributed Parity Code (Error Detection) aka [Reed-Solomon Code](http://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)  
+ RAID01 - RAID0 + RAID1  
    + M: 4  
    + F: ?  
    + A: Striping First, then Mirroring.  
+ RAID10 - RAID1 + RAID0  
    + M: 4  
    + F: ?  
    + A: Mirroring First, then Striping.  
  
---  
  
## References  
+ [RAID - Wikipedia](http://en.wikipedia.org/wiki/RAID)  
+ [Reed-Solomon Error Correction - Wikipedia](http://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)  
