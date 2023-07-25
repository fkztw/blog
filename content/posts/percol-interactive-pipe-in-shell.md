Title: percol - interactive pipe in shell  
Date: 2014-12-04 15:31  
Author: fkz  
Category: Note  
Tags: CLI, percol, Python, pip  
Slug: percol-interactive-pipe-in-shell  
Modified: 2015-10-28 13:48  
  
  
## [mooz/percol · GitHub](https://github.com/mooz/percol)  
  
Just like `less` + `grep` (in time) + `echo` (the result) to me.  
But the instant query filter maybe useful in some cases.  
  
### Installation  
  
```sh  
$ sudo pip2 install percol  
```  
  
### Examples  
  
+ `$ percol $file`  
+ `$ ps aux | percol`  
+ `$ git checkout $(git branch | percol)`  
