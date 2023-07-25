Title: Recursively Delete Files with Specific Name in the Current Directory  
Slug: recursively-delete-files-with-specific-name-in-the-current-directory  
Date: 2015-02-26 15:42:42  
Authors: fkz  
Category: Note  
Tags: CLI, find, one-liner  
Summary: Recursively delete files with specific name by using `find` command  
Modified: 2015-10-28 14:11  
  
  
## Usage  
  
+ Delete all the files which have same name with `${filename}`.  
```sh  
find . -name "${filename}" -type f -delete  
```  
  
+ Delete all files with .bak file extension in the current dir  
```sh  
find . -name "*.bak" -type f -delete  
```  
  
---  
  
## Doc  
  
```txt  
-name pattern  
    True if the last component of the pathname being examined matches pattern.  
    Special shell pattern matching characters (``['', ``]'', ``*'', and ``?'') may be used as part of pattern.  
    These characters may be matched explicitly by escaping them with a backslash (``\'').  
```  
  
or you can use regular expression for file matching.  
  
```txt  
-regex pattern  
    True if the whole path of the file matches pattern using regular expression.  
    To match a file named ``./foo/xyzzy'', you can use the regular expression ``.*/[xyz]*'' or ``.*/foo/.*'',  
    but not ``xyzzy'' or ``/foo/''.  
```  
  
---  
  
## Reference  
  
+ [command line - How can I recursively delete all files of a specific extension in the current directory? - Ask Ubuntu](http://askubuntu.com/questions/377438/how-can-i-recursively-delete-all-files-of-a-specific-extension-in-the-current-di)  
  
