Title: Screen copy mode scrollback 行數不夠  
Date: 2014-05-27 15:57  
Author: fkz  
Category: Note  
Tags: CLI, screen, copy mode, history buffer  
Slug: not-enough-lines-for-scrollback-in-screen-copy-mode  
Modified: 2015-10-28 14:21  
  
  
今天剛好有兩個人都問了這個問題  
  
> 「screen 可以回捲的行數不夠怎麼辦?」  
  
所以就寫下來記錄一下  
--其實是直接複製貼上--  
  
---  
  
## 第一種解法：跟 screen 無關  
  
關於您的問題應該是不用升級版本就可以解決的  
只要將您的指令 pipe 給 less  
  
```sh  
$ (Your command) | less  
```  
  
或是使用 `>` 將程式的輸出結果導到某個檔案中  
  
```sh  
$ (Your command) > $file  
```  
  
再使用 `less` 或是您慣用的編輯器開啟  
  
`less $file`, `vim $file`, `emacs $file`, ...  
  
---  
  
## 第二種解法：從 screen 的設定下手  
  
如果您想要從 screen 的方面下手的話  
可以參考 <http://www.gnu.org/software/screen/manual/screen.html>  
  
  
### 情況一：仍未開啟 screen  
  
在開啟 `screen` 的時候 加上 `-h $num`  
> `$num` 代表可以往上捲幾行  
  
`screen` 預設為 100  
  
  
### 情況二：已經開啟 screen  
  
如果已經開啟 `screen` 的話  
可以在 `screen` 的 cli 環境中輸入  
  
```screen  
:defscrollback $num  
```  
> `$num` 一樣代表可以往上捲幾行  
  
則新開啟的 `screen` 分頁會套用此設定  
