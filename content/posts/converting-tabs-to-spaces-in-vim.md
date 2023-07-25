Title: Converting tabs to spaces in Vim  
Date: 2014-12-09 07:28  
Author: fkz  
Category: Note  
Tags: CLI, Vim, Makefile  
Slug: converting-tabs-to-spaces-in-vim  
Modified: 2015-10-28 13:41  
  
  
## Convert tabs to spaces  
  
```vim  
:retab  
```  
  
---  
  
## Set the 1 tab to be expanded to 4 spaces  
  
```vim  
:set tabstop=4 shiftwidth=4 expandtab  
```  
  
---  
  
## Comments below have some useful tips for some specail cases (like Makefile)  
  
![Comment 1](/files/converting-tabs-to-spaces-in-vim/comments_1.png)  
  
![Comment 2](/files/converting-tabs-to-spaces-in-vim/comments_2.png)  
  
![Comment 3](/files/converting-tabs-to-spaces-in-vim/comments_3.png)  
  
---  
  
## Reference  
  
+ [Converting tabs to spaces - Vim Tips Wiki](http://vim.wikia.com/wiki/Converting_tabs_to_spaces)  
