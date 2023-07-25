Title: find 指令排除指定路徑  
Date: 2014-05-21 15:10  
Author: fkz  
Category: Note  
Tags: CLI, find, sysadmin  
Slug: exclude-path-in-find-command  
Modified: 2015-10-28 14:29  
  
  
為了寫作業用到的  
參考 [linux - Exclude directory from find . command - Stack Overflow](http://stackoverflow.com/questions/4210042/exclude-directory-from-find-command)  
  
基本上就是  
  
```sh  
$ find $target_path -path $exclude_path -prune -o [condition] -print  
```  
  
---  
  
我自己的用法是  
  
```sh  
$ find / -path /proc -prune -o -perm o=w -type f -print  
```  
  
用來 print 出整個 `/` 底下除了 `/proc` 以外所有的 global writable 的 file  
  
---  
  
解答中甚至給出了要排除多個資料夾路徑的寫法  
  
```sh  
find $target_path -type d \( -path $exclude_path1 -o -path $exclude_path2 -o -path $exclude_path3 \) -prune -o -print  
```  
  
---  
  
## Appendix  
  
+ `-prune`  
	+ This primary always evaluates to true.  It causes find to not descend into the current file.  Note, the -prune primary has no effect if the -d option was specified.  
  
