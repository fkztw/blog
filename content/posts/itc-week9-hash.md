Title: ITC week9 - Hash  
Date: 2013-11-22 07:43  
Author: fkz  
Category: Course  
Tags: Cryptography, Security  
Slug: itc-week9-hash  
  
  
## NCTUCS 2013-Fall Introduction to Cryptography by Professor Rong-Jaye Chen.  
  
SHA 系列的比較表  
![SHA series](/files/itc-week9-hash/sha-series.jpg)  
  
> Hash 一定要夠快而且夠亂 才不容易被破解  
  
---  
  
![General Structure of Secure Hash Code](/files/itc-week9-hash/general-structure-of-secure-hash-code.png)  
  
---  
  
### compression function  
一個 Block 1024 bits 加 SHA-512 出來的 512 bits，出來就會變成原本的三倍  
  
---  
  
> Birthday attack 只要 2^32 就可以找到一個 collision  
  
---  
  
+ W0~W79 共 80 個 Rounds  
+ 2012 年 SHA-3 問世  
