Title: Save Content of tmux/screen Scrollback Into A File  
Slug: save-content-of-tmux-or-screen-scrollback-into-a-file  
Date: 2015-07-27 01:03:26  
Authors: fkz  
Category: Note  
Tags: CLI, tmux, screen  
Summary: Steps to save content of tmux/screen scrollback into a file.  
Modified: 2016-09-12 00:24  
  
  
因為某些原因，  
想要把 tmux copy mode 裡面的內容 dump 出來。  
但因為之前沒試過，不知道該如何做，所以去查了一下，  
以下整理簡單步驟：  
  
## tmux  
  
+ 將指定的行數 (`$linenum`) 存到 buffer 中，進入 copy mode 後，即可在右上角看到行數。  
```tmux  
:capture-pane -S -$linenum  
```  
  
+ 將剛剛存到 buffer 中的內容，儲存到指定的檔案路徑 (`$filepath`)  
```tmux  
:save-buffer $filepath  
```  
  
+ 刪除 buffer 中的內容 (optional)  
```tmux  
:delete-buffer  
```  
  
+ `$filepath` 檔案中應該就是 dump 出來的內容  
  
---  
  
## screen  
  
`screen` 的話，目前看到的相似用法是  
  
```screen  
:hardcopy -h $filepath  
```  
  
但這個用法只能儲存全部的內容，無法選擇行數。  
  
然後我在 screen 版本 4.04.00 (GNU) 19-Jun-16 使用時，  
如果內容裏面有中文的話，  
dump 出來以後中文會變成亂碼。  
  
---  
  
## References  
  
+ [Write all tmux scrollback to a file - Unix & Linux Stack Exchange](http://unix.stackexchange.com/questions/26548/write-all-tmux-scrollback-to-a-file)  
+ [Copying GNU screen scrollback buffer to file (extended hardcopy)? - Stack Overflow](http://stackoverflow.com/questions/4807474/copying-gnu-screen-scrollback-buffer-to-file-extended-hardcopy)  
