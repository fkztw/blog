Title: asm hw3 - a small shooting game  
Date: 2013-04-10 22:07  
Author: fkz  
Category: Course  
Tags: assembly, MASM  
Slug: asm-hw3-a-small-shooting-game  
  
  
![Demo](/files/asm-hw3-a-small-shooting-game/demo.png)  
  
---  
  
Key usages:  
  
 * ‘a’ : leftmove: Step size 2.  
 * ‘d’ :rightmove: Step size 2.  
 * Spacebar:fire bullet: Step size 1.  
 * ESC : quit program  
  
---  
  
這學期修組語的第三次作業  
  
跟之前第二次的作業很類似 都是寫一個射擊遊戲  
  
不過這次的比較複雜  
  
但黃世強教授有先給 template 所以寫起來也不算太難  
  
這次的作業強調全部使用 Procedure  
  
讓整份 code 達到近乎 100% 的 modulization  
  
我覺得我寫出來算是蠻漂亮了  
  
要改設定幾乎都在 .data 的部分更改就可以完成了  
  
真正要縮減的大概就是 explosion 的 show 和 reset 吧...  
  
為了找怎麼樣在 user 按 Esc 的時候可以讀到 key  google 到這幾個網址  
  
+ <http://msdn.microsoft.com/en-us/library/ms927178.aspx>  
+ <http://programming.msjc.edu/asm/help/source/irvinelib/readkey.htm>  
  
總之就是看 dx 的值是不是 001Bh  是的話就是 ReadKey 讀到 Esc 了  
  
為了找哪個 symbol 當 user 控制的 spaceship 比較好看 google 到了 [Code page 437](http://en.wikipedia.org/wiki/Code_page_437)  
  
---  
  
系上組語都是使用 MASM 並搭配 Irvine32.lib  
  
這是課本提供的 Irvine 相關檔案  
<https://drive.google.com/folderview?id=0B4nAP-ilSfbjUnFJTkVaSFVQRUU&usp=sharing>  
  
可以搭配這份網路上找到的 Irvine32.asm 的 source code 一起學習  
<http://lcs.syr.edu/faculty/pease/handouts/CSE%20281/Irvine%20Programming%20Examples/Lib32/Irvine32_Library/Irvine32.asm>  
  
---  
  
source code 放在 gist 上  
<https://gist.github.com/M157q/5358879>  
  
---  
  
> 在 M$ 上用 codepad++ 的 tab 排版 gist 的 tab 縮排又不能選 4 格 看來有點悲劇= ="  
