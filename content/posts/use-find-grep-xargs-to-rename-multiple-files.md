Title: Use find, grep, xargs to Rename Multiple Files  
Date: 2014-11-10 13:44  
Author: fkz  
Category: Note  
Tags: CLI, find, grep, xargs, mv, rename  
Slug: use-find-grep-xargs-to-rename-multiple-files  
Modified: 2015-10-28 13:51  
  
  
Recursively find filenames ends up with `.vh` from pwd directory and change their names from `*.vh` to `*.vhd`  
  
  
```bash  
find | grep .vh$ | xargs -I {}.vh mv {}.vh {}.vhd  
```  
> This Only works with BSD `xargs` !!  
  
---  
  
## References  
  
+ <http://stackoverflow.com/questions/10212192/how-to-grep-for-a-filename-instead-of-the-contents-of-a-file>  
+ <http://viewsby.wordpress.com/2012/12/04/find-mvrename-with-xargs-example/>  
