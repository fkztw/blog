Title: pip install lxml fail in Mac  
Slug: pip-install-lxml-fail-in-mac  
Date: 2015-02-04 15:39:08  
Modified: 2015-02-11 04:25:05  
Author: fkz  
Category: Note  
Tags: Python, pip, lxml, Mac, Pelican  
Summary: A brief solution to solve this problem  
  
  
While I built up the develope environment for `Pelican` on my Mac OSX 10.9,  
I encounterd this problem below:  
  
```txt  
In file included from src/lxml/lxml.etree.c:239:  
  
    /private/var/folders/v2/td9_yf3x7lv6myk_9cy1_h640000gn/T/pip-build-UkRKm0/lxml/src/lxml/includes/e  
tree_defs.h:14:10: fatal error: 'libxml/xmlversion.h' file not found  
  
    #include "libxml/xmlversion.h"  
```  
  
### Solution  
  
```bash  
$ brew install libxml2  
$ brew link libxml2 --force  
$ export C_INCLUDE_PATH=/usr/local/Cellar/libxml2/2.9.2/include/libxml2:$C_INCLUDE_PATH  
```  
  
### Reference  
  
- [python - Fail to install lxml in MacOS 10.8.4 - Stack Overflow](http://stackoverflow.com/questions/17857858/fail-to-install-lxml-in-macos-10-8-4)  
