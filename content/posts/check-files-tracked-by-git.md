Title: Check files tracked by git  
Slug: check-files-tracked-by-git  
Date: 2015-02-18 11:39:37  
Authors: fkz  
Category: Note  
Tags: CLI, Git  
Summary: A brief solution to show a list of git tracked files.  
  
  
```zsh  
$ git ls-files  
```  
  
or  
  
```zsh  
$ git ls-tree -r ${branch} --name-only  
```  
  
---  
  
## Reference  
  
+ [How can I make git show a list of the files that are being tracked? - Stack Overflow](http://stackoverflow.com/questions/15606955/how-can-i-make-git-show-a-list-of-the-files-that-are-being-tracked)  
