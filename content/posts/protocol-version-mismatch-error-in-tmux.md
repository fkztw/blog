Title: Protocol version mismatch error in tmux  
Date: 2014-02-27 16:01  
Author: fkz  
Category: Note  
Tags: CLI, tmux  
Slug: protocol-version-mismatch-error-in-tmux  
Modified: 2015-10-26 13:28  
  
  
今天打 `$ tmux attach` 之後  
  
竟然噴了錯誤訊息 `protocol version mismatch (client 8, server 7)`  
  
以前完全沒看過  
  
只好丟去 Google  
  
第一個解法是 **強行 attach tmux**  
  
```  
$ pgrep tmux  
$ /proc/${tmuxpid}/exe attach  
```  
  
但執行後發現會噴 Permission Denied. 失敗  
  
第二個解法是 **把 tmux 砍掉重開**  
  
```  
$ pgrep tmux  
$ kill ${tmuxpid}  
```  
  
然後重開 tmux 就行了  
  
---  
  
#### References  
  
+ [protocol version mismatch (client 7, server 6)](https://bugs.launchpad.net/byobu/+bug/1174724)  
+ <https://plus.google.com/110139418387705691470/posts/BebrBSXMkBp>  
+ [Tmux 出現 protocol version mismatch 解法](http://blog.longwin.com.tw/2013/11/tmux-protocol-version-mismatch-fix-2013/)  
